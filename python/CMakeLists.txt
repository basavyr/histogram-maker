configure_file(histogram.py histogram.py COPYONLY)
configure_file(randoms.py randoms.py COPYONLY)

# install(FILES histogram.py DESTINATION ${CMAKE_INSTALL_PREFIX}/${py_dir})
# install(FILES randoms.py DESTINATION ${CMAKE_INSTALL_PREFIX}/${py_dir})

# add_custom_target(py_random_script 
#     COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/randoms.py ${CMAKE_CURRENT_BINARY_DIR}/randoms.py 
#     DEPENDS randoms.py)

# add_custom_target(py_random_script2 
#     COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/randoms.py ${CMAKE_INSTALL_PREFIX}/python-bindings/randoms.py 
#     DEPENDS py_random_script)

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

# add_custom_target(run_python ALL
#     DEPENDS  py_random_script )