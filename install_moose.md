#Reference
- https://mooseframework.inl.gov/getting_started/installation/manual_installation_gcc.html
- https://lists.mcs.anl.gov/pipermail/petsc-users/2015-October/027404.html

# Preparation
- load the module of gcc and MPI accordingly
- export CC=mpicc; export CXX=mpicxx ; export F77=mpif77 ; export FC=mpif90; 
- export OPTFLAGS="-O3 -march=native -mtune=native -DNDEBUG"

# PETSC install
- Download petsc source. Also download external packages from http://ftp.mcs.anl.gov/pub/petsc/externalpackages/ or newer from their own sites
- The newest package might not be installed. Do some trials and errors
```
./configure \
 COPTFLAGS="$OPTFLAGS" CXXOPTFLAGS="$OPTFLAGS" FOPTFLAGS="$OPTFLAGS" CUDAOPTFLAGS="$OPTFLAGS" \
--prefix=/opt/petsc/3.12.2_4moose \
--with-debugging=0 \
--with-ssl=0 \
--with-pic=1 \
--with-openmp=1 \
--with-mpi=1 \
--with-shared-libraries=1 \
--with-cxx-dialect=C++11 \
--with-fortran-bindings=0 \
--with-sowing=0 \
--download-hypre=/opt/petsc/externals/hypre-2.15.1.zip \
--download-fblaslapack=/opt/petsc/externals/fblaslapack-3.1.1.tar.gz \
--download-metis=/opt/petsc/ANL/metis.tar.gz \
--download-ptscotch=/opt/petsc/externals/scotch_6.0.9.tar.gz \
--download-parmetis=/opt/petsc/externals/parmetis-4.0.3.tar.gz \
--download-superlu_dist=/opt/petsc/externals/superlu_dist-6.2.0.zip \
--with-scalapack-dir=/opt/scalapack/2.1_gcc53 \
--download-mumps=/opt/petsc/externals/MUMPS_5.2.1.tar.gz \
--download-slepc=/opt/petsc/externals/slepc-3.12.2.tar.gz \
PETSC_DIR=`pwd` PETSC_ARCH=linux-opt
```
- This didn't work. unpack those libraries at petsc/linux-opt/externalpackages/ and rename them such as metis-** to petsc-pkg-metis
- In particular, metis, parmetis, MUMPS may need to be from ftp.anl. New version may not work.
- Scalapack didnt' work. Install scalapack as a stand-alone then coupling using --with-scalapack-dir
  - ccmake ..; setup blas and lapack using existing libraries. dynamic (.so) only
  - make -j22; make install
- make PETSC_DIR=/opt/petsc/petsc-3.12.2 PETSC_ARCH=linux-opt all # took less than 5 min
- make PETSC_DIR=/opt/petsc/petsc-3.12.2 PETSC_ARCH=linux-opt install 
- make PETSC_DIR=/opt/petsc/petsc-3.12.2 PETSC_ARCH=linux-opt test # testing with MPI
```
Running test examples to verify correct installation  
Using PETSC_DIR=/share/apps/7/petsc/petsc-3.12.2 and PETSC_ARCH=linux-opt  
C/C++ example src/snes/examples/tutorials/ex19 run successfully with 1 MPI process  
C/C++ example src/snes/examples/tutorials/ex19 run successfully with 2 MPI processes  
C/C++ example src/snes/examples/tutorials/ex19 run successfully with hypre  
C/C++ example src/snes/examples/tutorials/ex19 run successfully with mumps  
C/C++ example src/snes/examples/tutorials/ex19 run successfully with superlu_dist  
Completed test examples  
```

# Installing moose
- VTK might be necesssary. Install or skip VTK in the moose (actually libmesh) configuration
- Will need the info of PETSC location. DO `export PETSC_DIR=/opt/petsc/3.12.2_4moose`
- Define VTKLIB_DIR and VTKINCLUDE_DIR if ncessary
- Download moose
  - If moose-master.zip is downloaded from github webpage, it will not contain 1) libmesh and 2) metaphysicL
  - Download each of them and upack libmesh at moose/libmesh. Unpack metaphysicL at moose/libmesh/contrib/metaphysicl
    - go to moose/libmesh/contrib/metaphysicl and run bootstrap script
    - go to moose/libmesh/contrib/timpi and run bootstrap script
- `cd moose; ./scripts/update_and_rebuild_libmesh.sh`
   - This will very slow. Or hack the script and edit as make -j 10

# Running tests
- `mkdir ~/project ; cd ~project ; cp -r /opt/moose/moose-next moose`
- `cd ~/projects/moose/test`
- `make -j 10` # took several minutes
- `make hit`
- Edit ~/.config/matplotlib/matplotlibrc as "backend : TkAgg"
- `./run_tests -j 10`
    
