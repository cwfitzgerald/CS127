add_python_program(NAME 12_py_inverse_indices
                   FILES iindex_core.py offender_search.py sample_search.py
                   DATA sample.csv offenders.csv
                   #TESTS tests/test_madlibs.py
                   )