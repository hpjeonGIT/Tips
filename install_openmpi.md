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
- Build with cuda-aware mpi
  - Using --with-cuda might not be enough
  - Need to use gdr_copy and ucx. Then couple ucx with openmpi build
  - Ref: https://www-lb.open-mpi.org/faq/?category=buildcuda
  - Steps
    - Build gdr_copy
    - Build ucx with coupling of gdr_copy
    - Build openmpi with --with-cuda and --with-ucx
  - Make sure using ompi_info --all |grep -in cuda_support
  - As of March 2024, openmpi 5.0.1 seems not working with cuda build. cuda_support yields off. Use 4.1.4

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

## openmpi 5.0.3 with UCX + CUDA
- gdrcopy: make prefix=... CUDA=... all install
- UCX
  - Needs autoconfig/automake/libtool
  - ./autogen.sh
  - When failed, run libtoolize then autogen.sh again
  - ./configure --prefix=... --with-knem=... --with-grdcopy=... --with-verbs=/usr --with-cuda=...
  - make -j20; make install
  - After installation, check `./bin/ucx_info -d |grep Transport` and confirm mlx5 or verbs
- openmpi 5.0.3
- `--lib-cuda-libdir` must point the dir containing libcuda.so
- ./autogen.pl --force
- ./configure --prefix=... --with-cuda=/usr/local/cuda --with-cuda-libdir=/usr/local/cuda/targets/x86_64-linux/lib/stubs --disable-dependency-tracking --disable-silent-rules --enable-shared --enable-fast-install --with-devel-headers --with-hwloc=internal --with-platform=contrib/platform/optimized --with-knem=... --with-hcoll=... --with-ucx=... --enable-mpi-compatibility CC=gcc CXX=g++ F77=gfortran F90=gfortran

## For version 5.0.* + UCX + CUDA + Mellanox
- When there is a warning message: UCP deosn not support MPI_THREAD_MULTIPLE
  - When building ucx, add the option of --enable_mt
  - In the application code, feed MPI_THREAD_FUNNELED into MPI_Init()
- Crash is found at MPI_Allreduce() -> mca_coll_hcoll_allreduce()
  - No solution is found yet
  - --mca coll ^hcoll will skip hcoll 
