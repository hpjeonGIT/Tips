## How to edit smspec/unsmry files
- They are Fortran binaries made by Schlumberger Eclipse
- libecl is shared on github (developers are not from Schlumberger)
  - https://github.com/equinor/libecl
  - Install steps
    - Unzip
    - `mkdir build`
    - `cd build`
    - `ccmake ..`
    - Enable Python binding (supports 2.7 only at 2019)
    - Enable BUILD_APPLICATIONS=ON
    - `make -j 10`
    - `make install`
  - In the intall location, bin/convert.x is found
  - `convert.x a.smspec` yields a.fsmspec, which is ASCII
  - `convert.x a.unsmry` yields a.funsmry, which is ASCII
  - After editing, `convert.x b.funsmry` yields b.unsmry, which is BINARY

# Python binding 
- Enable Python binding when install from cmake
- If Python binding is done, then install setuptools-41.2.0 or newer, setuptools_scm-3.3.3 or newer or cwrap-1.6.1 or newer
  - `unzip; python setup.py install --user`
  - This will install python package at ~/.local
