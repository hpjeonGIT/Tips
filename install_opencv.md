export ANT_HOME=/opt/libs/ant/apache-ant-1.9.9
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/opt/apps/opencv/3.4 \
-D PYTHON_EXECUTABLE=/opt/apps/python/3.6.1/bin/python3  \
-D PYTHON_DEFAULT_EXECUTABLE=/opt/apps/python/3.6.1/bin/python3 \
-D PYTHON_INCLUDE_DIRS=/opt/apps/python/3.6.1/include/python3.6m \
-D PYTHON_LIBRARY=/opt/apps/python/3.6.1/lib/libpython3.6m.so \
-D WITH_CUDA=OFF -D OPENCV_EXTRA_MODULES_PATH=/opt/src/apps/opencv/opencv_contrib-3.4/modules .. 
make -j 16 VERBOSE=1
make install

