git clone https://github.com/LLNL/ior.git  
./bootstrap ; ./configure --prefix=... ; make -j 4 ; make install

Ref: https://media.readthedocs.org/pdf/ior/latest/ior.pdf  
mpirun -n 2 /usr/local/bin/ior -t 1m -b 16m -s 16 -F
