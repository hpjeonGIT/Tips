# objective
- Track five variables if their status has been changed or not
- To track five variables, additional five number might be necessary but actually can be done with one variable
- Assume a 64bit integer number. Initially x = 0
  - In 2bit, it would be 00000
- When a0 changes, we may change x as 00001
- When a2 changes, we may change x as 00101
- Now x = 0101 and we know:
```
00101
----^ : a0 is changed
--^:    a2 is changed
```
- We may find a1, a3, a4 are not changed.
- Corresponding C++ code is shown below.

```c++
#include <iostream>

enum metric {
    a0 = 1,
    a1 = 2,
    a2 = 4,
    a3 = 8,
    a4 = 16
};

int main(int argc, char** argv) {

    uint64_t x = 0; // 0000
    // Assume that a0 is changed
    x |= a0;       //  0001

    // Assume that a2 is changed
    x |= a2;        //  0101

    std::cout << (x & a0)  << std::endl;
    std::cout << (x & a1)  << std::endl;
    std::cout << (x & a2)  << std::endl;  
    std::cout << (x & a3)  << std::endl;
    std::cout << (x & a4)  << std::endl;
        
    return 0;
    
}
```
