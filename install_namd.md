- Download the source code and Unpack NAMD
- Unpack charm inside of NAMD source folder
- Configure intel compiler, mkl, mpi environment
- CHARM
  - Reference: [link](http://hpckp.org/index.php/articles/best-practices/92-how-to-install-namd-2-9-with-intel-cluster-studio-2013-on-intel-sandy-bridge-architecture-and-ib-support)
  - cd charm-6.8.2
  - Edit src/arch/mpi-linux-x86_64/cc-mpicxx.sh and src/arch/mpi-linux-x86_64/conv-mach.sh
	  - Convert all mpicxx -> mpiicpc, mpicc -> mpiicc, gcc-> icc, g++-> icpc, mpif77 -> mpiifort, mpif90 -> mpiifort, f95 -> ifort, g77 -> ifort
  - ./build charm++  mpi-linux-x86_64
- NAMD
  - Reference: [link](https://software.intel.com/en-us/articles/recipe-building-namd-on-intel-xeon-and-intel-xeon-phi-processors-for-multi-node-runs), [link2](https://www.pugetsystems.com/labs/hpc/NAMD-Custom-Build-for-Better-Performance-on-your-Modern-GPU-Accelerated-Workstation----Ubuntu-16-04-18-04-CentOS-7-1196/#edit-archlinux-x86mkl)
  - Edit arch/Linux-x86_64-icc.arch
      ```bash
      AMD_ARCH = Linux-x86_64
      CHARMARCH = mpi-linux-x86_64-smp
      FLOATOPTS = -ip -xCORE-AVX512  -O3 -g -fp-model fast=2 -no-prec-div -qoverride-limits -DNAMD_DISABLE_SSE
      CXX = icpc -std=c++11
      CXXOPTS = -static-intel -O2 $(FLOATOPTS)
      CXXNOALIASOPTS = -O2 -fno-alias $(FLOATOPTS)
      CXXCOLVAROPTS = -O2 -ip
      CC = icc
      COPTS = -static-intel -O2 $(FLOATOPTS)
      ```
  - Edit arch/Linux-x86_64.tcl
      ```bash
      TCLDIR=/share/libs/tcl/8.6.9
      TCLINCL=-I$(TCLDIR)/include
      TCLLIB=-L$(TCLDIR)/lib -ltcl8.6 -ldl -lpthread
      TCLFLAGS=-DNAMD_TCL
      TCL=$(TCLINCL) $(TCLFLAGS)
      ```
  - ./config Linux-x86_64-icc --with-mkl --charm-base ./charm-6.8.2 --charm-arch mpi-linux-x86_64
  	- --with-mkl will use arch/Linux-x86_64.mkl
  - cd Linux-x86_64-icc/
  - make -j 32
  - *namd2* is produced
# Running namd
- Download *apoa1.tar.gz* from https://www.ks.uiuc.edu/Research/namd/utilities/
- export LD_LIBRARY_PATH+=:/share/libs/tcl/8.6.9/lib
- mpirun -n 40 ../NAMD_Git-2019-04-23_Source/Linux-x86_64-icc/namd2 apoa1.namd
