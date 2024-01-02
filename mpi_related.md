## boolean in cpp
- MPI_Bcast(v.data(),3,MPI_INT,0,MPI_COMM_WORLD) works for std::vector<int>v(3)
- MPI_Bcast(b.data(),3,MPI_C_BOOL,0,MPI_COMM_WORLD) does not work for std::vector<bool>b(3)
- Use int type in MPI with C/C++ for boolean

## Intel compiler/mpi since 2024
- Module configuration Needs definition of ONEAPI_ROOT, I_MPI_ROOT, MKLROOT, FI_PROVIDER_PATH
