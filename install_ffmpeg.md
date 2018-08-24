## install nasm ##
- ./configure –prefix=/opt/libs/nasm/2.13.03; make –j 20; make install

## install x264 ##
- ./configure --prefix=/opt/libs/x264  --enable-shared --enable-static; make –j 20; make install

## install ffmpeg4 ##
- export PKG_CONFIG=/opt/libs/x264/lib/pkgconfig
- ./configure --prefix=/opt/libs/ffmpeg/402 --enable-yasm   --enable-libx264  --enable-gpl --enable-shared --enable-static --extra-cflags='-I/opt/libs/x264/include/' --extra-ldflags='-L/opt/libs/x264/lib -lx264'
