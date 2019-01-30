# Default configuration
- HDF5 path in C_INCLUDE_PATH, INCLUDE, LD_LIBRARY_PATH
## C version
- ./configure --prefix=/opt/libs/netcdf/4.6.1_intel18 --enable-netcdf4 CC=mpiicc LDFLAGS="-L/opt/libs/hdf5/1.10.1_intel18/lib" CPPFLAGS="-I/opt/libs/hdf5/1.10.1_intel18/include" FC=mpiifort --enable-remote-fortran-bootstrap 
- make; make install; make check # make sure all tests pass
## Fortran version
- The lib of C version must be in LD_LIBRARY_PATH
- ./configure --prefix=/opt/libs/netcdf/4.4.4_ifort18 LDFLAGS="-L/opt/libs/hdf5/1.10.1_intel18/lib –L/opt/libs/netcdf/4.6.1_intel18/lib" CPPFLAGS="-I/opt/libs/hdf5/1.10.1_intel18/include -I/opt/libs/netcdf/4.6.1_intel18/include" CC=mpiicc FC=mpiifort
- make –j16; make install; make check # make sure all tests pass

# Using openCAF
- Configure CAF environment
- ./configure --prefix=/share/libs/netcdf/4.6.2_CA24 --enable-netcdf4 CC=mpicc LDFLAGS="-L/share/libs/hdf5/1.10.4_CAF24/lib" CPPFLAGS="-I/share/libs/hdf5/1.10.4_CAF24/include" FC=mpifort --enable-remote-fortran-bootstrap
- make  -j 40;make all; make install
- export LD_LIBRARY_PATH+=:/share/libs/netcdf/4.6.2_CA24/lib
- ./configure --prefix=/share/libs/netcdf/4.4.4_CAF24 LDFLAGS="-L/share/libs/hdf5/1.10.4_CAF24/lib -L/share/libs/netcdf/4.6.2_CA24/lib" CPPFLAGS="-I/share/libs/hdf5/1.10.4_CAF24/include -I/share/libs/netcdf/4.6.2_CA24/include" CC=mpicc FC=mpifort
- make -j40; make all; make install
