# mvapich on a local computer (no IB) using gcc
- mkdir bulid; cd build ; ../configure --prefix=/opt/2.3.1 --disable-mcast
- mkdir bulid; cd build ; ../configure --prefix=/opt/2.3.1 CC=.../gcc CXX=../g++ --disable-mcast

# mvapich on a local computer (no IB) using llvm
- mkdir bulid; cd build ; ../configure --prefix=/opt/2.3.1_llvm90 CC=/opt/llvm/9.0_gcc91/bin/clang CXX=/opt/llvm/9.0_gcc91/bin/clang++ --disable-mcast
