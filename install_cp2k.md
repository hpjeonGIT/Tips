## using intel compiler only
- intel mkl and intel mpi
- may use arch/Linux-x86-64-intel-minimal.psmp
- make -j 10 ARCH=Linux-x86064-intel-minimal.psmp
- if system gcc is too old, we can couple new gcc with intel compiler
  - `CC = mpiicc -qopenmpp -gcc-name=/opt/gcc/5.3/bin/gcc`
  - `FC = mpiifort -qopenmp -gcc-name=/opt/gcc/5.3/bin/gcc`
