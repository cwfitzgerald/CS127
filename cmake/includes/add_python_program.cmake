include(CMakeParseArguments)

find_package(PythonInterp 3.1 REQUIRED)

function(add_python_program) 

	cmake_parse_arguments(PT "" "NAME" "FILES;TEST" ${ARGN})

	set(ALL_FILES ${PT_FILES} ${PT_TEST})

	foreach (file ${ALL_FILES})
		add_custom_command(OUTPUT ${file}
			               COMMAND ${PYTHON_EXECUTABLE} ARGS -m py_compile ${CMAKE_CURRENT_SOURCE_DIR}/${file}
			               COMMAND ${PYTHON_EXECUTABLE} ARGS -m pep8 --show-source --max-line-length=120 ${CMAKE_CURRENT_SOURCE_DIR}/${FILE}
			               COMMAND cp ARGS ${CMAKE_CURRENT_SOURCE_DIR}/${file} ${CMAKE_CURRENT_BINARY_DIR}/${file}
			               DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${file})
		set(PT_DEPEND ${PT_DEPEND} "${file}")
	endforeach()

	foreach (test ${PT_TEST})
		add_test(${PT_NAME} ${PYTHON_EXECUTABLE} ${test} -v)
	endforeach()

	add_custom_target(${PT_NAME} ALL DEPENDS ${PT_DEPEND})
endfunction(add_python_program)