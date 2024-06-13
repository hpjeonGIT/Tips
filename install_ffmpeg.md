## install nasm ##
- ./configure –prefix=/opt/libs/nasm/2.13.03; make –j 20; make install

## install x264 ##
- Update PATH and LD_LIBRARY_WITH nasm/yasm
- ./configure --prefix=/opt/libs/x264  --enable-shared --enable-static; make –j 20; make install

## install ffmpeg4 ##
- export PKG_CONFIG=/opt/libs/x264/lib/pkgconfig
- ./configure --prefix=/opt/libs/ffmpeg/402 --enable-yasm   --enable-libx264  --enable-gpl --enable-shared --enable-static --extra-cflags='-I/opt/libs/x264/include/' --extra-ldflags='-L/opt/libs/x264/lib -lx264'

## ffmpeg7
- Requires SDL2, SDL2-devel. Use yum update or repo lib
- nasm as shown above
- ./configure --prefix=/opt/ffmpeg/7.0 --enable-ffplay
  - By default, ffplay is not built
