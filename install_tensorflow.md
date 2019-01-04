# 1.12 with CUDA 9.2 in Centos7

## bazel
- download bazel 0.18.0 (the newest may not work)
- ./compile.sh --cxxopt="-D_GLIBCXX_USE_CXX11_ABI=0"
- cp output/bazel /opt/apps/bazel/0.18.0/

## TF
- export PATH+=:/opt/apps/bazel/0.18.0; export TEST_TMPDIR=/tmp/TMP_BZL
- ./configure # setup cuda, cudnn
- bazel build --config=opt --config=mkl --copt=-march=native --config=cuda --verbose_failures //tensorflow/tools/pip_package:build_pip_package
