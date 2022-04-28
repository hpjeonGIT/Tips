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

## intel mpi
- https://www.intel.com/content/www/us/en/develop/documentation/mpi-developer-guide-linux/top/running-applications/mpmd-launch-mode.html
```bash
$ cat mpmd_config
-n 1 -host node1 ./io <io_args>
-n 4 -host node2 ./compute <compute_args_1> 
-n 4 -host node3 ./compute <compute_args_2
$ mpirun -configfile mpmd_config
```
