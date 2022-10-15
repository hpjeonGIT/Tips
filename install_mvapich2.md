# mvapich on a local computer (no IB) using gcc
- mkdir bulid; cd build ; ../configure --prefix=/opt/2.3.1 --disable-mcast
- mkdir bulid; cd build ; ../configure --prefix=/opt/2.3.1 CC=.../gcc CXX=../g++ --disable-mcast
- Using --with-device=ch3:sock could be 2-3x slower

# mvapich on a local computer (no IB) using llvm
- mkdir bulid; cd build ; ../configure --prefix=/opt/2.3.1_llvm90 CC=/opt/llvm/9.0_gcc91/bin/clang CXX=/opt/llvm/9.0_gcc91/bin/clang++ --disable-mcast

# mvapich/2.3.6 on RHEL6 using gcc/10.3
- Prerequisite
  - Install autoconf and add bin folder to $PATH
  - Install texinfo and add bin folder to $PATH
    - If tar yields `tar: value XXXXXX out of uid_t range 0..2097151`
    - export TAR_OPTIONS="--owner=0 group=0 --numeric-owner"
  - May need automake 1.15
    - Can be installed on Lustre but Config/build at serial disk might be necessary
- mvapich/2.3.6
  - Can be installed on Lustre but Config/build at serial disk might be necessary
  - For gfortran/10.3
    - export FFLAGS="-w -fallow-argument-mismatch -O2"
  - mkdir build ; cd build
  - ../configure --prefix=/opt/mvapich/2.3.6_gcc103 --with-slurm=... --with-ibverbs-lib=/usr/lib64 --with-hcoll=... --with-mxm=... --with-fca=... --with-knem=... --with-file-system=lustre --with-device=ch3:mrail --with-rdma=gen2 --with-ib-include=/usr/include/infiniband --with-ib-libpath=/usr/lib64 --disable-rdma-cm CC=/opt/gcc/10.3/bin/gcc CXX=/opt/gcc/10.3/bin/g++ FC=/opt/gcc10.3/bin/gfortran F77=/opt/gcc10.3/bin/gfortran
  - make -j 16
- If an error message of `tools/bootstrap/src/bsci_init.c:17:266: error: 'HYDT_bsci_launcher_pbs_init' undeclared here ...`
  - Add --with-hydra-bss="user,ssh,rsh,fork,slurm,sge,manual,persist", excluding pbs for bss list

## 2.3.7 with slingshot
- For slingshot10, use 2.3.7, not 3.0a
- Or make sure to use `--with-device=ch3:mrail --with-rdma=gen2`
- Use `--with-ofi`, `--with-ofi-include`, `--with-ofi-lib` pointing cray ofi libs
- Append `FFLAGS-fallow-argument-mismatch FCFLAGS=-fallow-argument-mismatch` for gfortran
- For more than 32767 ranks, needs `--with-ch3-rank-bits=32`
