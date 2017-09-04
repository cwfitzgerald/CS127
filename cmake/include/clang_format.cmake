include(CMakeParseArguments)

add_custom_target(format)

function(format)
	cmake_parse_arguments(CF "" "" "FILES" ${ARGN})

	foreach(file ${CF_FILES})
		string(REPLACE "/" "__" CURRENT_SUBTARGET ${file})
		set(CF_SUBTARGETS ${CF_SUBTARGETS} format_subtarget_${CURRENT_SUBTARGET})
		add_custom_target(format_subtarget_${CURRENT_SUBTARGET} 
		                  COMMAND clang-format -i -style=file ${CMAKE_CURRENT_SOURCE_DIR}/${file})
	endforeach()
	add_dependencies(format ${CF_SUBTARGETS})
endfunction(format)