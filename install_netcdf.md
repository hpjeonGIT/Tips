# Default configuration
- HDF5 path in C_INCLUDE_PATH, INCLUDE, LD_LIBRARY_PATH
## C version
- ./configure --prefix=/opt/libs/netcdf/4.6.1_intel18 --enable-netcdf4 CC=mpiicc LDFLAGS="-L/opt/libs/hdf5/1.10.1_intel18/lib" CPPFLAGS="-I/opt/libs/hdf5/1.10.1_intel18/include" FC=mpiifort --enable-remote-fortran-bootstrap 
; make; make install; make check # make sure all tests pass
## Fortran version
./configure --prefix=/opt/libs/netcdf/4.4.4_ifort18 LDFLAGS="-L/opt/libs/hdf5/1.10.1_intel18/lib –L/opt/libs/netcdf/4.6.1_intel18/lib" CPPFLAGS="-I/opt/libs/hdf5/1.10.1_intel18/include -I/opt/libs/netcdf/4.6.1_intel18/include" CC=mpiicc FC=mpiifort
; make –j16; make install; make check # make sure all tests pass

