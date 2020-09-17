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
