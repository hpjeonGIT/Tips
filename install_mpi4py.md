## Recommended install using on-line pip
- pip install mpi4py

## Offline install
1. edit mpi.cfg then python3 setup.py install -> not working
2. mkdir build; cd build; ccmake ..
    - If cmake or make process conflicts with anaconda3 library like:
```
ccmake: /home/hpjeon/sw_local/anaconda3/2023.03/lib/libtinfo.so.6: no version information available (required by ccmake)
ccmake: /home/hpjeon/sw_local/anaconda3/2023.03/lib/libncurses.so.6: no version information available (required by ccmake)
```
    - Manually adjust LD_LIBRARY_PATH to remove the lib location of anaconda3
    - May use gcc/g++ then mpiexec location from existing mpi library
3. Update the PYTHONPATH to load mpi4py
- hello.py 
```py
from mpi4py import MPI
import sys

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

sys.stdout.write(
    "Hello, World! I am process %d of %d on %s.\n"
    % (rank, size, name))
```
- Demo:
```bash
$ mpirun -n 3 python3 hello.py 
Hello, World! I am process 2 of 3 on hakuneMini.
Hello, World! I am process 0 of 3 on hakuneMini.
Hello, World! I am process 1 of 3 on hakuneMini.
```
