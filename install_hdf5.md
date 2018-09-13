# hdf5 with intel mpi
unzip; mkdir build; cd build;../configure --prefix=/opt/libs/hdf5/1.10.1_intel18  --enable-shared --enable-static --enable-build-mode=production --enable-deprecated-symbols --enable-parallel --enable-hl --enable-fortran CC=mpiicc FC=mpiifort CXX=mpiicxx F77=mpiifort CPP="icc -E" CXXCPP="icpc -E" LDFLAGS="-L/opt/compiler/intel/18.0/lib/intel64/libiomp5.so"

# hdf5 with openmpi and gcc
unzip; mkdir build; cd build; ../configure --prefix=/opt/libs/hdf5/1.10.1_gcc48  -enable-shared --enable-static --enable-build-mode=production --enable-deprecated-symbols --enable-parallel --enable-hl --enable-fortran CC=mpicc FC=mpif90 CXX=mpicxx F77=mpif90

## Make sure if h5fc (or h5pfc) and lib**_fortran.so are produced
