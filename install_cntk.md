* prerequisite

-Kaldi
 # No installation step. Unzip at the install location; install apr, apr-util, subversion
 # proxy_config is necessry. Or setup https
 cd tools ; export PATH+=:/usr/nic/apps/subversion/1.9.7/bin
 export LD_LIBRARY_PATH+=:/usr/nic/apps/subversion/1.9.7/lib
  extras/check_dependencies.sh ;  make -j 8 CXX=g++-4.8
 cd ../src; ./configure --shared --use-cuda --cudatk-dir=/usr/nic/libs/cuda/8.0  --mkl-root=/usr/nic/libs/mkl/2017/mkl; make -j 20


-protobuf
 # proxy_config or https setup for firewall over-ride is required
 cd protobuf-3.1.0 ; ./autogen.sh 
 ./configure CFLAGS=-fPIC CXXFLAGS=-fPIC --disable-shared --prefix=/usr/nic/libs/protobuf/3.4
 make -j 20; make install 


-Boost
 http://www.boost.org/doc/libs/1_61_0/more/getting_started/unix-variants.html
 ./bootstrap.sh --prefix=/usr/nic/libs/boost/1.65 --with-python=/usr/nic/apps/python_data_analytics/2.7.12/bin/python --with-python-version=2.7
 ./b2 install -j 20 --python-buildid=py27


* cntk v2.2
Requires cudnn 6.0 
Ref: https://docs.microsoft.com/en-us/cognitive-toolkit/Setup-CNTK-on-Linux
No make install step. Begin install at /usr/nic/apps/  as base
git clone https://github.com/Microsoft/cntk ;cd cntk; git submodule update --init -- Source/Multiverso 
git submodule update --init -- Source/1BitSGD # for 1bit-SGD
Install swig, libzip, cub library (1.4.1 only), kaldi, boost
Edit configure script
Line 77, cudnn_check=include/cudnn.h
Line 302, local py_bin="$py_dir/$py_check${required_version:0:1}"
Line 1184, echo PYTHON${ver}_PATH=${py_paths[$ver]}/$py_check${ver:0:1} >>         $config
Edit Makefile
Line 154-155 for cudnn lib/include location

Edit Source/Common/CrossProcessMutex.h, line 131: /var/lock/ to /tmp/Ref: https://github.com/Microsoft/CNTK/issues/62
mkdir build_dbg/release -p; cd build_dbg/release
../../configure --cuda=yes --python=yes --mpi=yes --gdr=yes --with-cuda=/usr/nic/libs/cuda/8.0 --with-cub=/usr/nic/libs/cub/cub-1.4.1 --with-gdk-include=/usr/nic/libs/cuda/8.0/include --with-gdk-nvml-lib=/usr/lib64 --with-cudnn=/usr/nic/libs/cudnn/6.0/cuda_8.0/ --with-mkl=/usr/nic/libs/CNTKcustomMKL --with-kaldi=/usr/nic/libs/kaldi/kaldi-5.1 --with-opencv=/usr/nic/libs/opencv/330_p2_fastmath --with-libzip=/usr/nic/libs/libzip/1.3.0 --with-boost=/usr/nic/libs/boost/1.65 --with-protobuf=/usr/nic/libs/protobuf/3.4 --with-py-versions='27 36' --with-py27-path=/usr/nic/apps/python_data_analytics/2.7.13 --with-py36-path=/usr/nic/apps/python_data_analytics/3.6.2 --with-swig=/usr/nic/apps/swig/3.0.12 --with-mpi=/usr/nic/mpi/openmpi/1.10.7-cuda8 --1bitsgd=yes
In order to use multiple nodes/multilpe gpus, use --1bitsgd=yse
make -j 20
This step will make wheel files at  pip3 install /usr/nic/apps/cntk/build/release/python/cntk-2.2-cp36-cp36m-linux_x86_64.whl



