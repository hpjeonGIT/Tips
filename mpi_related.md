## boolean in cpp
- MPI_Bcast(v.data(),3,MPI_INT,0,MPI_COMM_WORLD) works for std::vector<int>v(3)
- MPI_Bcast(b.data(),3,MPI_C_BOOL,0,MPI_COMM_WORLD) does not work for std::vector<bool>b(3)
- Use int type in MPI with C/C++ for boolean

## Intel compiler/mpi since 2024
- Module configuration Needs definition of ONEAPI_ROOT, I_MPI_ROOT, MKLROOT, FI_PROVIDER_PATH

## send/recv using a same variable in collective calls
- MPI_Allreduce(x,x,....) fails
- Use MPI_Allreduce(MPI_IN_PLACE, x, ....) works

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

# Check if IB is really working
- cat  /sys/class/infiniband/mlx*_0/ports/1/counters/port_*_packets
- May observe it changes/increases more than several thousands

# How to check IB dev/port
- show_gids
- If openmpi is installed, ompi_info --all |grep pml # not showing mlx but shows ucx or ob1
- If ucx is installed, ucx_info -d |grep Transport

# Find the version of mellanox driver
- modinfo mlx5_core

# monitoring memory consumption in the main node
- monitor.sh
```sh
#!/bin/sh
while true
do
  sleep 1
  date >> free.log_`hostname`
  free >> free.log_`hostname`
done
```
- In the job script
```
..
./monitor.sh&
mpirun ...
```
## cpu binding
- mvapich2: export MV2_CPU_MAPPING=0:1:2:3:4
- mpich: mpirun -n 4 -bind-to user:0,1,2,3 python3 cpu_id.py
  - Instruction: mpirun -bind-to -help
- openmpi: mpirun -n 4 -cpu-set 0,1,2,3 python3 cpu_id.py
```python
import psutil
print(psutil.Process().cpu_num())
```
## coupling with nvcc
- If nvcc cannot find mpi.h, then update CPATH variable as $MPI_ROOT/include

## configuring local variables per nodes
- Using hostname
  - At ~/.bashrc, check the hostname and we may configure different variables like CUDA_VISIBLE_DEVICES
- Using the configfile of MPMD
  - In MPICH
    - Command: `mpirun -hostfile ./my_hosts -configfile ./my_config`
    - Config file: `-n 4 -env CUDA_VISIBLE_DEVICES 0,1,2,3 ./my.exe -i ./my_input : -n 2 -env CUDA_VISIBLE_DEVICES 2,3 ./my.exe -i ./my_input`
  - In openmpi
    - Command: `mpirun --hostfile ./mfile --app ./config_ompi`
    - config_ompi:
```
-n 4 --map-by L3cache -x CUDA_VISIBLE_DEVICES=0,1,2,3 ./my_exe -i ./my_input
-n 2 --map-by L3cache -x CUDA_VISIBLE_DEVICES=2,3     ./my_exe -i ./my_input
```
