#!/usr/bin/env python3
# Shebang to allow autoexecution of script on UNIX-likes


import iindex_core as ii  # Use code from my iindex_core.py file


def filter_non_alphanumeric(x):
    '''
    inputs: x - string to filter
    output: filtered string that only contains alphanumeric characters or '@.,
    '''
    return "".join([v for v in x.lower() if ('a' <= v <= 'z' or
                                             '0' <= v <= '9' or
                                             v in "\'@.,"
                                             )])

if __name__ == "__main__":
    # Build the index based on offenders.csv using the 4th column as the result (the "document")
    # and using the 9th column as the data column. This will automatically split all values in the csv by
    # spaces. Additionally all values in the csv will be passed to the filter function to get them ready
    # for entry in the index.
    index = ii.iindex_build_csv("offenders.csv", document_column=3, data_columns=8,
                                split=' ', filt=filter_non_alphanumeric)

    # REPL!
    while True:
        # If you try to exit with ctrl-c or ctrl-d, exit gracefully w/o traceback
        try:
            search = input("Enter search terms for offenders.csv\n> ")
        except (EOFError, KeyboardInterrupt):  # ctrl-d, ctrl-c respectivly
            print()  # Need a newline in there
            exit()

        # Search through the index for with the search terms, splitting the terms on the space
        # and applying the same filter that the index was created with
        results = ii.iindex_search(index, search, split=' ', filt=filter_non_alphanumeric)

        # Generate the result header. This is of variable length based on number and if there is an S
        # or period on the end. This is necessary for pretty printing the results
        header_text = "{} Result{}".format(len(results),
                                           's.' if len(results) == 0 else
                                           ('s:' if len(results) != 1 else ':'))

        # Convience variable for clarity
        header_length = len(header_text)

        # Pregenerate the header for each result. This is composed of a newline and enough
        # spaces to have the result start one column to the right of the space after "X Results:"
        # Please note this isn't used BEFORE the first result only between results due to the use
        # of .join() at the end.
        per_element_header = ("\n" + " " * (header_length + 1))

        # Sort the results first then add an extra newline at the end for pretty endings
        print("{} {}".format(header_text,
                             per_element_header.join(sorted(results))),
              '\n')
