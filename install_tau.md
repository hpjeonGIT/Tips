## TAU at ROCKY OS
- Download tau/pdt source code

## Using TAU only
- At tau source code, configure -prefix=/opt/tau/2.34 -c++=mpicxx -cc=mpicc -mpi -openmp; make install
- But this may yield UNRESOLVED UNKNOWN for function name at postprocessing of profiling results
- Will need bintuils with -bfd options
- Install binutils with configure command of ./configure --prefix=/opt/bintuils/2.42 --enable=shared --enable-6t4-bit-bfd --enalbe-install-libiberty ...
  - Check configure script to check which version of binutils is supported
    - but apex/cmake/Modules/FindBFD.cmake downloads 2.42 (Feb 2025)
  - Details are at apex/cmake/Modules/FindBFD.cmake
  - make -j 20; make install
  - Make sure that libiberty.a is installed
  - cd /opt/binutils/2.42/include; ln -s libiberty ./extra # include/libiberty is not searched from TAU for demangle.sh
- Install libunwind: autoconf -i; configure --prefix=/opt/libunwind/1.6.2 ; make -j 10; make install
- Install papi: cd src; configure --prefix=/opt/papi; make -j 10; make instal
- Then configure tau as  configure -prefix=/opt/tau/2.34 -bfd=/opt/bin/utils/2.40 -unwind=/opt/libunwind/1.6.2 -papi=/opt/papi/ -c++=mpicxx -cc=mpicc -mpi -openmp; make install
- For environmental variables
  - TAU_VERBOSE=1
  - TAU_OPTIONS=-optCompInst
  - TAU_SAMPLING=1
  - TAU_CALLPATH=1
  - TAU_CALLPATH_DEPTH=100
  - TAU_METRICS=TIME,PAPI_L1_DCM
  - TAU_MAKEFILE=..../Makefile.tau-papi-mpi-openmp

## TAU + PDT
- Install PDT first. MPI not required
- At tau, configure -prefix=/opt/tau/2.34 -bfd=/opt/bin/utils/2.43 -unwind=/opt/libunwind/1.6.2 -papi=/opt/papi -pdt=/opt/pdt/ -c++=mpicxx -cc=mpicc -mpi -openmp; make install
- support for C++ may not work well
- PDT may be deprecated. See SALT coupling

## TAU with cmake
- cmake may not work well due to instrument optimzation
  - Edit configure script with tau_cc.sh and tau_cxx.sh
  - export TAU_OPTIONS=-optDisable
  - configure; # TAU will pass through, not disrupting the source code/cmake
  - export TAU_OPTIONS=-optCompInst
  - make -j 40
