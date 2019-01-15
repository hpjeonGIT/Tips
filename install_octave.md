# install using gnu and netlib blas and lapack #
## lapack must be cleaned and compiled with -fPIC and liblapack.so is necessary
export LD_LIBRARY_PATH+=:/opt/libs/blas

./configure --prefix=/usr/nic/apps/octave/4.4.1 --with-blas="-L/usr/nic/libs/blas -lblas" --with-lapack=" -L/usr/nic/libs/lapack/lapack-3.8.0 -llapack" ;  make -j 32 ;    make check ;   make install

### For grahics, adjust PATH for gnuplot or fltk-config executable. When install fltk, -fPIC option is necessary for c/cxx compiler
export PATH+=:/opt/libs/fltk/3.4.2/bin/  
export PATH+=:/opt/compiler/llvm/4.0.1/bin # when JIT is required
./configure --enable-jit --prefix=/usr/nic/apps/octave/4.4.1 --with-blas="-L/usr/nic/libs/netlib/3.8.0/lib64/ -lblas" --with-lapack="-L/usr/nic/libs/netlib/3.8.0/lib64/ -llapack"


# using MKL may crash in matrix inversion #
## octave with MKL ##
### configure LD_LIBRARY with lib/intel64 and mkl/lib/intel645
export LD_LIBRARY_PATH+=:/opt/intel/18.0/mkl/lib/intel64:/opt/intel/18.0/lib/intel64

./configure  --prefix=/usr/nic/apps/octave/4.2.2  --with-blas="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread" --with-lapack="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread" --with-fftw3="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm" --with-fftw3f="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm"

make -j 32; make install

# Using intel compiler + MKL
###### ref: https://software.intel.com/en-us/articles/using-intel-mkl-in-gnu-octave
export CC=icc  
export CXX=icpc  
export F77=ifort  
export CFLAGS="-O3 -ipo -std=c99 -fPIC -DMKL_LP64"  
export MKLROOT=/usr/nic/compiler/intel/18.0/mkl  
export CPPFLAGS="-I$MKLROOT/include -I$MKLROOT/include/fftw"  
export LDFLAGS="-L$MKLROOT/lib/intel64 -L$MKLROOT/../compiler/lib/intel64"   
export LD_LIBRARY_PATH+=:$MKLROOT/lib/intel64:$MKLROOT/../compiler/lib/intel64:$LD_LIBRARY_PATH  
./configure --prefix=/usr/nic/apps/octave/4.4.1_intel18 --with-blas="-Wl,--start-group -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -Wl,--end-group -liomp5 -lpthread" --with-lapack="-Wl,--start-group -lmkl_intel_lp64 -lmkl_intel_thread -lmkl_core -Wl,--end-group -liomp5 -lpthread" --enable-fortran-calling-convention=gfortran  
- This seems working
### Another
export CFLAGS="-O2 -fPIC -DMKL_LP64 -DM_PI=3.1415926535897932384"
export FFLAGS="-O2 -fPIC"
export CPPFLAGS="-I$MKLROOT/include/ -I$MKLROOT/include/fftw/"
export LDFLAGS="-L$MKLROOT/lib/intel64 -L$MKLROOT/../lib/intel64"
#export LD_LIBRARY_PATH+=:$MKLROOT/lib/intel64:$MKLROOT/../compiler/lib/intel64:$LD_LIBRARY_PATH  
./configure --prefix=/usr/nic/apps/octave/4.4.1_intel18 --with-blas="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread" --with-lapack="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread" --with-fftw3="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm" --with-fftw3f="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm" --enable-fortran-calling-convention=gfortran
### Add --enable-fortran-calling-convention=gfortran in the end
