## using intel compiler only
- intel mkl and intel mpi
- may use arch/Linux-x86-64-intel-minimal.psmp
- make -j 10 ARCH=Linux-x86064-intel-minimal.psmp
- if system gcc is too old, we can couple new gcc with intel compiler
  - `CC = mpiicc -qopenmpp -gcc-name=/opt/gcc/5.3/bin/gcc`
  - `FC = mpiifort -qopenmp -gcc-name=/opt/gcc/5.3/bin/gcc`

## coupling with libint
- This is for HF-style XC
- Download customized libint source from https://github.com/cp2k/libint-cp2k/releases/tag/v2.6.0
- Only one type of lmax can be installed
- Prepare a new source pack of cp2k
- Unpack libint source at cp2k/tools/toolchain/install
- Update arch/custom.psmp with LIBINT info. Refer other arch files as samples
  - LIBINT configuration must be in the head of custom.psmp, prior to mpicc or CC
- make command is same as above

## compiling with gcc environment
- Use mpich. mvapich2 seems not working
- install fftw from source. Add --enable-mpi --enable-openmp
- install lapack/blas with static library
- install scalapack library using cmake. Add -fPIC into CFLAGS and FFLAGS
- install libint with selcted lmax value. May need recent cmake
- When making arch/custom.psmp, add fftw and scalapack. In the end, add liblapack.a and libblas.a to LIB
  - lapack lib may not find blas library. then LIB += /.../libblas.a /..../liblapack.a /.../libbas.a -lz -ldl -lstdc++
  - Repeat libblas.a 
- For fortran flags,  -fallow-argument-mismatch  might be  necessary for gfortran > 10.x
