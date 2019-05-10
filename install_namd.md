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

## verbs - infiniband version
- CHARM
	- cd charm-6.8.2
	- Edit *src/arch/mpi-linux-x86_64/cc-mpicxx.sh* and *src/arch/mpi-linux-x86_64/conv-mach.sh*
		- Convert all mpicxx -> mpiicpc, mpicc -> mpiicc, gcc-> icc, g++-> icpc, mpif77 -> mpiifort, mpif90 -> mpiifort, f95 -> ifort, g77 -> ifort
	- ./build charm++ verbs-linux-x86_64 icc # for infinibands - slightly faster than MPI
- NAMD
	- Edit arch/Linux-x86_64-icc.arch
```bash
AMD_ARCH = Linux-x86_64
CHARMARCH = verbs-linux-x86_64-icc #mpi-linux-x86_64
FLOATOPTS = -ip -xCORE-AVX512  -O3 -g -fp-model fast=2 -no-prec-div -qoverride-limits -DNAMD_DISABLE_SSE
CXX = icpc -std=c++11
CXXOPTS = -static-intel -O2 $(FLOATOPTS)
CXXNOALIASOPTS = -O2 -fno-alias $(FLOATOPTS)
CXXCOLVAROPTS = -O2 -ip
CC = icc
COPTS = -static-intel -O2 $(FLOATOPTS)
```
	- ./config Linux-x86_64-icc --with-mkl --charm-base ./charm-6.8.2 --charm-arch verbs-linux-x86_64-icc
	- cd Linux-x86_64-icc/
	- make -j 40
	- *namd2* is produced
- Run command
	- charm-6.8.2/bin/charmrun +p 40  Linux-x86_64-icc/namd2 apoa1.namd

## NAMD with CUDA or GPU computing
- Ref: https://www.nvidia.com/en-us/data-center/gpu-accelerated-applications/namd/
- GCC build
	- CHARM
		- cd charm-6.8.2
		- ./build charm++ verbs-linux-x86_64 smp  --with-production # mpi-linux-x86_64 conflicts with cuda
			- SMP is necessary. NAMD instruction: CUDA builds require non-MPI SMP or multicore Charm++ arch for reasonable performance. Consider ibverbs-smp or verbs-smp (InfiniBand), gni-smp (Cray), or multicore (single node).
			- MPI build is not supported: ERROR: CUDA builds require non-MPI SMP or multicore Charm++ arch for reasonable performance.
	- NAMD
		- Edit arc/Linux-x86_64-g++.arch
```
NAMD_ARCH = Linux-x86_64
CHARMARCH = verbs-linux-x86_64
CXX = g++ -m64 -std=c++0x
CXXOPTS = -O3 -fexpensive-optimizations -ffast-math 
CC = gcc -m64
COPTS = -O3 -fexpensive-optimizations -ffast-math
```
	- Edit Linux-x86_64.mkl
```
FFTDIR=/share/compiler/intel/19.1/mkl
FFTINCL=-I$(FFTDIR)/include/fftw
FFTLIB=-L$(FFTDIR)/lib/intel64 -lmkl_gf_lp64 -lmkl_sequential -lmkl_core
FFTFLAGS=-DNAMD_FFTW -DNAMD_FFTW_3
FFT=$(FFTINCL) $(FFTFLAGS)
```
	- Edit arch/Linux-x86_64.tcl
        ```bash
        TCLDIR=/share/libs/tcl/8.6.9
        TCLINCL=-I$(TCLDIR)/include
        TCLLIB=-L$(TCLDIR)/lib -ltcl8.6 -ldl -lpthread
        TCLFLAGS=-DNAMD_TCL
        TCL=$(TCLINCL) $(TCLFLAGS)
        ```
		- ./config Linux-x86_64-g++.arch --with-mkl --charm-base ./charm-6.8.2 --charm-arch verbs-linux-x86_64-smp --with-cuda --cuda-prefix /usr/nic/libs/cuda/10.0
	- cd Linux-x86_64-g++.arch
    - make -j 20
    - *namd2* is produced
- Intel Compiler build
	- Configure Intel environment
	- CHARM
		- cd charm-6.8.2
		- ./build charm++ verbs-linux-x86_64 smp icc  --with-production
	- NAMD
		- Edit arc/Linux-x86_64-icc.arch
```
NAMD_ARCH = Linux-x86_64
CHARMARCH = verbs-linux-x86_64-smp-icc
FLOATOPTS = -ip -xCORE-AVX512  -O3 -g -fp-model fast=2 -no-prec-div -qoverride-limits -DNAMD_DISABLE_SSE
CXX = icpc -std=c++11
CXXOPTS = -static-intel -O2 $(FLOATOPTS)
CXXNOALIASOPTS = -O2 -fno-alias $(FLOATOPTS)
CXXCOLVAROPTS = -O2 -ip
CC = icc
COPTS = -static-intel -O2 $(FLOATOPTS)
```
	- Edit Linux-x86_64.mkl
```
FFTDIR=/share/compiler/intel/18.0/mkl
FFTINCL=-I$(FFTDIR)/include/fftw
FFTLIB=-L$(FFTDIR)/lib/intel64 -lmkl_gf_lp64 -lmkl_sequential -lmkl_core
FFTFLAGS=-DNAMD_FFTW -DNAMD_FFTW_3
FFT=$(FFTINCL) $(FFTFLAGS)
```
		- ./config Linux-x86_64-icc.arch --with-mkl --charm-base ./charm-6.8.2 --charm-arch verbs-linux-x86_64-smp-icc --with-cuda --cuda-prefix /share/libs/cuda/10.0
	- cd Linux-x86_64-icc.arch
    - make -j 20
    - *namd2* is produced
- Running:
	- Single node run: ../NAMD_CUDA/Linux-x86_64-g++.arch/namd2 +p 40 +devices 0,1 apoa1.namd
	- Multinodes not running. Charmrun> Waiting for 0-th client to connect. No solution at this moment
- Sample host_nodefile. Usage: ++nodelist ./host_nodefile
```
host aserver.my.org
host bserver.my.org
```
- Sample runscript. Usage: ++runscript ./run_script
```
#!/bin/bash
export LD_LIBRARY_PATH="${1:h}:$LD_LIBRARY_PATH"
$*
```
- If namd2 hangs, use `++verbose` to monitor the status


## checking charmrun
- After charm is built,
	- cd <charm_build>/tests/charm++/simplearrayhello/
	- make -j
	- mpirun -n 2 ./hello # check if it runs parallel or not
