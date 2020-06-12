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
    COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/setup.py build --build-base=${python_bindings_dir})

add_custom_target(run_build ALL
    DEPENDS build_bindings)

install(TARGETS randoms LIBRARY DESTINATION lib)
# install(FILES randoms.cc randoms.hh setup.py DESTINATION ${CMAKE_INSTALL_PREFIX}/py_dir)
install(FILES ${python_bindings_dir} DESTINATION ${CMAKE_INSTALL_PREFIX}/ )
install(CODE "execute_process(COMMAND pwd)")

# add_custom_command(OUTPUT build_extension POST_BUILD
#   COMMAND pwd
#   DEPENDS setup.py
# )

add_custom_target(run_extension ALL
    DEPENDS copy_sources  run_build)