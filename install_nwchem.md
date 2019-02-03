# 
run mpif90 –show and use the info into LIBMPI


- export NWCHEM_TOP=/usr/nic/apps/nwchem/6.8_gcc74
- export NWCHEM_TARGET=LINUX64
- export NWCHEM_MODULES=all
- export MPI_LOC=/usr/nic/mpi/ompi/400_gcc74
- export MPI_LIB=$MPI_LOC/lib
- export MPI_INCLUDE=$MPI_LOC/include
- export LIBMPI="-I/usr/nic/mpi/ompi/400_gcc74/include \
-I/usr/nic/mpi/ompi/400_gcc74/lib -L/opt/pbs/lib \
-L/opt/mellanox/sharp/lib -L/opt/mellanox/hcoll/lib -L/opt/mellanox/mxm/lib -Wl,-rpath -Wl,/opt/pbs/lib \
-Wl,-rpath -Wl,/opt/mellanox/fca/lib -Wl,-rpath -Wl,/opt/mellanox/mxm/lib \
-Wl,-rpath -Wl,/usr/nic/mpi/ompi/400_gcc74/lib -Wl,--enable-new-dtags \
-L/usr/nic/mpi/ompi/400_gcc74/lib -lmpi_usempif08 -lmpi_usempi_ignore_tkr -lmpi_mpifh -lmpi"
- export USE_MPI=y
- export USE_MPIF=y
- export USE_MPIF4=y
- export USE_64TO32=yes
- export NWCHEM_MODULES="all python" 
- export PYTHONHOME=/usr/nic/apps/python_da/3.6.8
- export PYTHONVERSION=3.6
- export USE_PYTHON64=y
- cd src
- make realclean
- make nwchem_config FC=gfortran CC=gcc
- make 64_to_32 FC=gfortran  CC=gcc
- make FC=gfortran  CC=gcc
