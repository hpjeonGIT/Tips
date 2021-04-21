# When system /lib64/libtinfo.so is not compatible, install Ncurses 6.1 (or newer) first.
./configure --with-shared --with-termlib=tinfo --prefix=/opt/ncurses/6.1
; make –j24; make install
# new ncurl might be necessary

# when libncurses is not coupled, ccmake will not be produced.
- If checking for curses support failed, use:
 - `./bootstrap --prefix=/opt/cmake_3.14.6 --parallel=20 -- -DBUILD_CursesDialog=ON -DCURSES_LIBRARY=/opt/ncurses_6.2/lib/libncurses.so -DCURSES_INCLUDE_PATH=/opt/ncurses_6.2/include/ncurses`
- `make -j 20; make install`
- If an error message comes:fatal error: ncurses/ncurses_dll.h: No such file or directory’
 - `ln -s /opt/ncurses/6.1/include/ncurses/*.h /opt/ncurses/6.1/include`
 - `./bootstrap --prefix=/opt/cmake_3.14.6 --parallel=20 -- -DBUILD_CursesDialog=ON -DCURSES_LIBRARY=/opt/ncurses_6.2/lib/libncurses.so -DCURSES_INCLUDE_PATH=/opt/ncurses_6.2/include`
 - Include paths of include/ncurses and include/ are required but cmake path may not understand multiple paths. So make symbolic links to be included.

# Now unpack cmake source code
./bootstrap --help; 
 ./bootstrap --prefix=/opt/cmake/3.11.4 --parallel=4;
 make -j16 ;
### If –ltinfo is not found, then edit Source/CMakeFiles/ccmake.dir/link.txt and add -L/opt/ncurses/6.1/lib in the left of -ltinfo
### or edit Modules/FindCurses.cmake of the main source files
set(CURSES_INCLUDE_DIRS "/opt/libs/ncurses/6.1/include")

set(CURSES_INCLUDE_DIR "/opt/libs/ncurses/6.1/include")

set(CURSES_INCLUDE_LIBRARIES "/opt/libs/ncurses/6.1/lib/libncurses.so")        

set(CURSES_INCLUDE_LIBRARY "/opt/libs/ncurses/6.1/lib/libncurses.so")        

## Edit CMakeCache.txt, adding -L/opt/libs/ncurses/6.1/lib -ltinfo as well
### if signal.c:(.text+0x1370): undefined reference to `pthread_atfork' => in CMakeCache.txt, convert -lpthread into -pthread then run 
```
export LD_LIBRARY_PATH+=:/opt/libs/ncurses/6.1/lib
make
make install
```

## building shared libs
- `CMAKE_SHARED_LINKER_FLAGS="-Wl,-Bsymbolic"` when links are messed up

## enforcing `$PREFIX/lib64`
- Ubuntu may make `$PREFIX/lib`
- `CMAKE_INSTALL_LIBDIR:PATH=lib64`

## After running cmake command, when there is an error message: undefined reference to pthread_create
- This might not be cmake or environment issue. May try again disabling employed options
- When labeling fails in add_test() or matching name doesn't exist, this error message may appear. Fix all the grammar in cmake file.
