## RHEL7/CENTOS7
- tbb libraries from yum
- upack src
- mkdir build; cd build
- configure LD_LIBRARY_PATH with mkl or netlib lapack
- ccmake ..
  - configure CMAKE_INSTALL_PREFIX
  - disable gsl
  - When lapack libraries are detected, umfpack and lapack would be ON
- make -j 22; make install

## RHEL6/CENTOS6
- TBB libraries need to be built from src
- Or use pre-built from Intel package
- Disable gsl. Enable umfpack, lapack. Confirm MKL libraries are detected in the INTEL library. Or setup lapack LD_LIBRARY_PATH
- DO NOT use bundled TBB libraries
- Find TBB from Intel suite: TBB_LIBRARY /opt/intel/2018.1/tbb/lib/intel64/gcc4.7/libtbb.so
- Match include folder, debug library (libtbb_debug.so)
- Check detailed.log after makefile is produced
```
TBB_DEBUG_LIBRARY:FILEPATH=/opt/intel/2018.1/tbb/lib/intel64/gcc4.7/libtbb_debug.so
TBB_DIR:PATH=/opt/intel/2018.1/tbb
TBB_INCLUDE_DIR:PATH=/opt/intel/2018.1/tbb/include
TBB_LIBRARY:FILEPATH=/opt/intel/2018.1/tbb/lib/intel64/gcc4.7/libtbb.so
TBB_DEBUG_LIBRARY-ADVANCED:INTERNAL=1
TBB_DEBUG_LIBRARY-MODIFIED:INTERNAL=ON
TBB_DIR-ADVANCED:INTERNAL=1
TBB_DIR-MODIFIED:INTERNAL=ON
TBB_INCLUDE_DIR-ADVANCED:INTERNAL=1
TBB_LIBRARY-ADVANCED:INTERNAL=1
TBB_LIBRARY-MODIFIED:INTERNAL=ON
```
- Even though pre-built library is for gcc4.7, it works with gcc/5.3 as well
- make -j 10
- make install

## With trilinos
- Trilinos installatin for deal.ii
  - Ref: https://www.dealii.org/current/external-libs/trilinos.html
  - untar source; make build ;cd build ; ccmake ..
  - Enable BUILD_SHARED_LIBS, TPL_ENABLE_Infiniband, TPL_ENABLE_BLAS, TPL_ENABLE_LAPACK
  - BLAS_LIBRARY_DIRS=/opt/intel/2019.1/mkl/lib/intel64
  - BLAS_LIBRARY_NAMES=mkl_intel_lp64;mkl_intel_thread;mkl_core;iomp5
  - TPL_BLAS_LIBRARIES=/opt/intel/2019.1/mkl/lib/intel64/libmkl_intel_lp64.so;/opt/intel/2019.1/mkl/lib/intel64/libmkl_intel_thread.so;/opt/intel/2019.1/mkl/lib/intel64/libmkl_core.so;/opt/intel/2019.1/lib/intel64/libiomp5.so
  - Same for LAPACK wise
  - TPL_InfiniBand_INCLUDE_DIRS=/usr/include/infiniband
  - TPL_InfiniBand_LIBRARIES=/usr/lib64/libibverbs.so
  - Enable Amesos, AztecOO, Epetra, EpetraExt, Ifpack, MueLu, ML, Sacao, ROL, Teuchos, Tpetra
  - produce make file then make -j 20 ; make install
- P4est with --enable-shared
  - P4est 2.2 for deal.ii 9.*
  - P4est 0.3.4.2 for deal.ii 8.*
- deal.ii
  - untar source; make build ;cd build ; ccmake ..
  - P4EST_DIR=/opt/p4est/0.3.4.2/
  - P4EST_INCLUDE_DIR=/opt/p4est/0.3.4.2/include
  - P4EST_LIBRARY_OPTIMIZED=/opt/p4est/0.3.4.2/lib/libp4est.so
  - SC_INCLUDE_DIR=/opt/p4est/0.3.4.2/include
  - SC_LIBRARY_OPTIMIZED=/opt/p4est/0.3.4.2/lib/libsc.so
  - TBB_DEBUG_LIBRARY:FILEPATH=/opt/intel/2018.1/tbb/lib/intel64/gcc4.7/libtbb_debug.so
  - TBB_DIR:PATH=/opt/intel/2018.1/tbb
  - TBB_INCLUDE_DIR:PATH=/opt/intel/2018.1/tbb/include
  - TBB_LIBRARY:FILEPATH=/opt/intel/2018.1/tbb/lib/intel64/gcc4.7/libtbb.so
  - produce make file then make -j 20 ; make install
  - Parallel building deal.ii will require large memory (> 40GB with -j16)
