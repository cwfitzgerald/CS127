@RUN_CLANG_TIDY_EXE@ '-header-filter=^@CMAKE_SOURCE_DIR@/@DIR_TO_LINT_STR@.*' -checks=*,-clang-analyzer-alpha.*,-clang-diagnostic-unknown-warning-option*,-clang-diagnostic-unknown-warning-option*,-clang-diagnostic-unused-command-line-argument,-llvm-header-guard -quiet @FILES_TO_LINT_STR@