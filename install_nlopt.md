# Install libtool/gmp
Standard configure/make/make install

# Install guile
./configure --prefix=/usr/nic/apps/guile/2.2.4_gcc48 --with-libltdl-prefix=/usr/nic/libs/libtool/2.4.6/ \
CPPFLAGS="-I/usr/nic/libs/libtool/2.4.6/include -I/usr/nic/libs/gmp/6.1.2/include/ -I/usr/nic/libs/libunistring/0.9.10/include/" \
LDFLAGS="-L/usr/nic/libs/libtool/2.4.6/lib -L/usr/nic/libs/gmp/6.1.2/lib -L/usr/nic/libs/libunistring/0.9.10/lib/"


# NLOPT
## load python environment if necessary
mkdir build; cd build; ccmake .. # configure python path, guile, matlab header, swigle, 
