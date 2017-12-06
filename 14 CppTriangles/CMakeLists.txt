set (triangle_sources triangles.cpp)
set (piglatin_sources piglatin.cpp)

format(FILES ${triangle_sources} ${piglatin_sources})
lint(FILES ${triangle_sources} ${piglatin_sources})

add_executable(cpp_triangles ${triangle_sources})
add_executable(cpp_piglatin ${piglatin_sources})
# target_include_directories(helloworld_test SYSTEM PUBLIC ${CMAKE_SOURCE_DIR}/gtest/googletest/include)
# target_include_directories(helloworld_test PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})
# add_test(NAME 0_cpp_helloworld COMMAND $<TARGET_FILE:helloworld_test>)
