find_program(
	RUN_CLANG_TIDY_EXE
	NAMES "run-clang-tidy" "run-clang-tidy.py"
	DOC "Path to run-clang-tidy executable")
if(NOT RUN_CLANG_TIDY_EXE)
	message(STATUS "run-clang-tidy not found.")
else()
	message(STATUS "run-clang-tidy found: ${RUN_CLANG_TIDY_EXE}")
	set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
endif()

function(lint) 
	cmake_parse_arguments(LT "" "" "FILES" ${ARGN})

	foreach(file ${LT_FILES})
		set(FILES_TO_LINT ${FILES_TO_LINT} ${CMAKE_CURRENT_SOURCE_DIR}/${file} CACHE INTERNAL "FILES_TO_LINT" FORCE)
	endforeach()
endfunction(lint)

function(add_linted_subdirectory)
	set(DIRECTORIES_TO_LINT ${DIRECTORIES_TO_LINT} ${ARGN} CACHE INTERNAL "DIRECTORIES_TO_LINT" FORCE)
	add_subdirectory(${ARGN})
endfunction(add_linted_subdirectory)

function(configure_linter)
	list(REMOVE_DUPLICATES FILES_TO_LINT)
	list(REMOVE_DUPLICATES DIRECTORIES_TO_LINT)

	foreach(file ${FILES_TO_LINT})
		set(FILES_TO_LINT_STR "${FILES_TO_LINT_STR} \"${file}\"")
	endforeach()

	foreach(dir ${DIRECTORIES_TO_LINT})
		if(DIR_TO_LINT_STR)
			set(DIR_TO_LINT_STR "${DIR_TO_LINT_STR}|${dir}")
		else()
			set(DIR_TO_LINT_STR "${dir}")
		endif()
	endforeach()
	set(DIR_TO_LINT_STR "(${DIR_TO_LINT_STR})")

	configure_file(${CMAKE_SOURCE_DIR}/lint.sh lint.sh @ONLY)
	execute_process(COMMAND chmod +x ${CMAKE_BINARY_DIR}/lint.sh)

	set(FILES_TO_LINT ${FILES_TO_LINT} CACHE INTERNAL "FILES_TO_LINT" FORCE)
	set(DIRECTORIES_TO_LINT ${DIRECTORIES_TO_LINT} CACHE INTERNAL "DIRECTORIES_TO_LINT" FORCE)
endfunction(configure_linter)
