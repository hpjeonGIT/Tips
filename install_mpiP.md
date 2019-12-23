## SRC: https://github.com/LLNL/mpiP
- Instlal libunwind
- `./configure --prefix=/opt/mpiP/3.4.1_gcc53 --with-cc=mpicc --with-cxx=mpicxx --with-f77=mpif90 \
CFLAGS=-I/opt/libunwind/1.3.1_gcc53/include LDFLAGS=-L/opt/libunwind/1.3.1_gcc53/lib --enable-collective-report-default
- make -j 10; make install # will install libmpiP.a
- make shared ; make install # will install libmpiP.so

## For SRC using cmake
- export LDFLAGS="-L/opt/mpiP/3.4.1_gcc53/lib -lmpiP -lm -lbfd -liberty -L/opt/libunwind/1.3.1_gcc53/lib -lunwind“
- export CMAKE_MODULE_LINKER_FLAGS=$LDFLAGS
- export CMAKE_SHARED_LINKER_FLAGS=$LDFLAGS
- export CMAKE_STATIC_LINKER_FLAGS=$LDFLAGS
- Then run cmake or ccmake

## When run
- export LD_LIBRARY_PATH+=:/opt/mpiP/3.4.1_gcc53/lib:/opt/libunwind/1.3.1_gcc53/lib
- mpirun -n 10 ./a.out # in the end, mpiP will show that which file was produced and data are stored


