cmake_minimum_required(VERSION 3.0)

set(project_name "HISTOGRAM-MAKER")

set(py_dir "python-bindings")

set(pkgs "${CMAKE_SOURCE_DIR}/packages.json")

project(${project_name})

SET(CMAKE_CXX_STANDARD 14)
SET(CMAKE_CXX_STANDARD_REQUIRED TRUE)

#this alows use to run the executables made after the `make install` command is executed by the user
set(CMAKE_MACOSX_RPATH 1)
# the RPATH to be used when installing
set(CMAKE_INSTALL_RPATH "${CMAKE_INSTALL_PREFIX}/lib")

# use, i.e. don't skip the full RPATH for the build tree
set(CMAKE_SKIP_BUILD_RPATH FALSE)

# when building, don't use the install RPATH already
# (but later on when installing)
set(CMAKE_BUILD_WITH_INSTALL_RPATH FALSE)

# add the automatically determined parts of the RPATH
# which point to directories outside the build tree to the install RPATH
set(CMAKE_INSTALL_RPATH_USE_LINK_PATH TRUE)

#installs the missing packages on the platform
find_package(PythonInterp REQUIRED)
add_custom_target(py_packages 
    COMMAND pip install -r ${pkgs})
add_custom_target(install_packages ALL
    DEPENDS  py_packages )

add_subdirectory(src)
add_subdirectory(python)
add_subdirectory(tests)