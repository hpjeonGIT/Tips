## stress package from yum

## make cpu busy
- yes > /dev/null
  - But may not be efficient for multicores
- openssl speed -multi $(nproc --all)
  - When nproc works, can make all of multicores busy
- mpirun -np $SLURM_NPROCS openssl speed -multi 1
  - MPI version for openssl
  
