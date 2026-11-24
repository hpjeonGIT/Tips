# Default SMP configuration
./boostrap.sh  
./b2 install --prefix=/opt/lib/boost/x.xx threading=multi --layout=tagged  -j32 --with-python # needs python environment in LD_LIBRARY_PATH

## add python
using python
  : 3.6
  : /usr/nic/apps/python_da/3.6.6/bin/python3
  : /usr/nic/apps/python_da/3.6.6/include/python3.6m
  : /usr/nic/apps/python_da/3.6.6/lib
 ;
### If /lstr/applications/focus_v7/libs/boost/1.68.0_gcc485/lib/libboost_python36-mt.so exists, libboost_python search in cmake may fail.
### Then edit CMakeLists.txt, COMPONENTS python-py34 => COMPONENTS python36-mt

# Using MPI
- Ref: https://www.boost.org/doc/libs/1_61_0/doc/html/mpi/getting_started.html
- After running boostrap.sh, add "
using mpi
   : /share/ompi/4.0.0/bin/mpicxx ;
" into project-config.jam

## Nitty Gritty
- For boost 1.61, the combo of gcc/5.3 + mvapich/2.3 might not work - produces ompi_mpi* library, which cannot be used
- For boost 1.61, the combo of gcc/5.3 + openmpi/4.1.0 didn't work - libboost_mpi was not made. Use openmpi/2.0.0

## When installing as external project in cmake
- When coupling with MPI, `using mpi ${CMAKE_CXX_COMPILER} ;` must be injected into project-config.jam after bootstrap. However, we cannot inject `;` in the middle of cmake. Therefore, we prepare pre_defined.jam in advance, then copy it to project-config.jam
```cmake
ExternalProject_Add(
  BOOST_PROJECT
 CONFIGURE_COMMAND ${boost_src_dir}/bootstrap.sh --with-libraries=mpi,serial && cp {CMAKE_SOURCE_DIR}/BACKUP/pre_defined.jam ${boost_src_dir}/project-config.jam && sed -i "s@REPLACE_COMPILER@${CMAKE_CXX_COMPILER}@" ${boost_src_dir}/project-config.jam
  SOURCE_DIR .../boost_1_61_0
  URL .../boost_1_61_0.tar.gz
  BUILD_IN_SOURCE 1
  BUILD_COMMAND ${boost_src_dir}/b2 install --prefix=${BOOST_INSTALL_PATH} --layout=tagged -j20
  INSTALL_DIR "${BOOST_INSTALL_PATH}"
  INSTALL_COMMAND ""
  BUILD_BYPRODUCTS ${BOOST_INSTALL_PATH}/lib/libboost_mpi-mt.a ${BOOST_INSTALL_PATH}/lib/libboost_serialization-mt.a
)
```
- For pre_defined.jam, `using mpi: mpicxx ;` would be appended in the bottom. For cray environment, use follwoing:
```
using mpi : CC
  : <include>/opt/cray/pe/mpich/..../gnu/x.x/include
    <library-path>/opt/cray/pe/mpich/..../ofi/gnu/x.x/lib
    <find-shared-library>mpich
    ;
```
