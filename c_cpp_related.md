## function with const argument
1. const argument
```cpp
#include <iostream>
void prnt(const int& x){    std::cout << "const int& x = " << x << std::endl; }
int main()
{
    int x = 1;
    const int z = 5;
    prnt(x);
    prnt(2);
    prnt(z);
    return 0;
}
```
- Can handle non-const argument as well
2. Regular argument
```cpp
#include <iostream>
void prnt(int& x) { std::cout <<"int& x = " << x << std::endl; }
int main()
{
    int x = 1;
    const int z = 5;
    prnt(x);
    prnt(2);
    prnt(z);
    return 0;
}
```
- Compiler breaks due to const z argument and '2'
3. Combo
```cpp
#include <iostream>
void prnt(int& x) { std::cout <<"int& x = " << x << std::endl; }
void prnt(const int& x) { std::cout << "const int& x = " << x << std::endl; }
void prnt(const int&& x){ std::cout << "const int&& x = " << x << std::endl; }
int main()
{
    int x = 1;
    const int z = 5;
    prnt(x);
    prnt(2);
    prnt(z);
    return 0;
}
```
- This yields:
```bash
$ ./a.out 
int& x = 1
const int&& x = 2
const int& x = 5
```
3.1 Combo2
```cpp
#include <iostream>
void prnt(int& x) { std::cout <<"int& x = " << x << std::endl; }
void prnt(const int& x) { std::cout << "const int& x = " << x << std::endl; }
int main()
{
    int x = 1;
    const int z = 5;
    prnt(x);
    prnt(2);
    prnt(z);
    return 0;
}
```
- This yields:
```
$ ./a.out 
int& x = 1
const int& x = 2
const int& x = 5
```
