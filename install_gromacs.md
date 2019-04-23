- Reference: https://software.intel.com/en-us/articles/recipe-building-and-running-gromacs-on-intel-processors
- Download the latest gromacs (2019.2 as of April 2019
- Set up intel compiler, mpi, mkl
- Unpack gromacs source zip and go to main folder
- mkdir build
- cd build
- FLAGS="-xCORE-AVX512 -g -static-intel"; CFLAGS=$FLAGS CXXFLAGS=$FLAGS CMAKE_C_COMPILER=mpiicc \
  CMAKE_CXX_COMPILER=mpiicpc CC=mpiicc CXX=mpiicpc cmake .. -DBUILD_SHARED_LIBS=OFF -DGMX_FFT_LIBRARY=mkl \
  -DCMAKE_INSTALL_PREFIX=/myproject/MD -DGMX_MPI=ON -DGMX_OPENMP=ON -DGMX_CYCLE_SUBCOUNTERS=ON -DGMX_GPU=OFF \
  -DGMX_BUILD_HELP=OFF -DGMX_HWLOC=OFF -DGMX_SIMD=AVX_512 -DGMX_OPENMP_MAX_THREADS=32
  - GMX_SIMD could be AVX_512, AVX2_256, AVX_256, ... Check http://www.gromacs.org/Documentation/Installation_Instructions_5.0
- make -j 32
- Will produce build\bin\gmx_mpi. Run './build_atom/bin/gmx_mpi -version`
- For centOS6.X, -std=c++11 is not met, and will not work. Install gcc >=5, 6,7, 8, and load them with intel compiler, so intel compiler can use those newer gcc library
- Sample run command
  - Download Test Case A of Gromacs from http://www.prace-ri.eu/ueabs/
	- export OMP_NUM_THREADS=1
	- mpirun -np 8 /myproject/MD/gromacs-2019.2/build/bin/gmx_mpi mdrun -s ion_channel.tpr -maxh 0.5  -noconfout -nsteps 10000 -g logfile

