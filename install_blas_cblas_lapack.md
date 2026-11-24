# BLAS
- Download  blas.tgz from netlib : http://www.netlib.org/blas/blas-3.8.0.tgz
- cd BLAS
#### static
- gfortran -c -O3 *.f;  ar rv libblas.a *.o; sudo cp libblas.a /opt/somewhere
#### dynamic
- gfortran -shared -fPIC -O3 *.f -o libblas.so

# CBLAS
### download http://www.netlib.org/blas/blast-forum/cblas.tgz
### Edit Makefile.in # blas library is required
- make

# LAPACK
#### Download http://www.netlib.org/lapack/lapack-3.8.0.tar.gz
- cp make.inc.example make.inc; vi make.inc
#### Edit BLAS and CBLAS location
- make
## or use cmake 
- mkdir build ; cd build ; ccmake .. # enable shared library
- for CLI, use `-DLAPACKE=ON` to have lapacke.h 
- make -j 32; make install

# scalapack
- Requires blas/lapack. use netlib as shown above
- mkdir build; cd build; ccmake ..
- Enable shared library (static will not be made)
- Or enable static library then *.so is not made
- make -j 20

# External project in cmake
```cmake
IF(CMAKE_CXX_COMPILER_VERSION VERSION_GREATER 10.0 AND CMAKE_CXX_COMPILER_ID MATCHES "GNU")
  set(FOPTFLAGS "${CMAKE_Fortran_FLAGS} -O3 -w -fallow-argument-mismatch")
ELSE()
  set(FOPTFLAGS "${CMAKE_Fortran_FLAGS} -O3")
ENDIF()
include(ExternalProject)
ExternalProject_Add(
  LAPACK_PROJECT
  SOURCE_DIR ...
  URL ...
  CMAKE_ARGS
    -DCMAKE_INSTALL_PREFIX=...
    -DCMAKE_C_COMPILER=${CMAKE_C_COMPILER}
    -DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER}
    -DCMake_Fortran_COMPILER=${CMAKE_Fortran_COMPILER}
    -DCMAKE_BUILD_TYPE=Release
    ...
    -DCMAKE_INSTALL_LIBDIR=lib # prevent to install at lib64
    -DCBLAS=ON
    -DLAPACKE=ON
  BUILD_IN_SOURCE=0
  BUILD_COMMAND make -j 10
  BINARY_DIR ${LAPACK_BUILD_PATH}
  INSTALL_DIR "${LAPACK_INSTALL_PATH}
)
```
- `-llapacke -llapack -lcblas -lbas` may need libgfortran. To extract the info of such library:
```cmake
execute_process(COMMAND ${CMAKE_Fortran_COMPILER} --print-file-name=libgfortran.a
  OUTPUT_VARIABLE LIBGFORTRAN_PATH
  OUTPUT_STRIP_TRAILING_WHITESPACE
  RESULT_VARIABLE RESULT)
SET(mylapack ${LAPACK_INSTALL_PATH}/lib/liblapacke.a ... ${LIBGFORTRAN_PATH})
```
