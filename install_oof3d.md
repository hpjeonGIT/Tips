- Edit SRC/common/DIR.py and delete pixelsetboundary.C and .H
- Edit SRC/common/IO/GUI/DIR.py for non detected source files
- Edit SRC/common/tostrring.h, SRC/engine/cskeleton2.h, SRC/SWIG3D/engine/fieldindexcmodule.C, <strstream.h> into <strstream>
- Requires python2.7 with pygtk support

### export MKLROOT=/opt/intel/18.0/mkl
### export LD_LIBRARY_PATH+=:/opt/intel/18.0/mkl/lib/intel64
### python setup.py build --blas-link-args="-fopenmp -I${MKLROOT}/include -L${MKLROOT}/lib/intel64 -lmkl_gf_lp64  -lmkl_gnu_thread -ldl" --blas-libraries="mkl_core" --enable-openmp  --3D --vtkdir=/opt/vtk/5.10.1_gcc447
- Disable blas test
### python setup.py install --prefix=/opt/oof3d/3.1.2 --enable-openmp  --3D --vtkdir=/opt/vtk/5.10.1_gcc447
- In environmental variables, PYTHONPATH as $APP_ROOT/lib/python2.7/site-packages:/opt/oof3d/3.1.2/lib/python2.7/site-packages
