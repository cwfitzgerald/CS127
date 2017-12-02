set (exe_sources coding_bat.cpp)

format(FILES ${exe_sources})
lint(FILES ${exe_sources})

add_executable(helloworld ${exe_sources})
# target_include_directories(helloworld_test SYSTEM PUBLIC ${CMAKE_SOURCE_DIR}/gtest/googletest/include)
# target_include_directories(helloworld_test PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
# add_test(NAME 0_cpp_helloworld COMMAND $<TARGET_FILE:helloworld_test>)
