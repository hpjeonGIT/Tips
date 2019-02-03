## install tcl ##
- cd unix; ./configure --prefix=/opt/libs/tcl/8.6.8; make –j 20 ; make install

## install tk ##
- cd unix; ./configure --prefix=/opt/libs/tk/8.6.8 --with-tcl=/opt/libs/tcl/8.6.8/lib; make -j 20; make install

## install bzip2 source ###
- unzip
- make -f Makefile-libbz2_so
- make install PREFIX=/opt/bzip2/1.0.6
- Manually copy libbz2.so* into /opt/bzip2/1.0.6/lib

## Python ##
- make sure readline library is installed
- install sqlite3 development rpm or hack setup.py for the location of sqlite3 if custom install is made. This is necessary for pysqlite or jupyter notebook
- Adjust or add LDFLAGS and CPPFLAGS to include the library and the header of bzip2. This will produce _bzip2***.so 
- export LD_LIBRARY_PATH+=:/opt/libs/tcl/8.6.8/lib:/opt/libs/tk/8.6.8/lib
./configure --prefix=/opt/apps/python_custorm/3.6.3 --enable-shared --with-ensurepip=install --with-tcltk-includes="-I/opt/libs/tcl/8.6.8/include -I/opt/libs/tk/8.6.8/include" --with-tcltk-libs="-L/opt/libs/tcl/8.6.8/lib -ltcl8.6 -L/opt/libs/tk/8.6.8/lib -ltk8.6“ CPPFLAGS="-I/opt/apps/bzip2/1.0.6/include" LDFLAGS="-L/opt/apps/bzip2/1.0.6/lib" 
- make –j 20;  # check if there is any module failed to build
- make install
