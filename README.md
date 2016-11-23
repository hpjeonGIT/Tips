# Tips

### multi_block.xmf
... An example of distributed parallel visualization.
... Among 200x3 position data, 100x3 and 100x3 are splitted and each of two processors in paraviewl will be responsible for each block.

### installation note
libunwind: ./configure --prefix /home/hpjeon/hw/libunwind

mpiP: ./configure --prefix=/home/hpjeon/hw/mpiP --with-cc=mpicc --with-f77=mpifort
 CFLAGS=-I/home/hpjeon/hw/libunwind/include LDFLAGS=-L/home/hpjeon/hw/libunwind/
lib --enable-collective-report-default
