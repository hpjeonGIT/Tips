## building shared libs
- CMAKE_SHARED_LINKER_FLAGS="-Wl,-Bsymbolic" when links are messed up

## enforcing $PREFIX/lib64
- Ubuntu may make $PREFIX/lib
- CMAKE_INSTALL_LIBDIR:PATH=lib64
