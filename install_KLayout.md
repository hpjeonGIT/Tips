## install ruby first
## when coupled with qt4.8. libcurl for download from internet
./build.sh -build /opt/apps/KLayout/0.25.4  -libcurl -j 16 -with-qtbinding -qmake /opt/libs/qt/4.8/bin/qmake

## if libcurl header or library is required
- edit qt/X.X/mkspecs/common/linux.conf
- QMAKE_INCDIR          = /usr/nic/apps/curl/7.61.1/include
- QQMAKE_LIBS              = -L/usr/nic/apps/curl/7.61.1/lib/


## with qt 5.11 - not working
./build.sh -build /opt/apps/KLayout/0.25.6 -j 4 
