## mvapich2 with totalview
- Can be used for MPMD case as well
- export TOTALVIEW=/opt/.../bin/totalview
- mpirun_rsh -hostfile MYhosts -tv -np 3 a.out : -np 4 b.out
- ? not working?

## openmpi/mpich/intel mpi
- totalview -classicUI -nocuda -args mpiexec -np 2 ./a.exe : -np 3 ./b.exe
- mpirun may not work. Use mpiexec
  - srun or aprun on cray
- The order of arguments matters
- In the new UI, the source code of b.exe may not appear. Then click b.exe in the pid pane -> go to the pane of call stack -> click the function name

## attaching running pid
- totalview -classicUI
- click attach menu
- click +H and add the first computing node (we assume that you're on headnode of the cluster)
- In cray srun environment, select **parent srun** process, not **child srun** process
  - In regular mpirun environment, this might be different
  - Can attach MPMD as well

## for openmpi version 5 or higher
- orterun is not provided anymore while totalview will look for orterun
- Make a symbolic link of orterun at bin folder using mpirun
