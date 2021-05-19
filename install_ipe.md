# IPE Latex Drawing tool (ipe.otfried.org)
- Prerequisite at RHEL7/CENTOS7
  - Needs gcc with `-std=c++11`
  - sudo yum install libgsl-dev
  - sudo yum install qt5-qbase-devel
- Installing libspiro
  - RPM (from Fedora) installation is not recommended
  - Download source from github.com/fonforge/libspiro
```
autoreconf -i
./configure --prefix=/opt/libspiro
make -j10
make install
```
- Installing lua 5.4
  - Unpack source zip file and edit src/Makefile, adding `-fPIC`
  - `make; make install INSTALL_TOP=/opt/lua/5.4.3`
- IPE
```
export PKG_CONFIG_PATH=/opt/libspiro/lib/pkgconfig
export MOC=/usr/lib64/qt5/bin/moc
export LUA_CFLAGS="-I/opt/lua/5.4.3/include"
export LUA_LIBS=/opt/lua/5.4.3/lib/liblua.a
export CXXFLAGS="-std=c++14"
export QT_SELECT=5
export QTDIR=/usr/lib64/qt5
cd src
make IPEPREFIX=/opt/ipe/7.2.24 CXX=/opt/gcc/5.3/bin/g++ CC=/opt/gcc/5.3/bin/gcc
make install IPEPREFIX=/opt/ipe/7.2.24
```
  - There might be error message during the compiling but can be ignored
