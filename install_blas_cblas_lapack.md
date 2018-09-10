# Download  blas.tgz from netlib : http://www.netlib.org/blas/blas-3.8.0.tgz
- cd BLAS
## static
- gfortran -c -O3 *.f;  ar rv libblas.a *.o; sudo cp libblas.a /opt/somewhere
## dynamic
- gfortran -shared -fPIC -O3 *.f -o libblas.so
# CBLAS
## download http://www.netlib.org/blas/blast-forum/cblas.tgz
## Edit Makefile.in # blas library is required
- make
# lapack
## Download http://www.netlib.org/lapack/lapack-3.8.0.tar.gz
cp make.inc.example make.inc; vi make.inc
# Edit BLAS and CBLAS location
make
