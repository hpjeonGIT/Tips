mkdir build
cd build
# using gcc/7.3 due to avx512 support
../configure --shared -b 64 -D c -DPentiumCPS=2400 --prefix=/opt/libs/atlas/3.10.3 --with-netlib-lapack-tarfile=/opt/src/libs/atlas/lapack-3.8.0.tar.gz
make build # -j doesn't work. May take a couple of hours
make check ; make ptcheck; make time make install
