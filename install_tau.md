## TAU at ROCKY OS
- Download tau/pdt source code

## Using TAU only
- At tau source code, configure -prefix=/opt/tau/2.34 -c++=mpicxx -cc=mpicc -mpi -openmp; make install
- But this may yield UNRESOLVED UNKNOWN for function name at postprocessing of profiling results
- Will need bintuils with -bfd options
- Install binutils with configure command of ./configure --prefix=/opt/bintuils/2.40 --enable=shared --enable-6t4-bit-bfd --enalbe-install-libiberty ...
  - Check configure script to check which version of binutils is supported  
  - Details are at apex/cmake/Modules/FindBFD.cmake
  - make -j 20; make install
  - Make sure that libiberty.a is installed 
- Install libunwind: autoconf -i; configure --prefix=/opt/libunwind/1.6.2 ; make -j 10; make install
- Install papi: cd src; configure --prefix=/opt/papi; make -j 10; make instal
- Then configure tau as  configure -prefix=/opt/tau/2.34 -bfd=/opt/bin/utils/2.40 -unwind=/opt/libunwind/1.6.2 -papi=/opt/papi/ -c++=mpicxx -cc=mpicc -mpi -openmp; make install

## TAU + PDT
- Install PDT first. MPI not required
- At tau, configure -prefix=/opt/tau/2.34 -bfd=/opt/bin/utils/2.43 -unwind=/opt/libunwind/1.6.2 -papi=/opt/papi -pdt=/opt/pdt/ -c++=mpicxx -cc=mpicc -mpi -openmp; make install
- PDT may be deprecated. See SALT coupling

## TAU with cmake
- cmake may not work well due to instrument optimzation
  - export TAU_OPTIONS=-optDisable
  - configure
  - export TAU_OPTIONS=-optCompInst
  - make -j 40
