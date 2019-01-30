## using intel and impi
../configure --prefix=/opt/libs/fftw/338_intel18 --enable-shared --enable-threads --enable-mpi --enable-single --enable-fortran --enable-static --enable-sse2 --enable-avx --enable-avx2 CC="icc" CPP="icc -E" F77="mpiifort" MPICC=mpiicc CFLAGS="-Ofast -xHost" CPPFLAGS="-Ofast -xHost" FFLAGS="-Ofast -xHost"

make -j 10; make all ; make install; make clean

../configure --prefix=/opt/libs/fftw/338_intel18 --enable-shared --enable-threads --enable-mpi --enable-fortran --enable-static --enable-sse2 --enable-avx --enable-avx2 CC="icc" CPP="icc -E" F77="mpiifort" MPICC=mpiicc CFLAGS="-Ofast -xHost" CPPFLAGS="-Ofast -xHost" FFLAGS="-Ofast -xHost"

make -j 10; make all ; make install; make clean

../configure --prefix=/opt/libs/fftw/338_intel18 --enable-shared --enable-threads --enable-mpi --enable-long-double --enable-fortran --enable-static --enable-sse2 --enable-avx --enable-avx2 CC="icc" CPP="icc -E" F77="mpiifort" MPICC=mpiicc CFLAGS="-Ofast -xHost" CPPFLAGS="-Ofast -xHost" FFLAGS="-Ofast -xHost"

make -j 10; make all ; make install; make clean

## using intel and impi + avx512
mkdir build
../configure --prefix=/opt/libs/fftw/338_intel19 --enable-shared --enable-threads --enable-mpi --enable-single --enable-fortran --enable-static --enable-sse2 --enable-avx --enable-avx2 --enable-avx512 CC="icc" CPP="icc -E" F77="mpiifort" MPICC=mpiicc CFLAGS="-Ofast -xHost" CPPFLAGS="-Ofast -xHost" FFLAGS="-Ofast -xHost"

make -j 10; make all ; make install; make clean

../configure --prefix=/opt/libs/fftw/338_intel19 --enable-shared --enable-threads --enable-mpi --enable-fortran --enable-static --enable-sse2 --enable-avx --enable-avx2 --enable-avx512 CC="icc" CPP="icc -E" F77="mpiifort" MPICC=mpiicc CFLAGS="-Ofast -xHost" CPPFLAGS="-Ofast -xHost" FFLAGS="-Ofast -xHost"

make -j 10; make all ; make install; make clean

../configure --prefix=/opt/libs/fftw/338_intel19 --enable-shared --enable-threads --enable-mpi --enable-long-double --enable-fortran --enable-static --enable-sse2 --enable-avx --enable-avx2 --enable-avx512 CC="icc" CPP="icc -E" F77="mpiifort" MPICC=mpiicc CFLAGS="-Ofast -xHost" CPPFLAGS="-Ofast -xHost" FFLAGS="-Ofast -xHost"

make -j 10; make all ; make install; make clean

# gcc with openmpi
mkdir build
../configure --prefix=/opt/libs/fftw/338_gcc48 --enable-shared --enable-threads --enable-mpi --enable-single --enable-fortran --enable-static --enable-sse2 --enable-avx --enable-avx2 --enable-avx512 CC="gcc" F77="mpifort" MPICC=mpicc CFLAGS="-Ofast -O3" CPPFLAGS="-Ofast -O3" FFLAGS="-Ofast -O3"
make -j 10; make all ; make install; make clean
## repeat without --enable-single or --enable-long-double
