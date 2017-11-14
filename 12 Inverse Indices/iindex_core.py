#!/usr/bin/env python3

# Here is the core library code that forms the basis of my little search engine
# This file is imported by various other programs that use it for doing searches
# The functions here are generic so they can be used to parse many-a csv

# For reference a set is like a list, but it is unordered, and is unique - there is only
# ever one copy of a value at any one time

import collections
import csv          # Parsing CSV files
import functools
import itertools
import operator
import os           # For path manipulations
import pprint


def iindex_build_csv(filename, document_column, data_columns=None, header=True, split=None, filt=None):
    '''
    inputs: filename        - csv file to load
            document_column - column of csv to use as the name of the "document"
            data_columns    - list of column indices to use as data. None (default) means all of them
            header          - if csv file has a row for a header
            split           - character to split columns by
            filt            - function that will be called on each element in csv
                              string -> string
    output: dicitonary mapping each data member to the set of documents that they are a part of
    '''

    # Allow you to call a program from a different directory while still retaining relative filenames
    # An average python user won't encounter this much, but this is important for how I run my code
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    # The dictionary should initialize the value of any new key to an empty set
    # A lambda is a mini function that returns what is to the right of the colon
    d = collections.defaultdict(lambda: set())

    # Open the file
    with open(filename) as file:
        # Parse the csv into rows and columns using the csv module
        csvreader = csv.reader(file)

        # If the data has a header, we want to chop off the first element of the
        # list of lists (the first row).
        # Due to an implimentation detail of csv.reader (returning an unsliceable iterable),
        # we must convert it to a list first though that is unnessary if we don't need to slice
        if header:
            data = list(csvreader)[1:]
        else:
            data = csvreader

        # Go through each row in the csv
        for row in data:
            # If data_columns is None (the default) we want all columns but the
            # document_column to be used as a key. We get an array of the contents.
            if data_columns is None:
                # Slice around the document_column
                keys = row[:document_column] + row[document_column + 1:]

            # If we are passed a list for data columns, we want to get the values
            # of all the appropriate rows.
            elif isinstance(data_columns, list):
                # We need to treat single columns differently to ensure the keys are list
                # of only one item. This assumption is throughout the rest of the function
                if len(data_columns) > 1:
                    # operator.itemgetter(*list_of_indices)(array) is a fancy way of getting a list of
                    # return values from indexing into the array multiple times. Equivilant to the following:
                    # keys = []
                    # for i in data_columns:
                    #     keys += row[i]
                    keys = operator.itemgetter(*data_columns)(row)
                else:
                    # Get the only needed data column, but put it in to a list of 1. This is done by the
                    # outside brackets that seemingly do nothing productive.
                    keys = [row[data_columns[0]]]

            # If we are passed a single number in data_columns it will fall here.
            # We must still ensure keys is an array for later processing
            else:
                keys = [row[data_columns]]

            # If we are passed a value to split by we must split all keys
            if not (split is None):
                # Apply the split
                array_of_split_keys = [val.split(split) for val in keys]

                # Array_of_split_keys is an array of arrays, so we need to flatten it from a 2D array
                # to a 1D array. itertools.chain.from_iterable does this.
                keys = itertools.chain.from_iterable(array_of_split_keys)

            # Grab the data that we will act is the document name
            document_data = row[document_column]

            # If there is a filter function, we must apply it to all keys and the document name itself
            if not (filt is None):
                # map calls filt on all elements of keys and returns and "array"
                keys = map(filt, keys)
                # call the function directly
                document_data = filt(document_data)

            # Add each key to point to the document
            for k in keys:
                d[k].add(document_data)

    # Return the inverse index
    return d


def iindex_search(dictionary, search_term, split=None, filt=None):
    '''
    inputs: dictionary      - generated inverted index
            search_term     - a string or a list of strings telling what to search for
            split           - character to split search_terms by
            filt            - function that will be called on each search term
                              string -> string
    output: a set of all result document name
    '''

    # If we aren't passed a list, make search_term a list of one
    if not isinstance(search_term, list):
        search_term = [search_term]

    # If we have a function to split by, apply the split
    if not (split is None):
        # Apply the split
        array_of_split_search_terms = [search.split() for search in search_term]

        # Flatten the list of lists into a single 1D list
        search_term = itertools.chain.from_iterable(array_of_split_search_terms)

    # Apply the filter to each search term
    if not (filt is None):
        search_term = map(filt, search_term)

    # Ensure search_term is a list for...reasons
    search_term = list(search_term)

    # Single searches need special treatment due to array vs non-array problems
    if len(search_term) > 1:
        # Get a list of the sets that match each search term
        result_sets = operator.itemgetter(*search_term)(dictionary)

        # Reduce the list of sets over operator binary-and
        # Explaination:
        # A reduction (or fold) is a higher older function that combines every element in a list
        # by calling the function on two elements at a time.
        # A sum of a list is an example of a reduction using operator.plus
        #
        # Calling operator binary-and on two sets produces a new set that contains
        # all elements that both share (Intersection for Stats people). By doing this over
        # a large list of sets, I will find only the documents that have matches for every single
        # search term
        unique_results = functools.reduce(operator.and_, result_sets)

        # Turn the unique results into a set and return it
        return set(unique_results)
    else:
        # If there is only a single search term, find the set of results for the term and return it
        return dictionary[search_term[0]]


if __name__ == "__main__":
    def filter_non_alphanumeric(x):
        return "".join([v for v in x.lower() if ('a' <= v <= 'z' or
                                                 '0' <= v <= '9' or
                                                 v in "\'@.,"
                                                 )])

    # print(["{}, {}".format(x, str(x) <= '1') for x in range(10)])
    sampledict = (iindex_build_csv("sample.csv", document_column=2, filt=filter_non_alphanumeric))
    offenddict = (iindex_build_csv("offenders.csv", document_column=3, data_columns=8, split=' ',
                                   filt=filter_non_alphanumeric))

    result = iindex_search(sampledict, "Eri,cha Female", split=' ', filt=filter_non_alphanumeric)
    result = iindex_search(offenddict, "Sorry God love", split=' ', filt=filter_non_alphanumeric)

    pprint.pprint(result)
