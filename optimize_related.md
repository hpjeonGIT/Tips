# when clang/clang++ cannot deduce function matching
- Disable optimization using `#pragma clang optimize off` in the top of the function
- Ref: https://gcc.gnu.org/onlinedocs/gcc/Function-Specific-Option-Pragmas.html

# using attribute
- `#pragma gcc optimize off` may not work well
- `bool __attribute__((optimize("O0"))) myfunc()` will work
