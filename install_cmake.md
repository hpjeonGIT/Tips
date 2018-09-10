# When system /lib64/libtinfo.so is not compatible, install Ncurses 6.1 (or newer) first.
./configure --with-shared --with-termlib=tinfo --prefix=/opt/ncurses/6.1
; make –j24; make install
# new ncurl might be necessary

# Now unpack cmake source code
./bootstrap --help; 
 ./bootstrap --prefix=/opt/cmake/3.11.4 --parallel=4;
 make -j16 ;
### If –ltinfo is not found, then edit Source/CMakeFiles/ccmake.dir/link.txt and add -L/opt/ncurses/6.1/lib in the left of -ltinfo
### or edit Modules/FindCurses.cmake of the main source files
set( CMAKE_INCLUDE_PATH "/opt/libs/ncurses/6.1/include)

set( CMAKE_LIBRARY_PATH "/opt/libs/ncurses/6.1/lib/libncurses.so")
### if signal.c:(.text+0x1370): undefined reference to `pthread_atfork' => in CMakeCache.txt, convert -lpthread into -pthread then run make

make install

