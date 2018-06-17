# Note
- In order to use parallel IO in netcdf, hdf5 must have been installed using parallel io option.
- C_INCLUDE_PATH, INCLUDE, LD_LIBRARY_PATH must include the correspondents of hdf5
- Recently netcdf split c/fortran distribution.
## C version
- edit include/netcdf.h for 
- #define NC_MAX_DIMS     65536
- #define NC_MAX_VARS     524288
- ./configure --prefix=/opt/libs/netcdf/4.6.1_intel18 --enable-netcdf4 CC=mpiicc LDFLAGS="-L/opt/libs/hdf5/1.10.1_intel18/lib" CPPFLAGS="-I/opt/libs/hdf5/1.10.1_intel18/include" 
Make; make install;make check
##Fortran version
- Edit fortran/module_netcdf_nc_data.F90 for NC_MAX_DIMS and NC_MAX_VARS
- ./configure --prefix=/opt/libs/netcdf/4.4.4_ifort18 LDFLAGS="-L/opt/libs/hdf5/1.10.1_intel18/lib" CPPFLAGS="-I/opt/libs/hdf5/1.10.1_intel18/include -I/opt/libs/netcdf/4.6.1_intel18/include" CC=mpiicc FC=mpiifort
Make –j16; make install

