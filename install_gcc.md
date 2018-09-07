# gcc8.2 using gcc4.8 #
## install gmp, mpic, mpfr first
mkdir build ; cd build
../configure --prefix=/opt/compiler/gcc/8.2 --enable-languages=c,c++,fortran --with-gmp=/opt/libs/gmp/6.1.2/ --with-mpc=/opt/libs/mpc/1.1.0 --with-mpfr=/opt/libs/mpfr/4.0.1 --disable-multilib
- 32bit support is disabled
- lib of mpfr is needed in LD_LIBRARY_PATH
