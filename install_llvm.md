## Version 14.0
- Download the entire project from github
  - clang, flang, openmp are already enclosed
- mkdir build; cd build; ccmake -S ../llvm
- When running cmake or ccmake, configure LLVM_ENABLE_PROJECTS as clang;clang-tools-extra;compiler-rt;flang;openmp;lldb
  - Full list is: clang;clang-tools-extra;compiler-rt;debuginfo-tests;libc;libclc;libcxx;libcxxabi;libunwind;lld;lldb;openmp;parallel-libs;polly;pstl
- Enable SHARED_LIBS ON
- make -j 20; make install
- may need `-stdlib=libc++` as CXX flags for application

## Version 11.0
- Not from https://releases.llvm.org/download.html but download from https://github.com/llvm/llvm-project, as the entire project
- clang, flang, openmp are already enclosed
- When running cmake or ccmake, configure LLVM_ENABLE_PROJECTS as clang;clang-tools-extra;compiler-rt;flang;openmp
  - Full list is: clang;clang-tools-extra;compiler-rt;debuginfo-tests;libc;libclc;libcxx;libcxxabi;libunwind;lld;lldb;openmp;parallel-libs;polly;pstl
- Enable SHARED_LIBS ON


## Clang would be  built with LLVM, putting clang source at tools/clang of LLVM src tree
- GCC> 7 is not supported for openmp
  - Let's us gcc 7.4
- tools/clang #https://github.com/llvm-mirror/clang
- tools/openmp #https://github.com/llvm-mirror/openmp
- mkdir build; cd build; ccmake ..
  - LLVM_TOOL_OPENMP_BUILD=ON
  - LLVM_EXTERNAL_OPENMP_SOURCE_DIR=....
  - SHARED_LIBS ON
- When omp is coupled, clang -fopenmp must be able to compile without header/lib locations
- `clang -v` will show the gcc-toolchain as the system default. To couple with specific gcc, use `clang --gcc-toolchain=/opt/gcc/5.3 -v`
- In order to use `#include <experimental/filesystem>`, use command `clang++ -std=c++14 fs_wrapper.cpp --gcc-toolchain=/opt/gcc/7.4 -lstdc++fs`
	- `-std=c++17` may not support `<filesystem>` yet. May work with `<experimental/filesystem>`


## FLang  
  
2. Bvuilding openmp
	- ccmake..
		- enable shared lib, parallel lib, and assign openmp source location
2. Flang is built as off-tree, as a stand-alone, after LLVM/clang is built
- install flang-driver first: 
- build openmp 
- build flang
- unpack llvm src
- unpack clang src at llvm/tools/clang
  - Clang may need gcc > 5.0
- unpack flang src at llvm/tools/flang
  - Flang may need gcc > 7.0
- mkdir build; cd build; ccmake ..;
  - BUILD_SHARED_LIBS=ON
  - LLVM_TOOL_OPENMP_BUILD:BOOL=ON
  - FLANG_LIBOMP               	llvm-release_90/tools/flang/runtime/flangrti
  - LIBPGMATH                   llvm-release_90/tools/flan/runtime/flangrti
- make # make -j 10 didn't work at 2019 version of flang
