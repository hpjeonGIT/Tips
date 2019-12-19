# mpich is from ANL

## Basic installation. For tcp or ethernet connection with intel compiler
- mkdir build; cd build
- ../configure -prefix=/share/mpich/3.3_intel18 --enable-shared CC=icc CXX=icpc FC=ifort F77=ifort				
- make -j 20; make install

## For infiniband
- mkdir build; cd build;
- ../configure -prefix=/share/mpich/3.3_intel18_ucx --with-ibverbs-include=/usr/include/infiniband \
--with-iverbs-lib=/usr/lib64 --with-hcoll=/opt/mellanox/hcoll --with-mxm=/opt/mellanox/mxm \
--with-knem=/opt/knem-1.1.2.90mlnx1 --enable-shared CC=icc CXX=icpc FC=ifort F77=ifort --with-device=ch4:ucx				
- make -j 20 ; make install

## Some discussion
- `--with-slum` might not be recommeded in the SLURM environment
- In infiniband-network with iverbs, using `--with-device=ch3:nemesis:mxm` may not work. MPI_Finalize crashes. Use UCX. UCX is contained in the mpich 3.3.x source package
