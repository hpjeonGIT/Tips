## octave with MKL ##
### configure LD_LIBRARY with lib/intel64 and mkl/lib/intel645
export LD_LIBRARY_PATH+=:/opt/intel/18.0/mkl/lib/intel64:/opt/intel/18.0/lib/intel64

./configure  --prefix=/usr/nic/apps/octave/4.2.2  --with-blas="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread" --with-lapack="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread" --with-fftw3="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm" --with-fftw3f="-lmkl_gf_lp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm"

make -j 32; make install
