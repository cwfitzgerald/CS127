include(CMakeParseArguments)

function(add_python_program) 
	cmake_parse_arguments(PT "" "NAME" "FILES" ${ARGN})

	foreach (file ${PT_FILES})
		add_custom_command(OUTPUT ${file}
			               COMMAND cp ARGS ${CMAKE_CURRENT_SOURCE_DIR}/${file} ${CMAKE_CURRENT_BINARY_DIR}/${file}
			               DEPENDS ${CMAKE_CURRENT_SOURCE_DIR}/${file})
		set(PT_DEPEND ${PT_DEPEND} "${file}")
	endforeach()

	add_custom_target(${PT_NAME} ALL DEPENDS ${PT_DEPEND})
endfunction(add_python_program)