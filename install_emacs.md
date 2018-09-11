### installing emacs ###

- C_INCLUDE_PATH=/opt/pbs/include:/opt/utilities/include:/opt/libs/gmp/6.1.2/include:/opt/libs/libunistring/0.9.10/include:/opt/libs/libtasn1/4.13/include:/opt/apps/gnutls/3.5.19/include:/opt/libs/giflib/5.1.4/include:/opt/libs/libtiff/4.0.9/include:/opt/libs/libjpeg/6b/include:/opt/apps/gnutls/3.5.19/include/gnutls
- INCLUDE=/opt/pbs/include:/opt/utilities/include:/opt/libs/gmp/6.1.2/include:/opt/libs/libunistring/0.9.10/include:/opt/libs/libtasn1/4.13/include:/opt/apps/gnutls/3.5.19/include:/opt/libs/giflib/5.1.4/include:/opt/libs/libtiff/4.0.9/include:/opt/libs/libjpeg/6b/include:/opt/apps/gnutls/3.5.19/include/gnutls
- PKG_CONFIG=/opt/apps/gnutls/3.5.19/lib/pkgconfig
- PKG_CONFIG_PATH=/opt/apps/gnutls/3.5.19/lib/pkgconfig
- LDFLAGS=-L/opt/apps/gnutls/3.5.19/lib -L/opt/libs/giflib/5.1.4/lib -L/opt/libs/libtiff/4.0.9/lib -L/opt/libs/libjpeg/6b/lib -L/opt/libs/ncurses/6.1/lib/
- LD_LIBRARY_PATH=/opt/apps/gnutls/3.5.19/lib:/opt/libs/giflib/5.1.4/lib:/opt/libs/libtiff/4.0.9/lib:/opt/libs/libjpeg/6b/lib:/opt/libs/ncurses/6.1/lib

- ./configure --prefix=/opt/apps/emacs/26.1 --with-xpm=no  --with-x-toolkit=no  --with-gnutls=no
