## Ref: agner.org
- Ref find function multiversioning in gcc

## Using GCC builtin functions
- MSVC or windows/intel may use different ways
- Sample g++ code:
```cpp
#include <iostream>
void myf() {
  if (__builtin_cpu_supports("avx512f")) std::cout <<" I support avx512f\n";
  if (__builtin_cpu_supports("avx2")) std::cout <<" I support avx2\n";
  if (__builtin_cpu_supports("avx")) std::cout <<" I support avx\n";
  if (__builtin_cpu_supports("sse4.1")) std::cout <<" I support sse4.1\n";
  if (__builtin_cpu_supports("fma")) std::cout <<" I support fma\n";
}
int main() {
  myf();
  return 0;
}
```
- After build the executable, it runs at different CPU machines, yielding different results.
  - When condition is met, appropriate intrinsic functions may be implemented
- Arguments of __builtin_cpu_spports() are found at https://gcc.gnu.org/onlinedocs/gcc/x86-Built-in-Functions.html
