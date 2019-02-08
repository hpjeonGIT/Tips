## download source
- wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.0.tar.gz

## openucx
- ./autogen.sh; ./configure --prefix=/share/openucx/1.4.0 ; make -j40; make all; make install


## openfabric
#### it refers ucm_config_modify(), which is deprecated since openucx 1.4x. Install openucx1.3.1
- ./autogen.sh; ./configure --prefix=/share/libs/libfabric/1.6.2 --enable-mlx=/share/libs/openucx/1.3.1

## libibverbs
- configure/make/make install

## With gcc
#### update LD_LIBRARY_PATH with of openucx and openfabric. Also if /usr/lib64 has ucx libs, then let /usr/lib64 to the end of LD_LIBRARY_PATH

./configure --prefix=/usr/nic/mpi/ompi/400_gcc74 --disable-dependency-tracking --disable-silent-rules --enable-binaries \
--enable-mpi-cxx --enable-mpi-cxx-seek --enable-shared --enable-openib-rdmacm --enable-fast-install --with-devel-headers \
--with-hwloc=internal --with-tm=/opt/pbs/ --with-verbs=/usr/nic/libs/ibverbs/1.2.1 --with-file-system=ufs+nfs+lustre \
--enable-oshmem --with-knem=/opt/knem-1.1.3.90mlnx1 --with-mxm=/opt/mellanox/mxm --with-platform=contrib/platform/mellanox/optimized \
--with-hcoll=/opt/mellanox/hcoll --enable-mpi1-compatibility --with-ucx=/usr/nic/libs/openucx/1.3.1 
# --with-ofi=/share/libs/libfabric/1.6.2
#### no ofi with oenmpi - libnl libnl-3 link simultaneously and no solution at this moment: https://github.com/ofiwg/libfabric/issues/1756

## With intel
  $ ./configure --prefix=/share/mpi/ompi/400_intel18 --disable-dependency-trac
king --disable-silent-rules --enable-binaries --enable-mpi-cxx --enable-mpi-cxx-
seek --enable-shared --enable-openib-rdmacm --enable-fast-install --with-devel-h
eaders --with-hwloc=internal --with-tm=/opt/pbs/ --with-verbs=auto --with-file-s
ystem=ufs+nfs+lustre --enable-oshmem --with-knem=/opt/knem-1.1.2.90mlnx3 --with-
mxm=/opt/mellanox/mxm --with-platform=contrib/platform/mellanox/optimized --with
-hcoll=/opt/mellanox/hcoll CC=icc CXX=icpc FC=ifort F77=ifort

