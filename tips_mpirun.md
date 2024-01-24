# In intel mpi
- Use -genv I_MPI_DEBUG 5 to find details of communication
- Use -genv MPI_IB_PORT_GID=fe80:0000:0000:0000 (<- this is GID from ibv_devinfo  -v) when there are issues from subnet mask
- export MPI_IB_PKEY="0xffff" when there are multiple pkeys : used for abaqus 2019
- For OFA, debug option is FI_LOG_LEVEL=debug. Use fi_info for find available fi
- Ex: mpirun -n $NPROCS -genv MPI_IB_PORT_GID="fe80:0000:0000:0000"  -genv MPI_IB_PKEY="0xffff" -genv I_MPI_DEBUG=5 -genv I_MPI_FABRICS="shm:ofa" -genv I_MPI_INFO_NUMA_NODE_MAP=mlx5_0:0 ./mpiBenc
- using ibv_devinfo, ib port can be confirmed.
- Collective call fine control:
- export I_MPI_ADJUST_ALLGATHER=1
- export I_MPI_ADJUST_ALLGATHERV=1
- export I_MPI_ADJUST_ALLREDUCE=1
- export I_MPI_ADJUST_ALLTOALL=1
- export I_MPI_ADJUST_ALLTOALLV=2
- export I_MPI_ADJUST_GATHER=1
- export I_MPI_ADJUST_GATHERV=1

# In openmpi
- Recompile with ucx. This helped OpenCA to run
- export OMPI_MCA_coll=^fca              # disable FCA for collective MPI routines
- export OMPI_MCA_coll_hcoll_enable=1    # enable HCOLL for collective MPI routines
- export OMPI_MCA_coll_hcoll_priority=95
- export OMPI_MCA_coll_hcoll_np=8        # use HCOLL for all communications with more than 8 tasks
- export HCOLL_MAIN_IB=mlx5_0:0
- export HCOLL_ENABLE_MCAST=1
- export HCOLL_ENABLE_MCAST_ALL=1

# when some nodes miss files or modules
- Write a 3 line python script
```py
import socket
import os
print(socket.gethostname(),os.path.isfile("/opt/libfabric/some_version"))
```
- Run the above script then we can narrow down which nodes don't have the file
- mpirun python3 host_check.py
- srun python3 host_check.py
