## php source 8.1 on rhel8.X
- source install libxml and sqlite3
- Update PKG_CONFIG_PATH using /lib/pkgconfig folder of them
- yum install libcurl-devel libdb-devel oniguruma-devel libzip-devel
- Unpack php 8.1 source
- ./configure --prefix=/opt/php/8.1.7 --disable-cgi --with-zlib --with-gettext --with-sqlite3 --enable-mbstring --enable-calendar \
-  --with-curl=/usr/lib --enable-soap --enable-bcmath --with-openssl --enable-ftp --with-libdir=lib64 --with-keroberos --enable-gd --with-zip
-  make -j 20
-  make install
