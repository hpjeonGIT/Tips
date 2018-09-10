# BLAS library from NETLIB #
# Download  blas.tgz from netlib : http://www.netlib.org/blas/blas-3.8.0.tgz
- cd BLAS

# static
- gfortran -c -O3 *.f
- ar rv libblas.a *.o
- sudo cp libblas.a /opt/somewhere

# dynamic
- gfortran -shared -fPIC -O3 *.f -o libblas.so

