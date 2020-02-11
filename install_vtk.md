# standard cmake
- `mkdir build; cd build; ccmake ..`
  - For RHEL7, opengl2.1 might not be able to run regular VTK library
  - Use 7.1.1
    - Set `VTK_RENDERING_BACKEND=OpenGL` while the default is OpenGL2
  - wrap with python or conda when available
  - Choose python version as 2 or 3
- `make -j 10; make install`
- Copy $PREFIX/lib/python3.x/site-packages/vtk to $PYTHONE_HOME/lib/python3.x/site-packages
