# When system /lib64/libtinfo.so is not compatible, install Ncurses 6.1 (or newer) first.
./configure --with-shared --with-termlib=tinfo --prefix=/opt/ncurses/6.1
; make –j24; make install

# Now unpack cmake source code
./bootstrap --help; 
 ./bootstrap --prefix=/opt/cmake/3.11.4 ;
 make -j16 ;
### If –ltinfo is not found, then edit Source/CMakeFiles/ccmake.dir/link.txt and add -L/opt/ncurses/6.1/lib in the left of -ltinfo
 make install

