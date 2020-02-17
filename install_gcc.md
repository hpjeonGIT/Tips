# install gmp, mpic, mpfr first
## gmp
- ./configure --prefix=/opt/gmp6
## mpfr
- ./configure --prefix=/opt/mpfr312 --with-gmp=/opt/gmp6
## mpc
- ./configure --prefix=/opt/mpc102 --with-gmp=/opt/gmp6 --with-mpfr=/opt/mpfr312
- make -j 20; make install

# gcc8.2 using gcc4.8 #
- mkdir build ; cd build
- ../configure --prefix=/opt/compiler/gcc/8.2 --enable-languages=c,c++,fortran --with-gmp=/opt/libs/gmp/6.1.2/ --with-mpc=/opt/libs/mpc/1.1.0 --with-mpfr=/opt/libs/mpfr/4.0.1 --disable-multilib
- 32bit support is disabled
- lib of mpfr is needed in LD_LIBRARY_PATH

# trouble-shooting
- When `configure: error: error verifying int64_t uses long long` message appears
  - The system doesn't have g++ compiler
- When `configure: error: cannot compute suffix of object files: cannot compile' appers
  - Update LD_LIBRARY_PATH with libs of mpfr, gmp, mpc
