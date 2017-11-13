set (CMAKE_CXX_STANDARD 17)

add_python_program(NAME 11_py_markov
                   FILES mc.py
                   DATA hamlet.txt psalms.txt sonnets.txt
                   #TESTS tests/test_madlibs.py
                   )
add_executable(11_cpp_markov cppmarkov.cpp)