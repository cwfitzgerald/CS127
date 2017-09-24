add_python_program(NAME  4_py_madlibs
                   FILES madlibs.py
                         collatz.py
                         comma.py
                         picture.py
                   TESTS tests/test_madlibs.py
                         tests/test_collatz.py
                         tests/test_comma.py
                         tests/test_picture.py
                   )