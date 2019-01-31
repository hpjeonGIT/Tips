## install tcl ##
- cd unix; ./configure --prefix=/opt/libs/tcl/8.6.8; make –j 20 ; make install

## install tk ##
- cd unix; ./configure --prefix=/opt/libs/tk/8.6.8 --with-tcl=/opt/libs/tcl/8.6.8/lib; make -j 20; make install

## install bzip2 source ###

## Python ##
- make sure readline library is installed
- install sqlite3 development rpm or hack setup.py for the location of sqlite3 if custom install is made. This is necessary for pysqlite or jupyter notebook
- Adjust or add LDFLAGS and CPPFLAGS to include the library and the header of bzip2. This will produce _bzip2***.so 
./configure --prefix=/opt/apps/python_custorm/3.6.3 --enable-shared --with-ensurepip=install --with-tcltk-includes="-I/opt/libs/tcl/8.6.8/include -I/opt/libs/tk/8.6.8/include" --with-tcltk-libs="-L/opt/libs/tcl/8.6.8/lib -L/opt/libs/tk/8.6.8/lib“
make –j 20; make install
