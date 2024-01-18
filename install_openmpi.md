## Issues of binary file writing
- There could be conflict b/w openmpi and binary file read/writer depending on the implementation
- May use `--mca io romio341` for ver 5
- May use `--mca io romio321` for ver 4

## for version 5.xx
- --enable-mpi-cxx --enable-mpi-cxx-seek  might not be used anymore

For fortran support, may use --enable-mpi-fortran=all   
## download source
- wget https://download.open-mpi.org/release/open-mpi/v4.0/openmpi-4.0.0.tar.gz

## openucx
- ./autogen.sh; ./configure --prefix=/share/openucx/1.4.0 ; make -j40; make all; make install


## openfabric
#### it refers ucm_config_modify(), which is deprecated since openucx 1.4x. Install openucx1.3.1
- ./autogen.sh; ./configure --prefix=/share/libs/libfabric/1.6.2 --enable-mlx=/share/libs/openucx/1.3.1
- or
- ./configure --prefix=/usr/nic/libs/libfabric/intel19 CC=icc --enable-mlx=no --enable-verbs=dl --enable-rxm=dl # this will make separate libverbs-fi.so and librxm-fi.so

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
  $ ./configure --prefix=/share/mpi/ompi/400_intel18 --disable-dependency-tracking --disable-silent-rules --enable-binaries --enable-mpi-cxx --enable-mpi-cxx-seek --enable-shared --enable-openib-rdmacm --enable-fast-install --with-devel-headers --with-hwloc=internal --with-tm=/opt/pbs/ --with-verbs=auto --with-file-system=ufs+nfs+lustre --enable-oshmem --with-knem=/opt/knem-1.1.2.90mlnx3 --with-mxm=/opt/mellanox/mxm --with-platform=contrib/platform/mellanox/optimized --with-hcoll=/opt/mellanox/hcoll CC=icc CXX=icpc FC=ifort F77=ifort

## With cuda
./configure --prefix=/share/ompi/401_gcc74_cuda --with-cuda=/share/libs/cuda/10.0 --disable-dependency-tracking --disable-silent-rules --enable-binaries --enable-mpi-cxx --enable-mpi-cxx-seek --enable-shared --enable-openib-rdmacm --enable-fast-install --with-devel-headers --with-hwloc=internal --with-tm=/opt/pbs/ --with-verbs=auto --with-file-system=ufs+nfs+lustre --enable-oshmem --with-knem=/opt/knem-1.1.3.90mlnx1 --with-mxm=/opt/mellanox/mxm --with-platform=contrib/platform/mellanox/optimized --with-hcoll=/opt/mellanox/hcoll --enable-mpi1-compatibility

## At centos7. Cuda+ucx
- Download ucx 1.5.1 with cuda. Install gdr if the driver is available
  - ./configure --prefix=/share/libs/openucx/1.5.1_cuda -with-cuda=/share/libs/cuda/10.0 --with-knem=/opt/knem-1.1.3.90mlnx1 --with-mlx5-dv --with-dm
  - make -j 40 all
  - make install
-  Install openmpi with cuda + ucx_cuda
```
./configure --prefix=/share/mpi/ompi/401_gcc74_cuda_ucx151 --with-cuda=/share/libs/cuda/10.0 \
--disable-dependency-tracking --disable-silent-rules --enable-binaries --enable-mpi-cxx \
--enable-mpi-cxx-seek --enable-shared --enable-openib-rdmacm --enable-fast-install \
 --with-devel-headers --with-hwloc=internal --with-tm=/opt/pbs/ --with-verbs=auto \
 --with-lustre --enable-oshmem --with-knem=/opt/knem-1.1.3.90mlnx1 \
 --with-mxm=/opt/mellanox/mxm --with-platform=contrib/platform/mellanox/optimized \
 --with-hcoll=/opt/mellanox/hcoll --enable-mpi1-compatibility --with-ucx=/share/libs/openucx/1.5.1_cuda
```


## applying the setup of mvapich2 into openmpi
- run mpivars from mvapich2
- extract `MPIR_CVAR...` using `cut -c-99`
- export or setenv prior to running mpirun at openmpi
