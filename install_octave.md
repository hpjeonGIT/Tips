# install using gnu and netlib blas and lapack #
## lapack must be cleaned and compiled with -fPIC and liblapack.so is necessary
export LD_LIBRARY_PATH+=:/opt/libs/blas

./configure --prefix=/usr/nic/apps/octave/4.4.1 --with-blas="-L/usr/nic/libs/blas -lblas" --with-lapack=" -L/usr/nic/libs/lapack/lapack-3.8.0 -llapack" ;  make -j 32 ;    make check ;   make install



# using MKL will crash in matrix inversion #
## octave with MKL ##
### configure LD_LIBRARY with lib/intel64 and mkl/lib/intel645
export LD_LIBRARY_PATH+=:/opt/intel/18.0/mkl/lib/intel64:/opt/intel/18.0/lib/intel64

./configure  --prefix=/usr/nic/apps/octave/4.2.2  --with-blas="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread" --with-lapack="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread" --with-fftw3="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm" --with-fftw3f="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm"

make -j 32; make install
