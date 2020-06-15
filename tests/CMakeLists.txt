
add_executable(test_randoms test_randoms.cc)
target_include_directories(test_randoms PUBLIC ${CMAKE_SOURCE_DIR}/src)

# in order to get the pyhton header while building project
find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
target_link_libraries (test_randoms randoms)

install(TARGETS test_randoms RUNTIME DESTINATION bin)