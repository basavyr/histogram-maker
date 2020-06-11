configure_file(histogram.py histogram.py COPYONLY)
configure_file(randoms.py randoms.py COPYONLY)

install(FILES histogram.py DESTINATION ${CMAKE_INSTALL_PREFIX}/python)
install(FILES randoms.py DESTINATION ${CMAKE_INSTALL_PREFIX}/python)

add_custom_target(py_script 
    COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/histogram.py copy_of_hist.py 
DEPENDS histogram.py)

add_custom_command(TARGET py_script POST_BUILD
  COMMAND cp ${CMAKE_CURRENT_SOURCE_DIR}/histogram.py ${CMAKE_INSTALL_PREFIX}/python/copy_of_hist.py
  DEPENDS py_script
)

add_custom_command(
  OUTPUT run_script
  COMMAND python3 ${CMAKE_CURRENT_SOURCE_DIR}/histogram.py
  DEPENDS py_script
)

add_custom_target(run ALL
    DEPENDS  py_script run_script)