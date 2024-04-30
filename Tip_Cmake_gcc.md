## building shared libs
- CMAKE_SHARED_LINKER_FLAGS="-Wl,-Bsymbolic" when links are messed up

## enforcing $PREFIX/lib64
- Ubuntu may make $PREFIX/lib
- CMAKE_INSTALL_LIBDIR:PATH=lib64

## local/global text symbol
- or just local/global symbol
- For library files like
```
$ nm libvtkCommonDataModel-9.1.so
.... T _Zn17vtkXMLData ...
.... U _Z.....
.... t _Z....
```
- T means global symbol
- U means undefined (wouldbe defined in other library file)
- t means local symbol

## compiling VTK with -DModule_vktCommonCore=ON -DModule_vtkCommonDataModel=ON
- gcc8.4 yields library with T, global symbol but gcc10.3 yielded with t, local
- Now linker with other source code yields undefined reference message
- How to enforce T, not t, in the library?
  - In Cmake files, add_library(someLib SHARED IMPORTED GLOBAL) will enforce global symbol -> but not working?
  - Comparing CMakeCache.txt by gcc8.4 vs 10.3, COMPILER_HAS_DEPRECATED:INTERNAL=1 is found at gcc8.4. 10.3 has no value.
  - ~~Needs newer version of cmake? This is 3.20.5
  - Tried vtk 9.1 and worked OK. But this will need the higher version of CMake (> 3.12)

## setting system variable within cmake
- In ExternalProject_Add ()
  - `CONFIGURE_COMMAND ${CMAKE_COMMAND} -E env TMPDIR=/tmp mkdir myfolder && cmake --prefix=/opt/myapps`

## intel2021 + mvapich2 on AMD cpu
- Hangs at FindMPI()
  - Check through cmake --trace-expand
  - ROI: execute_process(mpicxx -showme:compile ...)
- Intel cpu seems OK
- Found at 3.11, 3.28, 3.29, ...
- Alternative solution
  - Instead of mpicxx, use icpc and provide -DCMAKE_CXX_FLAGS="..."
  - The contents can be found from `mpicxx -show`
  - Might not work on building external projects
