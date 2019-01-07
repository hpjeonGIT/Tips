./configure --with-cc=mpicc --with-cxx=mpicxx --with-fc=mpifort \
--prefix=/opt/libs/petsc/3.10.3 \
 --with-valgrind-dir=/opt/apps/valgrind/3.14.0 \
 --with-blas-lapack-dir=/opt/intel/18.0/mkl/lib/intel64 
### or using netlib 
./configure --with-cc=mpicc --with-cxx=mpicxx --with-fc=mpifort \
--prefix=/opt/libs/petsc/3.10.3 \
 --with-valgrind-dir=/opt/apps/valgrind/3.14.0 \
 --with-blas-lapack-dir=/opt/libs/netlib/3.8.0/lib64

make all test 
make install
