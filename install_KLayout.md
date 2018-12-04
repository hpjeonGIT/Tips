## install ruby first
## when coupled with qt4.8. libcurl for download from internet
./build.sh -build /opt/apps/KLayout/0.25.4  -libcurl -j 16 -with-qtbinding -qmake /opt/libs/qt/4.8/bin/qmake

## with qt 5.11
./build.sh -build /opt/apps/KLayout/0.25.6 -j 4 
