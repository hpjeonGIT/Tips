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
- May not need nvcc. Just link CUDA

# USER-CUDA
- Deprecated. May not be supported anymore

# LAMMPS KOKKOS
- REF: http://www.hpcadvisorycouncil.com/pdf/LAMMPS_KOKKOS_Best_Practices.pdf
- http://www.afs.enea.it/software/lammps/doc17/html/accelerate_kokkos.html
- In cmake: -D KOKKOS=yes
- In Make: make yes-KOKKOS
