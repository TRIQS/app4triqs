# Copy h5 files to binary dir
file(GLOB_RECURSE all_h5_ref_files RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.ref.h5)
foreach(file ${all_h5_ref_files})
  configure_file(${file} ${file} COPYONLY)
endforeach()

add_test(NAME pytest
  COMMAND ${TRIQS_PYTHON_EXECUTABLE} -m pytest -v ${CMAKE_CURRENT_SOURCE_DIR}
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
)
set_property(TEST pytest APPEND PROPERTY ENVIRONMENT_MODIFICATION
  "PYTHONPATH=path_list_prepend:${PROJECT_BINARY_DIR}/python")
set_property(TEST pytest APPEND PROPERTY ENVIRONMENT ${SANITIZER_RT_PRELOAD})
