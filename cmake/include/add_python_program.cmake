include(CMakeParseArguments)

find_package(PythonInterp 3.1 REQUIRED)

function(add_python_program) 
	cmake_parse_arguments(PT "" "NAME" "FILES;TEST" ${ARGN})

	set(ALL_FILES ${PT_FILES} ${PT_TEST})

	foreach (file ${ALL_FILES})
		set (PY_COMPILE_FLAGS ${PYTHON_EXECUTABLE} -B -m py_compile "${CMAKE_CURRENT_SOURCE_DIR}/${file}" |& tee "${CMAKE_CURRENT_BINARY_DIR}/log/${file}.compile")
		add_custom_command(OUTPUT log/${file}.compile
			               COMMAND mkdir -p log
			               COMMAND bash ARGS -c '${PY_COMPILE_FLAGS}'
			               DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${file})
		
		set (PEP8_COMPILE_FLAGS ${PYTHON_EXECUTABLE} -B -m pep8 --show-source --max-line-length=120 "${CMAKE_CURRENT_SOURCE_DIR}/${FILE}" |& tee "${CMAKE_CURRENT_BINARY_DIR}/log/${file}.pep8")
		add_custom_command(OUTPUT log/${file}.pep8
		                   COMMAND mkdir -p log
		                   COMMAND bash ARGS -c '${PEP8_COMPILE_FLAGS}'
		                   DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${file})
		
		add_custom_command(OUTPUT ${file}
		                   COMMAND cp ARGS ${CMAKE_CURRENT_SOURCE_DIR}/${file} ${CMAKE_CURRENT_BINARY_DIR}/${file}
		                   DEPENDS log/${file}.pep8 log/${file}.compile)
		set(PT_DEPEND ${PT_DEPEND} "${file}")
	endforeach()

	foreach (test ${PT_TEST})
		add_test(${PT_NAME} ${PYTHON_EXECUTABLE} ${test} -v)
	endforeach()

	add_custom_target(${PT_NAME} ALL DEPENDS ${PT_DEPEND})
endfunction(add_python_program)
