## mvapich2 with totalview
- Can be used for MPMD case as well
- export TOTALVIEW=/opt/.../bin/totalview
- mpirun_rsh -hostfile MYhosts -tv -np 3 a.out : -np 4 b.out
