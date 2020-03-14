## compile source files in other locations
- Ref: http://nuclear.mutantstargoat.com/articles/make/
- Sample
```
.SUFFIXES: .o .cpp
CXX = g++
FLAGS = -std=c++14
LIB = -L/home/hpjeon/sw_local/antlr4/lib -lantlr4-runtime
INC = -I/home/hpjeon/sw_local/antlr4/include/antlr4-runtime/
TAR = a.exe
GENSRC = $(wildcard generated_cpp/*.cpp) main.cpp
OBJ = $(GENSRC:.cpp=.o) main.o
#
%.o: %.cpp
	${CXX} ${FLAGS} -o $@ -c $<
#
${TAR}: ${OBJ}
	${CXX} ${FLAGS} -o $@ $^ ${LIB}
#
clean:
	rm -rf ${GEN} main.o
```
