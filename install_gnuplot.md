# Install libGD
git clone https://github.com/libgd/libgd.git  
git checkout gd-2.2.5  
mkdir build; cd build ; ccmake ..; make -j 32 ; make install

# Install GNUPLOT
git clone git clone https://git.code.sf.net/p/gnuplot/gnuplot-main gnuplot-gnuplot-main  
git checkout 5.2.6
- git source is missing configure script. Download gz version  
./configure --prefix=/opt/apps/gnuplot/5.2.6 --with-cairo --with-latex --with-gd=/opt/libs/libgd/2.2.5   
make -j 32; make install

