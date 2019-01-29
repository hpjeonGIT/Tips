# Prerequisite
- Install hdf5 with parallel io options
- Install netcdf-c
- Install netcdf-fortran

# Get the source code
- Copy casup.f90 to cgca.f90
- Edit module casup to module cgca
- Add casup.f90 into SRC list in Makefile.*

# Compile/Run 
- make –f Makefile-h5pfc
- mkdir ~/lib; mkdir ~/include
- make install
- cd tests; make –f Makefile-h5pfc

# I_MPI_FABRICS configuration
- Shm: shared memory for intra-node
- Tcp: tcp for ethernet or infiniband
- Ofi: OpenFabrics Interface
- Ofa: Open Fabric alliances
- dapl
- Use I_MPI_FABRICS=shm:ofa
# I_MPI_DEBUG
- 2: debug level

# Issues in cgca_pswci4()
from: CALL h5dwrite_f(dset_id, H5T_NATIVE_INTEGER, coarray(1:arrsize(1),    &
1:arrsize(2), 1:arrsize(3), stype), dimsf, ierr,             &

 to: tmp(1:arrsize(1),1:arrsize(2),1:arrsize(3)) = &                                
       coarray(:arrsize(1),1:arrsize(2),1:arrsize(3), stype) 
…
 CALL h5dwrite_f(dset_id, H5T_NATIVE_INTEGER, tmp(:,:,:), dimsf, ierr,  &
       file_space_id = filespace, mem_space_id = memspace,          &     
       xfer_prp = plist_id)                                               




# Sample PBS script
#!/bin/zsh                                                                               
#PBS -l select=16:ncpus=32:mpiprocs=32:ompthreads=1:mem=100gb                            
#PBS -l walltime=10:00:00                                                                
#PBS -q @server
#PBS -N casup                                                                            
cd $PBS_O_WORKDIR
export NNODES=`sort $PBS_NODEFILE | uniq | wc -l`
export NPROCS=`wc -l < $PBS_NODEFILE`            
. /etc/profile.d/modules.sh
module load netcdf/f4.4.4_ifort18 netcdf/c4.6.1_intel18  hdf5/1.10.1_intel18
cd $PBS_O_WORKDIR

cat $PBS_NODEFILE > hosts
echo '-machinefile hosts -n ' $NPROCS ' -genvall -genv I_MPI_FABRICS=shm:ofa ./jeonb.x’ >  xx14.conf

make -f Makefile-jeonb clean
make -f Makefile-jeonb
lfs setstripe -S 1m -c 8 .
(time  ./jeonb.x ) |& tee $NPROCS.log.txt
lfs setstripe -S 1m -c 1 .


