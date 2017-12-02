set (lib_sources get_hello.cpp)
set (exe_sources main.cpp)
set (test_sources tests/test.cpp)

set (headers get_hello.hpp)

set (files ${lib_sources} ${exe_sources} ${test_sources} ${headers})

format(FILES ${files})
lint(FILES ${lib_sources} ${exe_sources} ${test_sources})

add_library(helloworld_gen STATIC ${lib_sources})
add_executable(helloworld ${exe_sources})
add_executable(helloworld_test ${test_sources})
target_link_libraries(helloworld helloworld_gen)
target_link_libraries(helloworld_test helloworld_gen gtest gtest_main)
target_include_directories(helloworld_test SYSTEM PUBLIC ${CMAKE_SOURCE_DIR}/gtest/googletest/include)
target_include_directories(helloworld_test PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
add_test(NAME 0_cpp_helloworld COMMAND $<TARGET_FILE:helloworld_test>)
