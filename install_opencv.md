- REF: https://docs.opencv.org/3.1.0/db/db8/tutorial_sfm_installation.html
- Install gflags with shared library option
- using gcc4.8.x yields undefined references error in opencv_test_sfm
## steps ##
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_CXX_COMPILER:FILEPATH=/opt/compiler/gcc/7.3.0/bin/g++ \
-D CMAKE_C_COMPILER:FILEPATH=/opt/compiler/gcc/7.3.0/bin/gcc \
-D CMAKE_INSTALL_PREFIX=/opt/apps/opencv/3.4 \
-D PYTHON_EXECUTABLE=/opt/apps/python_da/3.6.4/bin/python3  \
-D PYTHON_DEFAULT_EXECUTABLE=/opt/apps/python_custom/3.6.4/bin/python3 \
-D PYTHON_INCLUDE_DIRS=/opt/apps/python_custom/3.6.4/include/python3.6m \
-D PYTHON_LIBRARY=/opt/apps/python_custom/3.6.4/lib/libpython3.6m.so \
-D EIGEN_INCLUDE_PATH=/opt/libs/eigen/3.3.4/include/eigen3 \
-D GFLAGS_INLCUDE_PATH=/opt/libs/gflags/include \
-D GLOG_INCLUDE_DIR=/opt/libs/glog/include -D GLOG_LIBRARY=/opt/libs/glog/lib \
-D Glog_LIBS:FILEPATH=/opt/libs/glog/lib \
-D ANT_EXECUTABLE:FILEPATH=/opt/libs/ant/apache-ant-1.9.13/bin/ant \
-D BLAS_mkl_LIBRARY:FILEPATH=/opt/compiler/intel/18.0/mkl/lib/intel64 \
-D WITH_CUDA=OFF -D OPENCV_EXTRA_MODULES_PATH=/opt/src/apps/opencv/opencv_contrib-3.4/modules .. 
make -j 30 VERBOSE=1
make install

