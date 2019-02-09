# In intel mpi
- Use -genv I_MPI_DEBUG 5 to find details of communication
- Use -genv MPI_IB_PORT_GID=fe80:0000:0000:0000 (<- this is GID from ibv_devinfo  -v) when there are issues from subnet mask
- export MPI_IB_PKEY="0xffff" when there are multiple pkeys : used for abaqus 2019
- For OFA, debug option is FI_LOG_LEVEL=debug. Use fi_info for find available fi

# In openmpi
- Recompile with ucx. This helped OpenCA to run
