## Install SuiteSparse
export MKLROOT=/opt/compiler/intel/18.0/mkl; 
### Edit SuiteSparse_config/SuiteSparse_config.mk for the location of MKL library
Line 160: BLAS = -L$(MKLROOT)/lib/intel64 -lmkl_intel_lp64 -lmkl_core -lmkl_intel_t    hread -lpthread -lm
### 5.20. requires gcc>4.9 and corresponding cmake
make install INSTALL=/opt/libs/suitesparse/4.5.6

## SuperLU_MT
cp MAKE_INC/make.linux.openmp make.inc; make blaslib; make

## Install eig3
http://bitbucket.org/eigen/eigen/get/3.3.4.tar.gz

cd build; cmake -DCMAKE_INSTALL_PREFIX=/opt/libs/eigen/3.3.4  -DBoost_LIBRARY_DIR=/opt/libs/boost/1.54.0/lib -DBoost_INCLUDE_DIR=/opt/libs/boost/1.54.0/include -DCHOLMOD_INCLUDES=/opt/libs/suitesparse/4.5.6/include -DCHOLMOD_LIBRARIES=/opt/libs/suitesparse/4.5.6/lib/ libcholmod.so -DUMFPACK_INCLUDES=/opt/libs/suitesparse/4.5.6/include -DUMFPACK_LIBRARIES=/opt/libs/suitesparse/4.5.6/lib/ libumfpack.so  -DSPQR_INCLUDES=/opt/libs/suitesparse/4.5.6/include -DSPQR_LIBRARIES=/opt/libs/suitesparse/4.5.6/lib/ libspqr.so  -DSUPERLU_INCLUDES=/opt/libs/SuperLU/5.2.1/include -DSUPERLU_LIBRARIES=/opt/libs/SuperLU/5.2.1/lib64/libsuperlu.a -DBoost_NO_BOOST_CMAKE=BOOL:ON  ..

