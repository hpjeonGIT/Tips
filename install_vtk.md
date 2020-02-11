# standard cmake
- `mkdir build; cd build; ccmake ..`
  - For RHEL7, opengl2.1 might not be able to run regular VTK library
  - Recompile with `VTK_RENDERING_BACKEND=OpenGL` while the default is opengl2
- `make -j 10; make install`
- Copy $PREFIX/lib/python3.x/site-packages/vtk to $PYTHONE_HOME/lib/python3.x/site-packages
