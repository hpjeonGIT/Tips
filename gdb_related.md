## How to avoid optimized out at variable evaluation
- Sample cpp code
```cpp
#include <iostream>
#include <cmath>
int main()
{
    int x=1;
    std::cin >> x;
    int y=0;
    if (x==1 || x==2)
    {
	y = 3;
    } else
    {
	y = 4;
    }
    x = 2;
    int z = 3;
    if (x==1 || x==2)
    {
	z = 13;
    } else
    {
	z = 14;
    }
     std::cout << z << std::endl;
    return 0;
}
```
- By the end of the code, -O3 -g will yield optimized out for variable y
```bash
gdb-peda$ p y
$1 = <optimized out>
```
  - -O1 yields same results
- Applying -O0 will show the value of y but in -O3 state, we can use `volatile int y=0;`
  - This yields:
```bash
gdb-peda$ p y
$1 = 0x4
```
