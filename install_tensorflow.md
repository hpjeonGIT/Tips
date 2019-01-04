# 1.12 with CUDA 9.2 in Centos7

## bazel
- download bazel 0.15.0 (the newest may not work)
- ./compile.sh --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0"
- cp output/bazel /opt/apps/bazel/0.15.0/
#### bazel >= 0.18 has issues with http_proxy


## TF
- export PATH+=:/opt/apps/bazel/0.18.0; export TEST_TMPDIR=/tmp/TMP_BZL
- ./configure # setup cuda, cudnn
- Edit third_party/gpus/crosstool/CROSSTOOL_hipcc.tpl, in the top of "cxx_flag: "-std=c++11"
    cxx_builtin_include_directory: "/usr/lib/gcc/x86_64-redhat-linux/4.8.5/include"  
    cxx_builtin_include_directory: "/lstr/applications/ava/libs/cuda/8.0/include"  

- Edit third_party/gpus/crosstool/clang/bin/crosstool_wrapper_driver_is_not_gcc.tpl, 
CPU_COMPILER = ('/usr/bin/gcc')  
GCC_HOST_COMPILER_PATH = ('/usr/bin/gcc')  

- bazel build --config=opt --config=mkl --copt=-march=native --config=cuda --verbose_failures //tensorflow/tools/pip_package:build_pip_package
