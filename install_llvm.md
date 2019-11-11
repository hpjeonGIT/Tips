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
