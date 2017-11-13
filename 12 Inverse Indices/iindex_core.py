#!/usr/bin/env python3

import collections
import csv
import functools
import itertools
import operator
import os
import pprint


def iindex_build_csv(filename, document_column, data_columns=None, header=True, split=None, filt=None):
    '''
    inputs: filename        - csv file to load
            document_column - column of csv to use as the name of the "document"
            data_columns    - list of column indices to use as data. None (default) means all of them
            header          - if csv file has a row for a header
            split           - letter to split columns by
            filt            - function that will be called on each element in csv
                              string -> string
    output: dicitonary mapping each data member to the set of documents that they are a part of
    '''
    filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    d = collections.defaultdict(lambda: set())

    with open(filename, newline='') as file:
        csvreader = csv.reader([line for line in file])
        data = list(csvreader)[1:] if header else list(csvreader)
        for row in data:
            if data_columns is None:
                keys = row[:document_column] + row[document_column + 1:]
            elif isinstance(data_columns, list):
                if len(data_columns) > 1:
                    keys = operator.itemgetter(*data_columns)(row)
                else:
                    keys = [row[data_columns[0]]]
            else:
                keys = [row[data_columns]]

            if not (split is None):
                keys = itertools.chain.from_iterable([val.split(split) for val in keys])

            document_data = row[document_column]

            if not (filt is None):
                keys = map(filt, keys)
                document_data = filt(document_data)

            for k in keys:
                d[k].add(document_data)

    return d


def iindex_search(dictionary, search_term, split=None, filt=None):
    if not isinstance(search_term, list):
        search_term = [search_term]

    if not (split is None):
        search_term = itertools.chain.from_iterable([search.split() for search in search_term])

    if not (filt is None):
        search_term = map(filt, search_term)

    search_term = list(search_term)

    if len(search_term) > 1:
        return set(functools.reduce(operator.and_, operator.itemgetter(*search_term)(dictionary)))
    else:
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
