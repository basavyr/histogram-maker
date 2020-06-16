set(python_bindings_dir "${CMAKE_BINARY_DIR}/python-bindings")
add_custom_target(copy_sources
    COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/setup.py ${CMAKE_CURRENT_BINARY_DIR}/setup.py 
    COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/randoms.cc ${CMAKE_CURRENT_BINARY_DIR}/randoms.cc
    COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/randoms.hh ${CMAKE_CURRENT_BINARY_DIR}/randoms.hh
    DEPENDS setup.py)

# add_custom_target(runpython_from_build
# COMMAND python3 ${CMAKE_CURRENT_BINARY_DIR}/copy_of_setup.py
# DEPENDS copy_build
# )

add_custom_target(run_src ALL
    DEPENDS  copy_sources)

add_library(randoms SHARED randoms.cc randoms.hh)
target_include_directories(randoms PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
target_link_libraries(randoms ${PYTHON_LIBRARIES})

find_package(PythonInterp REQUIRED)
add_custom_command(OUTPUT build_bindings
    COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/setup.py build --build-base=${python_bindings_dir}
    DEPENDS copy_sources) # this needs to depend on the copy process of the python script and the C++ source files otherwise it can fail on make & make install 

add_custom_command(OUTPUT copy_scripts
    COMMAND cp ${CMAKE_SOURCE_DIR}/python/randoms.py ${python_bindings_dir}/lib*
    COMMAND cp ${CMAKE_SOURCE_DIR}/python/histogram.py ${python_bindings_dir}/lib*
    DEPENDS build_bindings
  )# copies the test scripts into lib dir after install
  #once the python scripts which are based on the random module are inside the lib folder, they can be executed without issue
add_custom_command(OUTPUT plot_storage
    COMMAND mkdir -p ${python_bindings_dir}/output
    DEPENDS copy_scripts
  )# creates output directory for python plot storage

install(TARGETS randoms LIBRARY DESTINATION lib)
install(DIRECTORY ${python_bindings_dir} DESTINATION ${CMAKE_INSTALL_PREFIX}/)

# install(FILES randoms.cc randoms.hh setup.py DESTINATION ${CMAKE_INSTALL_PREFIX}/py_dir)
# install(FILES ${python_bindings_dir} DESTINATION ${CMAKE_INSTALL_PREFIX}/ )
# install(FILES ${python_bindings_dir} DESTINATION ${CMAKE_INSTALL_PREFIX}/new-folder )

add_custom_target(run_extension ALL
    DEPENDS copy_sources  build_bindings copy_scripts plot_storage)