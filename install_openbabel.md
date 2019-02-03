## wxWidget
- ./configure --prefix=/opt/wxWidget/3.1.1
- make -j8 ; make install

## install eigen

# unzip source package
- mkdir build; cd build; cmake .. -DCMAKE_INSTALL_PREFIX=/opt/openbabel/2.4.1 DPYTHON_BINDINGS=ON -DBUILD_GUI=ON \
-DwxWidgets_CONFIG_EXECUTABLE=/opt/wxWidgets/3.1.1/bin/wx-config -DwxWidgets_wxrc_EXECUTABLE=/opt/wxWidgets/3.1.1/bin/wxrc\
-DPYTHON_EXECUTABLE=/opt/python/3.6.6/bin/python3 -DEIGEN2_INCLUDE_DIR=/opt/eigen/2.0.17/include/eigen2
