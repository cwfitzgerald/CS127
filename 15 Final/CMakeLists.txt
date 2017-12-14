set (cpp_1 presents.cpp)
set (cpp_2 sum.cpp)

add_python_program(NAME 15_py_final
                   FILES canibals.py circle_bounds.py
                   )

format(FILES ${cpp_1} ${cpp_2})
lint(FILES ${cpp_1} ${cpp_2})

add_executable(cpp_final_presents ${cpp_1})
add_executable(cpp_final_sums ${cpp_2})
