# download source code
- mpich is installed from the network
- gcc7.4 is not the system default compiler
- 40 cpus are used for compilation  
<del>./install.sh --num-threads 40 --install-prefix /share/compiler/openCAF/2.4.0_gcc74 \
--with-cxx /share/compiler/gcc/7.4.0/bin/g++ --with-fortran /share/compiler/gcc/7.4.0/bin/gfortran \
--with-c /share/compiler/gcc/7.4.0/bin/gcc --with-cmake /share/apps/cmake/3.13.3/bin/cmake --package mpich </del>
- use cmake
  - mkdir build ; cd build ; ccmake ..; make -j 40; make all; make install
