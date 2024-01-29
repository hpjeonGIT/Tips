## openmpi
- https://www.open-mpi.org/faq/?category=running
```bash
$ mpirun -np 1 ./a.out : -np 2 ./a.out 
0 3 hakune
2 3 hakune
1 3 hakune
$ cat appfile 
##
-np 1 ./a.out
-np 2 ./a.out
hpjeon@hakune:~/hw/mpi_cpp$ mpirun --app ./appfile 
0 3 hakune
1 3 hakune
2 3 hakune
```
- Q: ? global ranks are shared among applications?
- A: Yes. Communication b/w applications will be through MPI_COMM_WORLD. Each application will have it sown MPI_Comm, and each will have rank=0 from its own communicator

## mvapich
- https://mvapich.cse.ohio-state.edu/static/media/mvapich/mvapich2-2.3.6-userguide.html
```bash
$ cat configfile
#Config file example
#Launch 4 copies of exe1 with arguments arg1 and arg2
-n 4 : exe1 arg1 arg2
#Launch 2 copies of exe2
-n 2 : exe2
$ mpirun_rsh -config configfile -hostfile hosts
```
- ? `-config` option seems not working. Use `mpirun -np 1 ./a.out : -np 2 ./b.out`

## intel mpi
- https://www.intel.com/content/www/us/en/develop/documentation/mpi-developer-guide-linux/top/running-applications/mpmd-launch-mode.html
```bash
$ cat mpmd_config
-n 1 -host node1 ./io <io_args>
-n 4 -host node2 ./compute <compute_args_1> 
-n 4 -host node3 ./compute <compute_args_2
$ mpirun -configfile mpmd_config
```
- Or different formant of config file
```
-n 1 a.exe -m abc -mpmd ; -n 2 b.exe -m xyz -mpmd
```

## srun from cray
- mapfile
```
0-3 hostname
4-7 echo hello
```
- srun -n 8 -l --multi-prog ./mapfile
- for mpi job, srun --mpi=cray_shasta or pmi2 might be necessary

## sample test code
- a.cxx
```cxx
#include<iostream>
#include<mpi.h>
#include<unistd.h>
int main(int argc, char* argv[]) {
  int my_rank, ierr, ncpus;
  ierr = MPI_Init(&argc, &argv);
  ierr = MPI_Comm_size(MPIM_COMM_WORLD, &ncpus);
  ierr = MPI_Comm_rank(MPIM_COMM_WORLD, &my_rank);
  std::cout << "Hello from " << my_rank << " while ncpus = " << ncpus << std::endl;
  int color {1};
  int key {color};
  MPI_Comm local_comm;
  int ncpus_local, rank_local;
  ierr = MPI_Comm_split(MPI_COMM_WORLD, color, key, &local_commm);
  ierr = MPI_Comm_sizse(local_comm, &ncpus_local);
  ierr = MPI_Comm_rank(local_comm, &rank_local);
  char proc_name[MPI_MAX_PROCESSOR_NAME];
  int name_len;
  MPI_Get_Processor_name(proc_name, &name_len);
  std::cout << "Proccessor name = << proc_name << std::endl;
  std::cout << "a.exe from " << rank_local << " while local cpus = " << ncpus_local << std::endl;
  MPI_Finalize()
  return 0;
}
```
- Make another b.cxx using `int color {2}`
