
#### run mpif90 –show and use the info into LIBMPI
#### Unpack the source and locate into NWCHEM_TOP


- export NWCHEM_TOP=/share/apps/nwchem/6.8_gcc74
- export NWCHEM_TARGET=LINUX64
- export NWCHEM_MODULES=all
- export MPI_LOC=/share/mpi/ompi/400_gcc74
- export MPI_LIB=$MPI_LOC/lib
- export MPI_INCLUDE=$MPI_LOC/include
- export LIBMPI="-I/share/mpi/ompi/400_gcc74/include \
-I/share/mpi/ompi/400_gcc74/lib -L/opt/pbs/lib \
-L/opt/mellanox/sharp/lib -L/opt/mellanox/hcoll/lib -L/opt/mellanox/mxm/lib -Wl,-rpath -Wl,/opt/pbs/lib \
-Wl,-rpath -Wl,/opt/mellanox/fca/lib -Wl,-rpath -Wl,/opt/mellanox/mxm/lib \
-Wl,-rpath -Wl,/share/mpi/ompi/400_gcc74/lib -Wl,--enable-new-dtags \
-L/share/mpi/ompi/400_gcc74/lib -lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi"
- export USE_MPI=y
- export USE_MPIF=y
- export USE_MPIF4=y
- export USE_64TO32=yes
- export NWCHEM_MODULES="all python" 
- export PYTHONHOME=/share/apps/python_da/3.6.8
- export PYTHONVERSION=3.6
- export USE_PYTHON64=y
- export MKLROOT=/usr/nic/compiler/intel/19.1/mkl
- export MKLLIB="${MKLROOT}/lib/intel64"
- export MKLINC="${MKLROOT}/include"
- export HAS_BLAS=y
- export BLAS_SIZE=8
- export BLASOPT="-L${MKLROOT}/lib/intel64 -lmkl_gf_ilp64 -lmkl_gnu_thread -lmkl_core -liomp5 -lpthread -lm -ldl"
- export LAPACK_SIZE=8
- export LAPACK_LIB="$BLASOPT"
- export LAPACK_LIBS="$BLASOPT"
- export LAPACKOPT="$BLASOPT"
- export USE_SCALAPACK=y
- export SCALAPACK_SIZE=8
- export SCALAPACK="-L${MKLROOT}/lib/intel64 -lmkl_scalapack_ilp64 -lmkl_gf_ilp64 -lmkl_gnu_thread -lmkl_core -lmkl_blacs_intelmpi_ilp64 -liomp5 -lpthread -lm -ldl"
- export SCALAPACK_LIB="$SCALAPACK"
- export SCALAPACK_LIBS="$SCALAPACK"
### update C_INCLUDE_PATH and INCLUDE for Python.h 
- cd src
- make realclean
- make nwchem_config FC=gfortran CC=gcc
- make 64_to_32 FC=gfortran  CC=gcc
- make FC=gfortran  CC=gcc
