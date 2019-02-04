# Install libdrm
## configure; make; make install;
export PKG_CONFIG_PATH=/opt/libdrm/2.4.92/lib/pkgconfig

# Install llvm. Unpack source
mkdir build; cd build; ccmake ..;  # make sure BUILD_SHARED_LIBS=ON
make –j 32; make install; 
## note: Gcc/7.3.0 failed to compile. Used 4.8

# Mesa
## Ref: https://www.paraview.org/Wiki/ParaView/ParaView_And_Mesa_3D#Installing_Mesa_llvmpipe_and_swr_drivers,
./configure --prefix=/opt/mesa/18.1.1 --enable-llvm --with-llvm-prefix=/opt/compiler/llvm/6.0.0 --enable-opengl --disable-gles1 --disable-gles2   --disable-va --disable-xvmc --disable-vdpau --enable-shared-glapi --disable-texture-float --enable-gallium-llvm --enable-llvm-shared-libs --with-gallium-drivers=swrast,swr --disable-dri --with-dri-drivers=  --disable-egl --with-egl-platforms= --disable-gbm  --disable-glx --disable-osmesa --enable-gallium-osmesa;
make –j 32; make install;

## Or without llvm
#### xcb-proto
 ./configure --prefix=/usr/nic/libs/xcb/proto-1.13; make -j10; make all ;make install
export PKG_CONFIG_PATH=/usr/nic/libs/xcb/proto-1.13/lib/pkgconfig/
#### xcb
./configure --prefix=/usr/nic/libs/xcb/1.13; make -j10; make all ;make install
#### libxshmfence
./configure --prefix=/usr/nic/libs/xshmfence/1.3; make -j10; make all ;make install
### mesa
export PKG_CONFIG_PATH=/usr/nic/libs/xcb/proto-1.13/lib/pkgconfig:/usr/nic/libs/xshmfence/1.3/lib/pkgconfig/
./configure --prefix=/usr/nic/libs/mesa/18.3.3 --enable-opengl --disable-gles1 --disable-gles2   --disable-va --disable-xvmc --disable-vdpau --enable-shared-glapi --disable-texture-float --with-gallium-drivers=swrast --disable-dri --with-dri-drivers=  --disable-egl --with-egl-platforms= --disable-gbm  --disable-glx --disable-osmesa --enable-gallium-osmesa; make -j10; make all; make install
