# Installation of openfoam for firefoam from source package
git clone https://github.com/OpenFOAM/OpenFOAM-dev.git; git checkout 1ff57870007ac317d95a1756b41fd76c5a1e8f26 
* Requires intel compiler >=16 (ref: https://bugs.openfoam.org/view.php?id=2473)

# prerequisite
- Install gmp: `./configure --prefix=/share/libs/gmp/612_gcc51; make -j 32; make all; make install`
- Install mpfr: `./configure --prefix=/share/libs/mpfr/402_gcc51 --with-gmp=/share/libs/gmp/612_gcc51; make -j 32; make all; make install`
- Install scotch: `cd src; ln -s Make.inc/Makefile.inc.x86-64_pc_linux2 Makefile.inc; # add -fPIC in the CFLAGS ; make -j 32 scotch; export C_INCLUDE_PATH+=:/share/mpi/ompi/401_gcc51/include ; make -j32 ptscotch ; make prefix=/usr/nic/libs/scotch/607_gcc51 install`
- Install CGAL: `mkdir build; cd buld; ccmake ..; # configure using gmp/mpfr; make -j 32; make install`

# setup compiler and mpi environment as necessary
```
export LD_LIBRARY_PATH+=:/usr/local/gmp/612_gcc51/lib:/usr/local/mpfr/315_gcc51/lib:/usr/local/scotch/603_intel15/lib:/usr/local/cgal/47_gcc51/lib
export PATH+=:/usr/local/scotch/603_intel15/bin:/usr/local/cgal/47_gcc51/bin
export  MPI_ROOT=/usr/local/intel/18.0/impi_latest
export MPI_ARCH_FLAGS="-DMPICH_SKIP_MPICXX "
export MPI_ARCH_INC="-isystem $MPI_ROOT/include64" 
export MPI_ARCH_LIBS="-L$MPI_ROOT/lib64" 
export SCOTCH_ROOT=/usr/local/scotch/603_intel15
```
- edit etc/bashrc for prefix and icc
- set MPI type as IMPI and add IMPI) section at etc/config.sh/mpi
- REF: http://www.hpcadvisorycouncil.com/pdf/OpenFOAM_Best_Practices.pdf
- make  OpenFOAM-dev-version-5.0/wmake/rules/General/mplibIMPI
- edit etc/config.sh/scotch , CGAL, settings  for the location of scotch, boost, cgal, mpfr, gmp

```
source etc/bashrc
./Allwmake -j32
```
* To clean, ./wmake/wclean all
* issue
if PATH error appears:

`export MPFR_ARCH_PATH=/usr/local/mpfr/315_gcc51; export GMP_ARCH_PATH=/usr/local/gmp/612_gcc51; export BOOST_ARCH_PATH=/usr/local/boost/1.64_intel15; export CGAL_ARCH_PATH=/usr/local/cgal/47_gcc51 ;  export CGAL_INC="-I${CGAL_ARCH_PATH}/include -I${MPFR_ARCH_PATH}/include -I${GMP_ARCH_PATH}/include -I${BOOST_ARCH_PATH}/include -I/usr/include" ;  export CGAL_LIBS="-L${CGAL_ARCH_PATH}/lib -L${MPFR_ARCH_PATH}/lib -L${GMP_ARCH_PATH}/lib -L${BOOST_ARCH_PATH}/lib -lCGAL -lmpfr"`

* At /usr/nic/libs/mpfr/315_gcc51/, ln -s lib lib64

### Unofficial version
`git clone https://github.com/Unofficial-Extend-Project-Mirror/foam-extend-foam-extend-4.0.git`
Configure openmpi environment
```
export LD_LIBRARY_PATH+=:/share/libs/gmp/612_gcc48/lib:/share/libs/mpfr/400_gcc48/lib:/share/apps/scotch/604_gcc73/lib:/share/libs/cgal/411_gcc73/lib
export PATH+=:/share/apps/scotch/604_gcc73/bin:/share/libs/cgal/411_gcc73/bin
export MPI_ROOT=/share/mpi/ompi/300_gcc48
export MPI_ARCH_FLAGS="-DMPICH_SKIP_MPICXX "
export MPI_ARCH_INC="-isystem $MPI_ROOT/include"
export MPI_ARCH_LIBS="-L$MPI_ROOT/lib"
export SCOTCH_ROOT=/share/apps/scotch/604_gcc73
export SCOTCH_LIB_DIR=/share/apps/scotch/604_gcc73/lib
export CGAL_LIB_DIR=/share/libs/cgal/411_gcc73/lib
```
- edit etc/bashrc for prefix and icc: Choose SYSTEMOPENMPI
```bash
source etc/bashrc
./Allwmake -j32
```

### Sample run
```
source etc/bashrc 
cd $FOAM_TUTORIALS/incompressible/simpleFoam/
cp -r pitzDailyExptInlet pitzDailyExptInlet.test
cd pitzDailyExptInlet.test/
blockMesh 2>&1 | tee log. blockMesh
decomposePar 2>&1 | tee log. decomposePar
mpirun -np 4 simpleFoam -parallel 2>&1 | tee log.simpleFoam
```

