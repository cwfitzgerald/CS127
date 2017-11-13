#!/usr/bin/env python3

import iindex_core as ii
import itertools


def filter_non_alphanumeric(x):
    return "".join([v for v in x.lower() if ('a' <= v <= 'z' or
                                             '0' <= v <= '9' or
                                             v in "\'@.,"
                                             )])

if __name__ == "__main__":
    index = ii.iindex_build_csv("offenders.csv", document_column=3, data_columns=8,
                                split=' ', filt=filter_non_alphanumeric)
    while True:
        try:
            search = input("Enter search terms for offenders.csv\n> ")
        except (EOFError, KeyboardInterrupt):
            print()
            exit()
        results = ii.iindex_search(index, search, split=' ', filt=filter_non_alphanumeric)

        header_text = "{} Result{}".format(len(results), 's' if len(results) != 1 else '')

        header_length = len(header_text)

        per_element_header = ("\n" + "".join(itertools.repeat(" ", header_length + 2)))

        print("{}: {}".format(header_text, per_element_header.join(sorted(results))), '\n')
