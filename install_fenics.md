# Prerequisite
- load the module of mpi like openmpi
- Need ply module in python ;pip3 install ply
- ##### adjust LD_LIBRARY_PATH and INCLUDE for boost

# pybind11
- git clone https://github.com/pybind/pybind11.git
- checkout v2.2.24
- mkdir build; cd build; ccmake ..; make ; make install
- cd .. ; pip3 install .

# Python components
- git clone  dijitso, ffc, ufl, instant, fiat. Source links are found from fenics website
- then do: git checkout 2018.1.0; python3 setup.py install. This will install components into pyhon3 folder
- downgrade sympy as 1.1(pip3 install sympy==1.1)

# Dolfin - boost 1.68 yielded incompatible libdolfin.so. Use 1.56
- git clone dolfin. This is a stand-alone, not python3 component
- export PETSC_DIR=/opt/libs/petsc/3.10.3
- git checkout 2018.1.0; mkdir build; cd build; ccmake .. # setup prefix, eigen3 include, boost include, python3, swig, mpi lib, petsc
#### if scotch is to be connected, it must be compiled as shared library (*.so)
- make -j 4; make install; cd ../python;  
- export pybind11_DIR=/opt/libs/pybind11/2.2.4/share/cmake/pybind11/
- export DOLFIN_DIR=/usr/nic/apps/dolfin/2018.1.0/share/dolfin/cmake/
- pip3 install .

# mshr
- git clone https://bitbucket.org/fenics-project/mshr.git
- git checkout 2018.1.0; mkdir build; cd build; 
- ccmake .. # make CMAKE_INSTALL_PREFIX as dolfin install directory
- make -j2; make install; cd ../python 
- export CPPFLAGS='-I/usr/nic/libs/boost/1.68.0_gcc485/include/' ; pip3 install .

# Fenics
- git clone https://bitbucket.org/fenics-project/fenics.git
