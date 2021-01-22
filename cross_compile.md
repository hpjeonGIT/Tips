##
- Ref:https://stackoverflow.com/questions/47957255/cmake-linking-fortran-against-static-c-library-fails
- ex.c
```
int get_key()
{
    return 10000;
}
```
- ex1.c
```
int get_key1()
{
    return 10001;
}
```
- ex.f08
```
program main
    implicit none

    interface
        function get_key() bind(c, name='get_key')
            use iso_c_binding
            integer(kind=c_int) :: get_key
        end function get_key
    end interface

    write(*, '(i0)') get_key()
end program main
```
- For c + fortran
```
gcc -c ex.c
gcc -c ex1.c
ar cr libex.a ex.o ex1.o
gfortran fex.f08 -L. -lex
```
- For C++ + fortran
```
g++ -c ex.c
g++ -c ex1.c
ar cr libex.a ex.o ex1.o
gfortran fex.f08 -L. -lex
```
- This yields `undefined reference to 'get_key'`
- Add `extern "C"` to ex.c and ex1.c. Then repeat the process
```
extern "C" int get_key()
{
    return 10000;
}
```
- If `extern "C"` is not used, then use -static with g++ command
```
g++ -static -c ex.c
g++ -static -c ex1.c
ar cr libex.a ex.o ex1.o
gfortran fex.f08 -L. -lex
```

# In cmake, adjusting archive options
SET(CMAKE_C_ARCHIVE_CREATE "<CMAKE_AR> <LINK_FLAGS> cr <TARGET> <OBJECTS>")
SET(CMAKE_C_ARCHIVE_APPEND "<CMAKE_AR> <LINK_FLAGS> r <TARGET> <OBJECTS>")
SET(CMAKE_CXX_ARCHIVE_CREATE "<CMAKE_AR> <LINK_FLAGS> cr <TARGET> <OBJECTS>")
SET(CMAKE_CXX_ARCHIVE_APPEND "<CMAKE_AR> <LINK_FLAGS> r <TARGET> <OBJECTS>")
