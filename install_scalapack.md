## scalapack source install
- we need libblas.a and liblapack.a
- Download source from https://performance.netlib.org/lapack/
- setup using mkdir build; cd build; ccmake ..
  - disable shared lib. Install static only
  - add -fPIC into CFLAG and FFLAG
- make -j 40; make install
- Download source from http://www.netlib.org/scalapack/
- setup using mkdir build; cd buld;  ccmake ..
  - Use the location of libblas.a and liblapack.a
  - Use mpicc, mpif90 as necessary
- make -j 40; make install 

## for intel compiler, use intel mpi + mkl when available
