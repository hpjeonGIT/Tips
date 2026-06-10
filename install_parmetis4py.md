SRC: https://github.com/florianwechsung/parmetis4py
  - It is not maintained more than 8 years as of 2026
- Even though Petsc is shown as required but not necessary for install
- Just install parmetis and mpi4py, coupling them with the same MPI library
- Edit setup.py to find parmetis libs and mpi lib
- `Python3 setup.py build_ext -i`
- Then setup PYTHONPATH in module file to load the produced library
- `mpirun -n 3 python3 tests/test.py`
