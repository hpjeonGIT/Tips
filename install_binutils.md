# RHEL6 or CENTOS6
- If the assembler (`as -v`) version is too old, it may not be able to generate avx2 executable : `no such instruction: v2iXXXXX`
- Install GNU binutils
  - `configure --prefix=< > ; make; make install`
  - If `makeinfo comand not found` error message appears, suppress makeinfo by : `make MAKINFO=true; make install MAKEINFO=true`
