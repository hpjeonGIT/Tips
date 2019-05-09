# Using intel compiler
- Ref: https://software.intel.com/en-us/articles/recipe-lammps-for-intel-xeon-phi-processors
- Configure MKL/IMPI by sourcing intel configuration scripts
- make yes-asphere yes-class2 yes-kspace yes-manybody yes-misc yes-molecule
- make yes-mpiio yes-opt yes-replica yes-rigid
- make yes-user-omp yes-user-intel
- cp MAKE/OPTIONS/Makefile.knl MAKE/OPTIONS/Makefile.intel18
- Open Makefile.intel18 and change -xMIC-AVX512 to -xCORE-AVX512 or -xAVX2. MIC-AVX512 is for PCI Intel Xeon Phi using off-loading
  - -xCORE-AVX512 or -xCOMMON-AVX512 for skylake
- make intel18 -j 16
- Sample Makefile.intel18
```
# skylake cpu customization
SHELL = /bin/sh
CC =        mpiicpc
OPTFLAGS =      -xCORE-AVX512 -O2 -fp-model fast=2 -no-prec-div -qoverride-limits
CCFLAGS =   -qopenmp -qno-offload -fno-alias -ansi-alias -restrict \
        -DLMP_INTEL_USELRT -DLMP_USE_MKL_RNG $(OPTFLAGS)
SHFLAGS =   -fPIC
DEPFLAGS =  -M
LINK =      mpiicpc
LINKFLAGS = -qopenmp $(OPTFLAGS)
LIB =           -ltbbmalloc
SIZE =      size
ARCHIVE =   ar
ARFLAGS =   -rc
SHLIBFLAGS =    -shared
LMP_INC =   -DLAMMPS_GZIP -DLAMMPS_JPEG
MPI_INC =       -DMPICH_SKIP_MPICXX -DOMPI_SKIP_MPICXX=1
MPI_PATH = 
MPI_LIB =
FFT_INC =       -DFFT_MKL -DFFT_SINGLE
FFT_PATH = 
FFT_LIB =       -L$(MKLROOT)/lib/intel64/ -lmkl_intel_ilp64 \
        -lmkl_sequential -lmkl_core 
JPG_INC =       
JPG_PATH =  
JPG_LIB =   -ljpeg
include Makefile.package.settings
include Makefile.package
EXTRA_INC = $(LMP_INC) $(PKG_INC) $(MPI_INC) $(FFT_INC) $(JPG_INC) $(PKG_SYSINC)
EXTRA_PATH = $(PKG_PATH) $(MPI_PATH) $(FFT_PATH) $(JPG_PATH) $(PKG_SYSPATH)
EXTRA_LIB = $(PKG_LIB) $(MPI_LIB) $(FFT_LIB) $(JPG_LIB) $(PKG_SYSLIB)
vpath %.cpp ..
vpath %.h ..
$(EXE): $(OBJ)
$(LINK) $(LINKFLAGS) $(EXTRA_PATH) $(OBJ) $(EXTRA_LIB) $(LIB) -o $(EXE)
$(SIZE) $(EXE)
lib:    $(OBJ)
$(ARCHIVE) $(ARFLAGS) $(EXE) $(OBJ)
shlib:  $(OBJ)
$(CC) $(CCFLAGS) $(SHFLAGS) $(SHLIBFLAGS) $(EXTRA_PATH) -o $(EXE) \
$(OBJ) $(EXTRA_LIB) $(LIB)
%.o:%.cpp
$(CC) $(CCFLAGS) $(SHFLAGS) $(EXTRA_INC) -c $<
%.d:%.cpp
$(CC) $(CCFLAGS) $(EXTRA_INC) $(DEPFLAGS) $< > $@
%.o:%.cu
$(CC) $(CCFLAGS) $(SHFLAGS) $(EXTRA_INC) -c $<
depend : fastdep.exe $(SRC)
@./fastdep.exe $(EXTRA_INC) -- $^ > .depend || exit 1
fastdep.exe: ../DEPEND/fastdep.c
cc -O -o $@ $<
sinclude .depend
```
- Sample run command
  - export OMP_NUM_THREADS=1
  - mpirun -np 32 /src/lmp_intel18 < in.rhodo


# GPU package with Nvidia CUDA
- Ref: https://lammps.sandia.gov/doc/Build_extras.html#gpu
- http://www.afs.enea.it/software/lammps/doc17/html/accelerate_gpu.html
- Ref: https://sites.google.com/site/rangsiman1993/comp-chem/program-install/install-lammps-pk-gpu
- When openmpi is instlalld with --with-cuda, $CUDA_HOME/lib64 and $CUDA_HOME/lib64/stubs must be on LD_LIBRARY_PATH
- Edit lib/gpu/Makefile.linux, Makefile.linux.double, Makfile.linux.mixed, Makefile.lammps.standard, Makefile.lammps
```
CUDA_HOME=/usr/nic/libs/cuda/10.0/
CUDA_ARCH="-arch=sm_70"
CUDA_PRECISION="-D_SINGLE_DOUBLE"
```
- make no-all
- make yes-gpu yes-asphere yes-class2 yes-kspace yes-manybody yes-misc yes-molecule yes-rigid yes-user-omp
- make gpu
- Run command: `mpirun -n 4  ../../src/lmp_gpu -sf gpu -pk gpu 4 -in in.lj`
- Batch job: Submit a following PBS script
```bash
#!/bin/bash
#PBS -l select=2:ncpus=40:mpiprocs=2:ompthreads=20:ngpus=2
#PBS -l walltime=10:00:00
#PBS -N atomtest
#PBS -q @atom
cd $PBS_O_WORKDIR
export NNODES=`sort $PBS_NODEFILE | uniq | wc -l`
export NPROCS=`wc -l < $PBS_NODEFILE`
. /etc/profile.d/modules.sh
module load ompi/4.0.1_gcc74_cuda10
mpirun -np $NPROCS  /work/jeonb/LAMMPS/lammps-stable_12Dec2018_Atom/src/lmp_gpu -sf gpu -pk gpu 2 -in in.rhodo
```

# USER-CUDA
- Deprecated. May not be supported anymore

# LAMMPS KOKKOS
- REF: http://www.hpcadvisorycouncil.com/pdf/LAMMPS_KOKKOS_Best_Practices.pdf
- http://www.afs.enea.it/software/lammps/doc17/html/accelerate_kokkos.html
- Centos7 with openmpi 4.0.1 + cuda 10 + ucx1.5.1 (there seems bugs in old ucx)
  - Install ucx 1.5.1 with cuda aware mode
```
module load gcc/7.4
./configure --prefix=/share/libs/openucx/1.5.1_cuda -with-cuda=/share/libs/cuda/10.0 \
--with-knem=/opt/knem-1.1.3.90mlnx1 --with-mlx5-dv --with-dm
make -j 20 all
make install
```
  - Install openmpi with cuda + ucx_cuda
```
./configure --prefix=/share/mpi/ompi/401_gcc74_cuda_ucx151 --with-cuda=/share/libs/cuda/10.0 \
--disable-dependency-tracking --disable-silent-rules --enable-binaries --enable-mpi-cxx \
--enable-mpi-cxx-seek --enable-shared --enable-openib-rdmacm --enable-fast-install \
 --with-devel-headers --with-hwloc=internal --with-tm=/opt/pbs/ --with-verbs=auto \
 --with-lustre --enable-oshmem --with-knem=/opt/knem-1.1.3.90mlnx1 \
 --with-mxm=/opt/mellanox/mxm --with-platform=contrib/platform/mellanox/optimized \
 --with-hcoll=/opt/mellanox/hcoll --enable-mpi1-compatibility --with-ucx=/share/libs/openucx/1.5.1_cuda
 make -j 20 all
 make install
```
- Edit lib/kokkos/Makefile.kokkos
```
KOKKOS_DEVICES ?= "Cuda,OpenMP"
KOKKOS_ARCH ?= "Volta70"
```
- Edit lib/kokkos/bin/nvcc_wrapper
```
default_arch="sm_70"
```
- Edit MAKE/OPTIONS/Makefile.kokkos_cuda_mpi
```
KOKKOS_DEVICES = Cuda, OpenMP
KOKKOS_ARCH = Volta70
```
- make no-all
- make yes-gpu yes-asphere yes-class2 yes-kspace yes-manybody yes-misc yes-molecule yes-rigid yes-kokkos
- make kokkos_cuda_mpi -j 40
- mpirun -np 2 ../../src/lmp_kokkos_cuda_mpi -k on g 2 -sf kk -in in.lj          # 1 node,   2 MPI tasks/node, 2 GPUs/node
- ~~If mxm_handle_error() appears, use `-mca pml ob1` in mpirun~~
- CUDA + OpenMP
		- `export OMP_PROC_BIND=false`
		- `mpirun -np 2 --bind-to socket  ../../src/lmp_kokkos_cuda_mpi -k on g 2 t 4  -sf kk -in in.rhodo`
			- Further optimization is necessary

