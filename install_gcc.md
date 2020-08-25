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
  
# 5.3 source compiling using 8.2
- Needs a few patchhttps://gcc.gnu.org/git/?p=gcc.git;a=commitdiff;h=ec1cc0263f156f70693a62cf17b254a0029f4852
- https://gcc.gnu.org/git/?p=gcc.git;a=commitdiff;h=ec1cc0263f156f70693a62cf17b254a0029f4852
  - cfns.gperf, cfns.h, except.c
- https://gcc.gnu.org/git/?p=gcc.git&a=commit;h=16b277761b432510ad6dcf72d877ae72b5f0a4b7
  - Apply i386 for intel64 build
- https://gcc.gnu.org/bugzilla/show_bug.cgi?id=81066
- comment out ustat.h. See below.

# 5.5 source compiling using 8.2
- https://stackoverflow.com/questions/56096060/how-to-fix-the-gcc-compilation-error-sys-ustat-h-no-such-file-or-directory-i
  - Comment out ustat.h and ustat variable
