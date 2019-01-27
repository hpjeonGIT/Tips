## download source
- wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.0.tar.gz

## With gcc
 ./configure --prefix=/share/mpi/ompi/300_gcc48 --disable-dependency-tracki
ng --disable-silent-rules --enable-binaries --enable-mpi-cxx --enable-mpi-cxx-se
ek --enable-shared --enable-openib-rdmacm --enable-fast-install --with-devel-hea
ders --with-hwloc=internal --with-tm=/opt/pbs/ --with-verbs=auto --with-file-sys
tem=ufs+nfs+lustre --enable-oshmem --with-knem=/opt/knem-1.1.2.90mlnx3 --with-mx
m=/opt/mellanox/mxm --with-platform=contrib/platform/mellanox/optimized --with-h
coll=/opt/mellanox/hcoll

## With intel
  $ ./configure --prefix=/share/mpi/ompi/400_intel18 --disable-dependency-trac
king --disable-silent-rules --enable-binaries --enable-mpi-cxx --enable-mpi-cxx-
seek --enable-shared --enable-openib-rdmacm --enable-fast-install --with-devel-h
eaders --with-hwloc=internal --with-tm=/opt/pbs/ --with-verbs=auto --with-file-s
ystem=ufs+nfs+lustre --enable-oshmem --with-knem=/opt/knem-1.1.2.90mlnx3 --with-
mxm=/opt/mellanox/mxm --with-platform=contrib/platform/mellanox/optimized --with
-hcoll=/opt/mellanox/hcoll CC=icc CXX=icpc FC=ifort F77=ifort

