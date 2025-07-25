# We use CPM for smaller dependencies, c.f. https://github.com/cpm-cmake/CPM.cmake
include(get_cpm.cmake)

# -- Cpp2Py --
if(PythonSupport OR (NOT IS_SUBPROJECT AND Build_Documentation))
  CPMAddPackage("gh:TRIQS/cpp2py#main")
endif()

# -- GTest --
CPMAddPackage("gh:google/googletest#main")
