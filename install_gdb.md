- similar to gcc, mpc, mpf, gmp is necessary
- But using --with-gmp/--with-mpfr/--with-mpc may not work, yielding libgmp is not found or inusable.
- Instead, use --with-libgmp-prefix/--with-libmpfr-prefix/--with-libmpc-prefix
- ./configure --prefix=/opt/gdb/13.2 --with-libgmp-prefix=/opt/gmp/6.1.1  --with-libmpfr-prefix=/opt/mpfr/3.1.1 --with-libgmp-prefix=/opt/gmp/1.0.2
- make -j 20
- make all
- make install


## since version 14:
- ./configure --prefix=/opt/gdb/14.1 --with-gmp=/opt/gmp/6.1.1  --with-mpfr=/opt/mpfr/3.1.1 --with-gmp=/opt/gmp/1.0.2 --enable-tui
- To enable TUI, libncurses library is required.
- If ncurses is not installed at default location (/usr or /usr/local), gdb may not be able to find ncurses components
  - In the configure step, use CFLAGS and CXX flags as CFLAGS="-L/opt/ncurses/6.4/lib -I/opt/ncurses/6.4/include"

