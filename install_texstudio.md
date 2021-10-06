# requires qt5 or qt6

# requires poppler
- Untar
- mkdir build
- cd build
- ccmake ..
  - At ENABLE_DCTDECODER, Enter `none`
- If NSS3, TIFF, JPG libs are not available, make WITH_TIFF, WITH_JPEG, WITH_NSS3 as OFF
- Set PREFIX and save/configure/generate Makefile
- make -j 20; make install 

# texstudio
- Untar and edit texstudio.pro for PREFIX
- Update `PKG_CONFIG_PATH` with the path of pkcgconfig in poppler
- Update INCLUDE and LD_LIBRARY_PATH with Qt and poppler
- qmake texstudio.pro
- make
- make install
