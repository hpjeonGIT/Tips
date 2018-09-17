## install tcl ##
- cd unix; ./configure --prefix=/opt/libs/tcl/8.6.8; make –j 20 ; make install

## install tk ##
- cd unix; ./configure --prefix=/opt/libs/tk/8.6.8 --with-tcl=/opt/libs/tcl/8.6.8/lib; make -j 20; make install

## Python ##
- make sure readline library is installed
./configure --prefix=/opt/apps/python_custorm/3.6.3 --enable-shared --with-ensurepip=install --with-tcltk-includes="-I/opt/libs/tcl/8.6.8/include -I/opt/libs/tk/8.6.8/include" --with-tcltk-libs="-L/opt/libs/tcl/8.6.8/lib -L/opt/libs/tk/8.6.8/lib“
make –j 20; make install
