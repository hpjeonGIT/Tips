### C/C++
- `__FILE__`, `__LINE__`, `__FUNC__` : macros for file name, line number, and functionn name
- Ref: https://gcc.gnu.org/onlinedocs/cpp/Standard-Predefined-Macros.html
- 
### Fortran
- `__FILE__`, `__LINE__`, `__DATE__`, `__TIME__`
- gfortran needs -cpp option
- ifort needs -fpp option

### Python
- `__file__`
- `__name__` for function name
```py
def func():
    print(func.__name__)
```
