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
    x = 0;
    uint64_t z = 8, y;
    for (size_t j =0;j < 66;j++) {
	x = 0;
	y = pow(2,j);
	x |= y;
	std::cout << j<< " " << y << " " << ((x & y) > 0) << " " << ((x & z) > 0) << std::endl;
    }
        
    return 0;
    
}
```
- from j=0 to j=63, this book-keeping works. Note j=64 or larger doesn't work anymore
```
0 1 1 0
1 2 1 0
2 4 1 0
3 8 1 1
4 16 1 0
5 32 1 0
6 64 1 0
7 128 1 0
8 256 1 0
9 512 1 0
10 1024 1 0
11 2048 1 0
12 4096 1 0
13 8192 1 0
14 16384 1 0
15 32768 1 0
16 65536 1 0
17 131072 1 0
18 262144 1 0
19 524288 1 0
20 1048576 1 0
21 2097152 1 0
22 4194304 1 0
23 8388608 1 0
24 16777216 1 0
25 33554432 1 0
26 67108864 1 0
27 134217728 1 0
28 268435456 1 0
29 536870912 1 0
30 1073741824 1 0
31 2147483648 1 0
32 4294967296 1 0
33 8589934592 1 0
34 17179869184 1 0
35 34359738368 1 0
36 68719476736 1 0
37 137438953472 1 0
38 274877906944 1 0
39 549755813888 1 0
40 1099511627776 1 0
41 2199023255552 1 0
42 4398046511104 1 0
43 8796093022208 1 0
44 17592186044416 1 0
45 35184372088832 1 0
46 70368744177664 1 0
47 140737488355328 1 0
48 281474976710656 1 0
49 562949953421312 1 0
50 1125899906842624 1 0
51 2251799813685248 1 0
52 4503599627370496 1 0
53 9007199254740992 1 0
54 18014398509481984 1 0
55 36028797018963968 1 0
56 72057594037927936 1 0
57 144115188075855872 1 0
58 288230376151711744 1 0
59 576460752303423488 1 0
60 1152921504606846976 1 0
61 2305843009213693952 1 0
62 4611686018427387904 1 0
63 9223372036854775808 1 0
64 0 0 0
65 0 0 0
```

