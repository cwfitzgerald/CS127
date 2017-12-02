set (CMAKE_CXX_STANDARD 17)

add_python_program(NAME 10_py_words
                   FILES wc.py wc_speed.py
                   DATA hamlet.txt psalms.txt sonnets.txt
                   #TESTS tests/test_madlibs.py
                   )
add_executable(10_cpp_markov cppmarkov.cpp)
add_executable(10_cpp_markov_faster cppmarkov-faster.cpp)

lint(FILES cppmarkov.cpp cppmarkov-faster.cpp)
format(FILES cppmarkov.cpp cppmarkov-faster.cpp)
