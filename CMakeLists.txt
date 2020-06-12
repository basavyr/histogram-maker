cmake_minimum_required(VERSION 3.0)

set(project_name "HISTOGRAM-MAKER")

set(py_dir "python-bindings")

project(${project_name})

SET(CMAKE_CXX_STANDARD 14)
SET(CMAKE_CXX_STANDARD_REQUIRED TRUE)

#this alows use to run the executables made after the `make install` command is executed by the user
set(CMAKE_MACOSX_RPATH 1)
# the RPATH to be used when installing
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")

add_subdirectory(src)
add_subdirectory(python)
add_subdirectory(tests)
