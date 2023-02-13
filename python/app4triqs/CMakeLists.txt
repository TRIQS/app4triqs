# Configure the version
configure_file(version.py.in version.py)

# ------- Python files ----------

# Copy them in the build dir to have a complete package for the tests.
file(GLOB_RECURSE python_sources RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} *.py)
foreach(file ${python_sources})
 configure_file(${file} ${file} COPYONLY)
endforeach()

# Install python files to proper location
set(PYTHON_LIB_DEST ${TRIQS_PYTHON_LIB_DEST_ROOT}/${PROJECT_NAME})
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/version.py DESTINATION ${PYTHON_LIB_DEST})
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR} DESTINATION ${TRIQS_PYTHON_LIB_DEST_ROOT} FILES_MATCHING PATTERN "*.py")

# ------- Python Extension ----------

# Find python
find_package(Python COMPONENTS Interpreter Development NumPy)

# Get c2py
include(FetchContent)
FetchContent_Declare(
  c2py
  GIT_REPOSITORY https://github.com/flatironinstitute/c2py
  GIT_TAG        unstable 
  EXCLUDE_FROM_ALL
)
FetchContent_MakeAvailable(c2py)

# 
option(GENERATE_PYTHON_BINDINGS "Use Clair python bindings generators" OFF)
if (GENERATE_PYTHON_BINDINGS)
  find_package(Clair REQUIRED)
endif()

set(module_name app4triqs_module)

Python_add_library(${module_name} MODULE ${module_name}.$<IF:$<BOOL:${GENERATE_PYTHON_BINDINGS}>,cpp,wrap.cxx>)

target_include_directories(${module_name} SYSTEM PRIVATE ${CMAKE_SOURCE_DIR}/src ${CMAKE_CURRENT_SOURCE_DIR})
target_link_libraries(${module_name}             PRIVATE ${PROJECT_NAME}_c c2py::c2py $<$<BOOL:${GENERATE_PYTHON_BINDINGS}>:clair::c2py_plugin> triqs_py)
target_link_libraries(${module_name}             PRIVATE $<$<BOOL:${ASAN}>:$<BUILD_INTERFACE:asan>> $<$<BOOL:${UBSAN}>:$<BUILD_INTERFACE:ubsan>> )

# Alias
add_library(${PROJECT_NAME}::${module_name} ALIAS ${module_name})

# Installation
install(TARGETS ${module_name} DESTINATION ${PYTHON_LIB_DEST}/${module_dir})

if(ASAN)
  target_link_libraries(${module_name}  PRIVATE $<BUILD_INTERFACE:asan>)
endif()

if(UBSAN)
  target_link_libraries(${module_name}  PRIVATE $<BUILD_INTERFACE:ubsan>)
endif()

#--------------------------------------------------------
#  Developer only
#  A target to copy the wrap.cxx files back to the src
#--------------------------------------------------------

# FIXME : make it a developer macro in clair ??
# 
if (GENERATE_PYTHON_BINDINGS)

 add_custom_target(clair_copy_bindings_to_src_dir)
 add_custom_command(
  TARGET clair_copy_bindings_to_src_dir
  COMMAND cp ${CMAKE_CURRENT_BINARY_DIR}/*.wrap.cxx     ${CMAKE_CURRENT_SOURCE_DIR}
  COMMAND cp ${CMAKE_CURRENT_BINARY_DIR}/*.wrap.hxx     ${CMAKE_SOURCE_DIR}/c++/${PROJECT_NAME} # the hxx file has to be includable as c++ source.
  COMMAND cp ${CMAKE_BINARY_DIR}/test/python/*.wrap.?xx ${CMAKE_SOURCE_DIR}/test/python
)

endif()
