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
4. Using -std=c++17
```
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
- Summary
    - a function of const argument can handle the argument of non-const
    - Function overloading of const argument vs non-const argument may not work in earlier c++ standard. Works by -std=c++11

## Clang
- `-Rpass-analysis=kernel-resource-usage` may show Spill of CGPR/VGPR
- `-save-temps` to generate assembly
- Ref: https://www.olcf.ornl.gov/wp-content/uploads/Intro_Register_pressure_ORNL_20220812_2083.pdf

## dynamic_cast
```cpp#include <iostream>
class Base
{
protected:
  int n = 3;
public:
  Base() {};
  virtual ~Base() {};
  virtual void print() {std::cout << "Base " << n << std::endl;}
};
class Drvd: public Base 
{
  public:
  Drvd() { n += 1; };
  ~Drvd() {};
  void print() {std::cout << "Drvd " << n << std::endl;}
};
int main() 
{
  // ######
  try {
    Drvd q;
    Base &s = dynamic_cast<Base&>(q);
    s.print(); // prints Drvd 4  
  } catch (std::bad_cast) {
    throw;
  }
  std::cout << "upcast using reference done\n"; 
  // ######  
  Drvd *f = new Drvd();
  Base *g = dynamic_cast<Base*>(f);
  if (g) {
    std::cout << "upcast using pointer done\n"; 
    g->print();  // prints Drvd 4
  }
  delete(f);
  // ######
  Base *x = new Base();
  Drvd *z = dynamic_cast<Drvd*>(x); // produces nullptr
  if (z) std::cout << "downcast using pointer done\n"; // never done due to nullptr
  //z->print(); segfaults. Need to use static_cast
  delete(x);
  // ######
  try {
    Drvd a; 
    Base &b = dynamic_cast<Base&>(a);
    b.print(); // prints Drvd 4
  } catch (std::bad_cast) {
    throw;
  }
  std::cout << "upcast using reference done\n"; 
  /*
  Base n; 
  Drvd &m = dynamic_cast<Drvd&>(n); // this is bad_cast. static_cast<> will work
  std::cout << "downcast using reference done\n"; 
  */
  // ######
  try {
    Drvd a; 
    Base &b = dynamic_cast<Base&>(a);
    Drvd &c = dynamic_cast<Drvd&>(b);
    c.print();  // prints Drvd 4
  } catch (std::bad_cast){
    throw;
  }
  std::cout << "dowcast using reference done\n"; 
  return 0;
  //https://stackoverflow.com/questions/11855018/c-inheritance-downcasting
}
```
