## using intel compiler ##
export CPP='icpc -E';export CC='icc'; export CXX='icpc' ; export F77=ifort; export FC=ifort

export C_INCLUDE_PATH+=:/opt/libs/zlib/1.2.8/gcc_447/include:/opt/libs/bzip2/1.0.6_gcc447/include:/opt/libs/xz/5.2.2_gcc447/include:/opt/libs/pcre/8.39_gcc447/include:/opt/libs/curl/7.50.3_gcc447/include

export INCLUDE_PATH=$C_INCLUDE_PATH

export LD_LIBRARY_PATH+=:/opt/libs/zlib/1.2.8/gcc_447/lib:/opt/libs/bzip2/1.0.6_gcc447/lib:/opt/libs/xz/5.2.2_gcc447/lib:/opt/libs/pcre/8.39_gcc447/lib::/opt/libs/curl/7.50.3_gcc447/lib
 export LDFLAGS="-L/opt/libs/bzip2/1.0.6_gcc447/lib -lbz2 -L/opt/libs/xz/5.2.2_gcc447/lib -llzma -L/opt/libs/curl/7.50.3_gcc447/lib -lcurl -L/opt/libs/pcre/8.39_gcc447/lib -lpcre"
./configure --prefix=/opt/apps/R/3.5.1/intel18  --with-cairo=yes --with-libpng=yes --with-jpeglib=yes --with-libtiff=yes  --with-x=yes --with-readline=yes --enable-R-shlib --enable-memory-profiling --with-blas=" -mkl=parallel  -L/opt/compiler/intel/18.0/mkl/lib/intel64 -L/opt/compiler/intel/18.0/lib/intel64 -lmkl_intel_lp64 -lmkl_lapack95_lp64 -lmkl_blas95_lp64 -lmkl_intel_thread -lmkl_core -lpthread -liomp5" --with-lapack=" -mkl=parallel  -L/opt/compiler/intel/18.0/mkl/lib/intel64 -L/opt/compiler/intel/18.0/lib/intel64  -lmkl_intel_lp64  -lmkl_lapack95_lp64 -lmkl_blas95_lp64 -lmkl_intel_thread -lmkl_core -lpthread -liomp5"

### In lib64./R/etc/Makeconf, add CXXFLAGS += -wd308

## Using gnu compiler and MKL
### install bzip2, xz, curl, pcre. 
####  for bzip2: make -f Makefile-libbz2_so ;  make  PREFIX=/opt/libs/bzip2/1.0.6  install ; *so files are copied manually
#### For pcre: ./configure --prefix=/usr/nic/apps/pcre/8.42 --enable-utf8 
#### texlive or pdflatex command might be necessary to yield pdf handling
export C_INCLUDE_PATH=/opt/pbs/include:/opt/utilities/include:/opt/libs/ffi/3.2.1/lib/libffi-3.2.1/include:/opt/libs/bzip2/1.0.6/include:/opt/libs/xz/5.2.4/include:/opt/apps/curl/7.61.1/include:/opt/apps/pcre/8.42/include

export INCLUDE=$C_INCLUDE_PATH

export LDFLAGS="-L/opt/libs/bzip2/1.0.6/lib -lbz2 -L/opt/libs/xz/5.2.4/lib -llzma -L/opt/apps/curl/7.61.1/lib -lcurl -L/opt/apps/pcre/8.42/lib -lpcre"

./configure --prefix=/opt/apps/R/3.5.1 --with-cairo=yes --with-libpng=yes --with-jpeglib=yes --with-libtiff=yes  --with-x=yes --with-readline=yes --enable-R-shlib --enable-memory-profiling --with-blas=" -L/opt/compiler/intel/18.0/mkl/lib/intel64 -L/opt/compiler/intel/18.0/lib/intel64 -lmkl_gf_lp64 -lmkl_lapack95_lp64 -lmkl_blas95_lp64 -lmkl_gnu_thread -lmkl_core -lpthread -liomp5" --with-lapack=" -L/opt/compiler/intel/18.0/mkl/lib/intel64 -L/opt/compiler/intel/18.0/lib/intel64  -lmkl_gf_lp64  -lmkl_lapack95_lp64 -lmkl_blas95_lp64 -lmkl_gnu_thread -lmkl_core -lpthread -liomp5"

make -j 32; make install

## Add R into jupyter notebook
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 'devtools', 'uuid', 'digest'), dependencies=TRUE, lib="/opt/R/3.5.1/lib64/R/library") 

devtools::install_github('IRkernel/IRkernel')

IRkernel::installspec() 

### This will make ir folder in /home/__user__/.local/share/jupyter/kernels. Then copy the ir folder into /opt/python/3.6.6/share/jupyter/kernels/
