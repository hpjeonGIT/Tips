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
set(CURSES_INCLUDE_DIRS "/opt/libs/ncurses/6.1/include")

set(CURSES_INCLUDE_DIR "/opt/libs/ncurses/6.1/include")

set(CURSES_INCLUDE_LIBRARIES "/opt/libs/ncurses/6.1/lib/libncurses.so")        

set(CURSES_INCLUDE_LIBRARY "/opt/libs/ncurses/6.1/lib/libncurses.so")        

## Edit CMakeCache.txt, adding -L/opt/libs/ncurses/6.1/lib -ltinfo as well
### if signal.c:(.text+0x1370): undefined reference to `pthread_atfork' => in CMakeCache.txt, convert -lpthread into -pthread then run 
export LD_LIBRARY_PATH+=:/opt/libs/ncurses/6.1/lib

make

make install

