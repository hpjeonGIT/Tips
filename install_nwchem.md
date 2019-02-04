
#### run mpiifort –show and use the info into LIBMPI
#### Unpack the source and locate into NWCHEM_TOP


- export NWCHEM_TOP=/usr/nic/apps/nwchem/6.8_intel19
- export NWCHEM_TARGET=LINUX64
- export NWCHEM_MODULES=all
- export MPI_LOC=/usr/nic/compiler/intel/19.1/impi/2019.1.144   # /share/mpi/ompi/400_gcc74
- export MPI_LIB=$MPI_LOC/intel64/lib
- export MPI_INCLUDE=$MPI_LOC/intel64/include
- export LIBMPI="-I/usr/nic/compiler/intel/19.1//compilers_and_libraries_2019.1.144/linux/mpi/intel64/include \
-I/usr/nic/compiler/intel/19.1//compilers_and_libraries_2019.1.144/linux/mpi/intel64/include \
-L/usr/nic/compiler/intel/19.1//compilers_and_libraries_2019.1.144/linux/mpi/intel64/lib/release \
-L/usr/nic/compiler/intel/19.1//compilers_and_libraries_2019.1.144/linux/mpi/intel64/lib -Xlinker \
--enable-new-dtags -Xlinker -rpath -Xlinker \
/usr/nic/compiler/intel/19.1//compilers_and_libraries_2019.1.144/linux/mpi/intel64/lib/release \
-Xlinker -rpath -Xlinker /usr/nic/compiler/intel/19.1//compilers_and_libraries_2019.1.144/linux/mpi/intel64/lib \
-lmpifort -lmpi -ldl -lrt -lpthread"
- export USE_MPI=y
- export USE_MPIF=y
- export USE_MPIF4=y
- export USE_64TO32=yes
- export NWCHEM_MODULES="all python" 
- export PYTHONHOME=/share/apps/python_da/3.6.8
- export PYTHONVERSION=3.6
- export PYTHONCONFIGDIR=config-3.6m-x86_64-linux-gnu
- export USE_PYTHON64=y
- export MKLROOT=/usr/nic/compiler/intel/19.1
- export MKLLIB="${MKLROOT}/mkl/lib/intel64"
- export MKLINC="${MKLROOT}/mkl/include"
- export HAS_BLAS=y
- export BLAS_SIZE=8
- export BLASOPT="-L${MKLROOT}/mkl/lib/intel64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -L${MKLROOT}/lib/intel64 -liomp5 -lpthread -lm -ldl"
- export LAPACK_SIZE=8
- export LAPACK_LIB="$BLASOPT"
- export LAPACK_LIBS="$BLASOPT"
- export LAPACKOPT="$BLASOPT"
- export USE_SCALAPACK=y
- export SCALAPACK_SIZE=8
- export SCALAPACK="-L${MKLROOT}/mkl/lib/intel64 -lmkl_scalapack_ilp64 -lmkl_intel_ilp64 -lmkl_intel_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl"
- export SCALAPACK_LIB="$SCALAPACK"
- export SCALAPACK_LIBS="$SCALAPACK"
### update C_INCLUDE_PATH and INCLUDE for Python.h
### Edit config/makefile.h and makefile-legacy.h , python-config => python3-config, lib64/python => lib/python, (PYTHONVERSION).$(PYTHONLIBTYPE) => (PYTHONVERSION)m.$(PYTHONLIBTYPE)
- cd src
- make realclean
- make nwchem_config FC=ifort CC=icc
- make 64_to_32 FC=ifort  CC=icc
- make FC=ifort  CC=icc
