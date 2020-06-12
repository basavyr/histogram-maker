configure_file(histogram.py histogram.py COPYONLY)
configure_file(randoms.py randoms.py COPYONLY)

install(FILES histogram.py DESTINATION ${CMAKE_INSTALL_PREFIX}/${py_dir})
install(FILES randoms.py DESTINATION ${CMAKE_INSTALL_PREFIX}/${py_dir})
install(FILES test-bindings.py DESTINATION ${CMAKE_INSTALL_PREFIX}/${py_dir})

add_custom_target(py_script 
    COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/test-bindings.py ${CMAKE_CURRENT_BINARY_DIR}/test-bindings.py 
    DEPENDS test-bindings.py)

# add_custom_target(writeintofile 
#     COMMAND echo NAME >> ${CMAKE_CURRENT_BINARY_DIR}/copy_of_hist.py
#     DEPENDS py_script)

# add_custom_command(TARGET py_script POST_BUILD
#   COMMAND cp ${CMAKE_CURRENT_BINARY_DIR}/copy_of_hist.py ${CMAKE_INSTALL_PREFIX}/python/copy_of_hist.py
#   DEPENDS py_script
# )

# add_custom_command(
#   OUTPUT run_script
#   COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/histogram.py
# )

add_custom_target(run_python ALL
    DEPENDS  py_script )