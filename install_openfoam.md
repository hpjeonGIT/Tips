# Installation of openfoam for firefoam from source package

git clone https://github.com/OpenFOAM/OpenFOAM-dev.git; git checkout 1ff57870007ac317d95a1756b41fd76c5a1e8f26 

* Requires intel compiler >=16 (ref: https://bugs.openfoam.org/view.php?id=2473)

# setup compiler and mpi environment as necessary

export LD_LIBRARY_PATH+=:/usr/local/gmp/612_gcc51/lib:/usr/local/mpfr/315_gcc51/lib:/usr/local/scotch/603_intel15/lib:/usr/local/cgal/47_gcc51/lib

export PATH+=:/usr/local/scotch/603_intel15/bin:/usr/local/cgal/47_gcc51/bin

export  MPI_ROOT=/usr/local/intel/18.0/impi_latest

export MPI_ARCH_FLAGS="-DMPICH_SKIP_MPICXX "

export MPI_ARCH_INC="-isystem $MPI_ROOT/include64" 

export MPI_ARCH_LIBS="-L$MPI_ROOT/lib64" 

export SCOTCH_ROOT=/usr/local/scotch/603_intel15

- edit etc/bashrc for prefix and icc
- set MPI type as IMPI and add IMPI) section at etc/config.sh/mpi
- REF: http://www.hpcadvisorycouncil.com/pdf/OpenFOAM_Best_Practices.pdf
- make  OpenFOAM-dev-version-5.0/wmake/rules/General/mplibIMPI
- edit etc/config.sh/scotch , CGAL, settings  for the location of scotch, boost, cgal, mpfr, gmp

source etc/bashrc

./Allwmake -j32
* To clean, ./wmake/wclean all
* issue
if PATH error appears:

export MPFR_ARCH_PATH=/usr/local/mpfr/315_gcc51; export GMP_ARCH_PATH=/usr/local/gmp/612_gcc51; export BOOST_ARCH_PATH=/usr/local/boost/1.64_intel15; export CGAL_ARCH_PATH=/usr/local/cgal/47_gcc51 ;  export CGAL_INC="-I${CGAL_ARCH_PATH}/include -I${MPFR_ARCH_PATH}/include -I${GMP_ARCH_PATH}/include -I${BOOST_ARCH_PATH}/include -I/usr/include" ;  export CGAL_LIBS="-L${CGAL_ARCH_PATH}/lib -L${MPFR_ARCH_PATH}/lib -L${GMP_ARCH_PATH}/lib -L${BOOST_ARCH_PATH}/lib -lCGAL -lmpfr"

* At /usr/nic/libs/mpfr/315_gcc51/, ln -s lib lib64


