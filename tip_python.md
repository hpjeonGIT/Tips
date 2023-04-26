# matplotlib backend format
- ~/.config/matplotlib/matplotlibrc
- Save as `backend : TkAgg` 

# Sample Python-C api code
```
#include "Python.h"
int main(){
  Py_Initialize();
  PyRun_SimpleString("import sys");
  PyRun_simpleString("print('hello world')");
  Py_Finalize();
}
```
- Build: gcc main.c -I/opt/python3.6/include/python3.6m $(python3-config --ldflags)
- python3-config --ldflags will produce: -L/opt/python3.6/config-3.6m-x86_64-linux-gnu  -lpython3.6m -lpthread -ldl  -lutil -lm  -Xlinker -export-dynamic -Wl,-O1 -Wl,-Bsymbolic-functions

# Reading/writing fortran binary file
- Sample fortran writer
```fortran
program test
  implicit none
  integer*4::i,j
  real*8::x,y
  chararacter*8:: header
  open(unit=10,file="input.bin",format="unformatted", action="write')
  header = "myheader"
  i=12
  j=345
  x = datan(1.d0)*4.0
  y = -dexp(1.0d0)
  write(10) header
  write(10) i,j
  write(10) x,y
  close(10)
end program test
```
- Sample Python reader/writer
```py
from scipy.io import FortranFile
import numpy as np
f = FortranFile("input.bin",'r')
header = f.read_record("a8")[0].decode('utf-8') # from byte to string
# i  = f.read_record("i4") this works but we use read_ints()
nint = f.read_ints(np.int32) #integer will be 64bit
i = nint[0]
j = nint[1]
nfloat = f.read_reals(float)
x = nfloat[0]
y = nfloat[1]
# to go back to the top of the file, f._fp.seek(0)
f.close()
# nfloat = f.read_record("f8") works as well
print(header, i,j, x,y)
### writing fortran binary
g = FortranFile("output.bin",'w')
g.write_record(str.encode(header)) # str -> byte
g.write_record(np.array([i,j]))
g.write_record(np.array([x,y]))
g.close()
```
- Sample fortran reader
```fortran
program test
  implicit none
  integer*4::i,j
  real*8:: x,y
  character*8:: header
  open(unit=10, file="ouptut.bin", form='unformatted',action='read')
  read(10) header
  read(10) i,j
  read(10) x,y
  close(10)
  print *, header, i, j, x, y
end program test
```

# Reading/writing fortran binary file with Big endian
- Sample fortran writer
```fortran
program test
  implicit none
  integer*4::i,j
  real*8::x,y
  chararacter*8:: header
  open(unit=10,file="input.bin",format="unformatted", action="write',convert='BIG_ENDIAN')
  header = "myheader"
  i=12
  j=345
  x = datan(1.d0)*4.0
  y = -dexp(1.0d0)
  write(10) header
  write(10) i,j
  write(10) x,y
  close(10)
end program test
```
- Sample Python reader/writer
```py
from scipy.io import FortranFile
import numpy as np
f = FortranFile("input.bin",'r','>u4')
header = f.read_record(">a8")[0].decode('utf-8') # from byte to string
nint = f.read_record('>i4')
i = nint[0]
j = nint[1]
nfloat = f.read_record('>f8')
x = nfloat[0]
y = nfloat[1]
# to go back to the top of the file, f._fp.seek(0)
f.close()
# nfloat = f.read_record("f8") works as well
print(header, i,j, x,y)
### writing fortran binary
g = FortranFile("output.bin",'w','>u4')
g.write_record(str.encode(header)) # str -> byte
g.write_record(np.array([i,j]))
g.write_record(np.array([x,y]))
g.close()
```
- Sample fortran reader
```fortran
program test
  implicit none
  integer*4::i,j
  real*8:: x,y
  character*8:: header
  open(unit=10, file="ouptut.bin", form='unformatted',action='read',convert='BIG_ENDIAN')
  read(10) header
  read(10) i,j
  read(10) x,y
  close(10)
  print *, header, i, j, x, y
end program test
```
