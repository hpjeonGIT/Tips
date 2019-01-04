# Prerequisite
- load the module of mpi like openmpi
- Need ply module in python ;pip3 install ply

# pybind11
- git clone https://github.com/pybind/pybind11.git
- checkout v2.2.24
- mkdir build; cd build; ccmake ..; make ; make install
- cd .. ; pip3 install .

# Python components
- git clone  dijitso, ffc, ufl, instant, fiat. Source links are found from fenics website
- then do: git checkout 2018.1.0; python3 setup.py install. This will install components into pyhon3 folder
- downgrade sympy as 1.1(pip3 install sympy==1.1)

# Dolfin
- git clone dolfin. This is a stand-alone, not python3 component
- git checkout 2018.1.0; mkdir build; cd build; ccmake .. # setup prefix, eigen3 include, boost include, python3, swig, mpi lib
- make -j 4; make install; cd ../python; 
- export pybind11_DIR=/opt/libs/pybind11/2.2.4/share/cmake/pybind11/
- export DOLFIN_DIR=/usr/nic/apps/dolfin/2018.1.0/share/dolfin/cmake/
- pip3 install .

# mshr
- git clone https://bitbucket.org/fenics-project/mshr.git
# Fenics
- git clone https://bitbucket.org/fenics-project/fenics.git
- git checkout 2018.1.0; mkdir build; cd build; 
- # adjust LD_LIBRARY_PATH and INCLUDE for boost
- ccmake .. # make CMAKE_INSTALL_PREFIX as dolfin install directory
- make -j2; make install; cd ../python ; pip3 install .
