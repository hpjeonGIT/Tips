# Using MK for lapack/blas
- ./configure --prefix=/opt/p4est/ CC-mpicc CXX=mpicxx FC=mipf90 F77=mpif77 --enable-openmp --enable-mpi --enable-pthread --with-blas="-L/opt/intel/2018/mkl/lib/intel65 -mkl_rt" --with-lapack="=L/opt/intel/2018/mkl/lib/intel64 -lmkl_rt"
- Use `mkl_rt`, not `mkl_core` or `mkl_gf_lp54`
- `make -j 20; make install`

# version 0.3.4.2
- Shared library is disabled as default
- Using --enable-shared
