## using intel compiler ##
```bash
export CPP='icpc -E';export CC='icc'; export CXX='icpc' ; export F77=ifort; export FC=ifort
export C_INCLUDE_PATH+=:/opt/libs/zlib/1.2.8/gcc_447/include:/opt/libs/bzip2/1.0.6_gcc447/include:/opt/libs/xz/5.2.2_gcc447/include:/opt/libs/pcre/8.39_gcc447/include:/opt/libs/curl/7.50.3_gcc447/include  
export INCLUDE_PATH=$C_INCLUDE_PATH  
export LD_LIBRARY_PATH+=:/opt/libs/zlib/1.2.8/gcc_447/lib:/opt/libs/bzip2/1.0.6_gcc447/lib:/opt/libs/xz/5.2.2_gcc447/lib:/opt/libs/pcre/8.39_gcc447/lib::/opt/libs/curl/7.50.3_gcc447/lib   
 export LDFLAGS="-L/opt/libs/bzip2/1.0.6_gcc447/lib -lbz2 -L/opt/libs/xz/5.2.2_gcc447/lib -llzma -L/opt/libs/curl/7.50.3_gcc447/lib -lcurl -L/opt/libs/pcre/8.39_gcc447/lib -lpcre"  
./configure --prefix=/opt/apps/R/3.5.1/intel18  --with-cairo=yes --with-libpng=yes --with-jpeglib=yes --with-libtiff=yes  --with-x=yes --with-readline=yes --enable-R-shlib --enable-memory-profiling --with-blas=" -mkl=parallel  -L/opt/compiler/intel/18.0/mkl/lib/intel64 -L/opt/compiler/intel/18.0/lib/intel64 -lmkl_intel_lp64 -lmkl_lapack95_lp64 -lmkl_blas95_lp64 -lmkl_intel_thread -lmkl_core -lpthread -liomp5" --with-lapack=" -mkl=parallel  -L/opt/compiler/intel/18.0/mkl/lib/intel64 -L/opt/compiler/intel/18.0/lib/intel64  -lmkl_intel_lp64  -lmkl_lapack95_lp64 -lmkl_blas95_lp64 -lmkl_intel_thread -lmkl_core -lpthread -liomp5"  
```
- In lib64./R/etc/Makeconf, add CXXFLAGS += -wd308

# Using gnu compiler and MKL
- install bzip2, xz, curl, pcre. 
- for bzip2: make -f Makefile-libbz2_so ;  make  PREFIX=/opt/libs/bzip2/1.0.6  install ; *so files are copied manually
- For pcre: ./configure --prefix=/usr/nic/apps/pcre/8.42 --enable-utf8 
-  texlive or pdflatex command might be necessary to yield pdf handling
```bash
export C_INCLUDE_PATH=/opt/pbs/include:/opt/utilities/include:/opt/libs/ffi/3.2.1/lib/libffi-3.2.1/include:/opt/libs/bzip2/1.0.6/include:/opt/libs/xz/5.2.4/include:/opt/apps/curl/7.61.1/include:/opt/apps/pcre/8.42/include  
export INCLUDE=$C_INCLUDE_PATH  
export LDFLAGS="-L/opt/libs/bzip2/1.0.6/lib -lbz2 -L/opt/libs/xz/5.2.4/lib -llzma -L/opt/apps/curl/7.61.1/lib -lcurl -L/opt/apps/pcre/8.42/lib -lpcre"  
./configure --prefix=/opt/apps/R/3.5.1 --with-cairo=yes --with-libpng=yes --with-jpeglib=yes --with-libtiff=yes  --with-x=yes --with-readline=yes --enable-R-shlib --enable-memory-profiling --with-blas=" -L/opt/compiler/intel/18.0/mkl/lib/intel64 -L/opt/compiler/intel/18.0/lib/intel64 -lmkl_gf_lp64 -lmkl_lapack95_lp64 -lmkl_blas95_lp64 -lmkl_gnu_thread -lmkl_core -lpthread -liomp5" --with-lapack=" -L/opt/compiler/intel/18.0/mkl/lib/intel64 -L/opt/compiler/intel/18.0/lib/intel64  -lmkl_gf_lp64  -lmkl_lapack95_lp64 -lmkl_blas95_lp64 -lmkl_gnu_thread -lmkl_core -lpthread -liomp5"  
make -j 32; make install  
```
# Add R into jupyter notebook
- install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'), dependencies=TRUE, lib="/opt/R/3.5.1/lib64/R/library")   
- devtools::install_github('IRkernel/IRkernel')  
- IRkernel::installspec()   
- This will make ir folder in /home/__user__/.local/share/jupyter/kernels. Then copy the ir folder into /opt/python/3.6.6/share/jupyter/kernels/

# Using KerasR
- install.packages('reticulate')  
- library(reticulate)  
- use_python("/opt/apps/python_data_analytics/3.6.0/bin/python3")  
- install.packages('kerasR')  

## install Rmpi with openmpi
- R CMD INSTALL Rmpi_0.6-9.tar.gz --configure-args="--with-Rmpi-include=/share/mpi/ompi/400_gcc48/include --with-Rmpi-libpath=/share/mpi/ompi/400_gcc48/lib --with-Rmpi-type=OPENMPI" --no-test-load

# install pbdMPI with openmpi
-  Requires install.packages('rlecuyer')
- R CMD INSTALL pbdMPI_0.3-8.tar.gz --configure-args="--with-mpi-include=/share/mpi/ompi/400_gcc48/include --with-mpi-libpath=/share/mpi/ompi/400_gcc48/lib --with-mpi-type=OPENMPI --with-mpi=/share/mpi/ompi/400_gcc48" --no-test-load

# Install Rmpi with MS-MPI at windows
- Ref:http://www.stats.uwo.ca/faculty/yu/Rmpi/
- Use MS-MPI: https://msdn.microsoft.com/en-us/library/windows/desktop/bb524831%28v=vs.85%29.aspx
- Install MSMpiSetup.exe and msmpisdk.msi
 - Edit control panel -> Edit the system environment variables for MPI_HOME and PATH
  - MPI_HOME as "C:\Program Files(x86)\Microsoft SDKs\MPI"
  - Add C:\Program Files\R\R-3.4.1\bin to PATH
- Open R as admin
 - .libPaths("C:/Program Files/R/R-3.4.1/library")
  - Adjust path accordingly
 - install.packages("Rmpi")
- Open cmd windows
 - mpiexec -n 2 Rscript Rmpi_hello.r

