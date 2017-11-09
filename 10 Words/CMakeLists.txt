add_python_program(NAME 10_py_words
                   FILES wc.py
                   DATA hamlet.txt psalms.txt sonnets.txt
                   #TESTS tests/test_madlibs.py
                   )
add_executable(10_py_markov cppmarkov.cpp)
target_compile_options(10_py_markov BEFORE PUBLIC -std=c++1z)