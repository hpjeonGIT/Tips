## RHEL7/CENTOS7
- tbb libraries from yum
- upack src
- mkdir build; cd build
- configure LD_LIBRARY_PATH with mkl or netlib lapack
- ccmake ..
  - configure CMAKE_INSTALL_PREFIX
  - disable gsl
  - When lapack libraries are detected, umfpack and lapack would be ON
- make -j 22; make install

## RHEL6/CENTOS6
- TBB libraries need to be built from src
- Or use pre-built from Intel package
- Disable gsl. Enable umfpack, lapack. Confirm MKL libraries are detected in the INTEL library. Or setup lapack LD_LIBRARY_PATH
- DO NOT use bundled TBB libraries
- Find TBB from Intel suite: TBB_LIBRARY /opt/intel/2018.1/tbb/lib/intel64/gcc4.7/libtbb.so
- Match include folder, debug library (libtbb_debug.so)
- Check detailed.log after makefile is produced
```
TBB_DEBUG_LIBRARY:FILEPATH=/opt/intel/2018.1/tbb/lib/intel64/gcc4.7/libtbb_debug.so
TBB_DIR:PATH=/opt/intel/2018.1/tbb
TBB_INCLUDE_DIR:PATH=/opt/intel/2018.1/tbb/include
TBB_LIBRARY:FILEPATH=/opt/intel/2018.1/tbb/lib/intel64/gcc4.7/libtbb.so
TBB_DEBUG_LIBRARY-ADVANCED:INTERNAL=1
TBB_DEBUG_LIBRARY-MODIFIED:INTERNAL=ON
TBB_DIR-ADVANCED:INTERNAL=1
TBB_DIR-MODIFIED:INTERNAL=ON
TBB_INCLUDE_DIR-ADVANCED:INTERNAL=1
TBB_LIBRARY-ADVANCED:INTERNAL=1
TBB_LIBRARY-MODIFIED:INTERNAL=ON
```
- Even though pre-built library is for gcc4.7, it works with gcc/5.3 as well
- make -j 10
- make install
