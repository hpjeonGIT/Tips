## Altair PBS
- qsub -I -l walltime=1:0:0 -l select=1:ncpus=8
- qsub myscript
- qstat -u USERNAME
- qdel 12345
```
#!/bin/bash
#PBS -q workq
#PBS -l select=2:ncpus=16:mpiprocs=8:ompthreads=2
#PBS -l walltime=1:0:0
#PBS -o log.out
#PBS -e log.err
#
cat $PBS_NODEFILE
nranks=$(wc -l < ${PBS_NODEFILE})
#
module load intel
module load mpi/intel.4.2.0
cd $PBS_O_WORKDIR
#mpirun a.exe
mpirun -n $nranks ./a.exe
```    
## SLURM
- srun : run commands in the computing node
    - `srun -N 1 ./a.out` # Run a.out using 1 node. When the a.out is completed, the prompt is returned
- salloc : allocate resource but the prompt is still available. Then use `srun` or ssh into the assigned re
source. You may run multiple sequential jobs. To terminate the queue, run `exit`
    - `salloc -N 1; srun ./a.out; exit`
- sbatch : batch job command. Must provide batch jobs script
    - `sbatch myjobscript.job`
- squeue : show the status of queue in SLURM scheduler
    - `squeue` # shows all of queue
    - `squeue -u USERNAME` # shows the jobs status of a user USERNAME
- scancel : terminate the job regardless of the status
    - `scancel 12345`
- A sample SLURM script
```
#!/bin/bash
#SBATCH -o job-%j.out
#SBATCH -e job-%j.err
##SBATCH -w, --nodelist=node123,node124
#SBATCH -J my_job
#SBATCH -N 5
#SBATCH --ntasks-per-node=16
#SBATCH --export=ALL
#SBATCH --time=1:0:0
#
module load gcc mvapich
export OMP_NUM_THREADS=1
export MV2_ENABLE_AFFINITY=0
export EXE=/home/myhome/a.exe
#
cd $SLURM_SUBMIT_DIR
mpirun -np $SLURM_NPROCS $EXE | tee $SLURM_NPROCS.log
```

## UGE
- Univa Grid Engine
- Ref: https://proteusmaster.urcf.drexel.edu/UGE/user_guide.html
- qsub:
    - ex: `qsub -pe mpi_pe 4-10 -masterq super.q mpi.sh`
- qdel:
- qmod
- qlogin: interactive job
- qhost : shows the working queue
- qstat : 
- qconf: shows the configuration
- Sample batch script
```
#!/bin/bash
#$ -pe mpi-24 48
module load ompi/2.1.1-intel-17.1
mpirun -np $NSLOTS yourapplication
```
- `qsub sample.sh` # using the default queue
- `qsub -q abcEXF sample.sh` # using abcEXF queue

## LSF
- IBM job scheduler for P9 cluster
- REF: https://hpc.llnl.gov/banks-jobs/running-jobs/lsf-commands
- bhist: display info from completed jobs
- bhosts: display hosts and their static and dynamic resources
- bjobs: display your jobs in the scheduling queues, one job per line
- bjobs -l <jobID>: display detailed information about a specific job
- bjobs -u all: display all jobs in the scheduling queues, one job per line
- bkill: remove a job from the queue or kill it if it is running
- bkill -s <signal>: send a signal to a running job
- bmod: modify a job's requirements
- bpeek: display the stdout and stderr output of a running job
- bqueues: display the available queues
- bresume: re-enable a suspended job for scheduling
- bstop: suspend a pending job from being scheduled to run
- bsub: submit a batch script to LSF
- bsub -Ip: request an interactive job allocation
- bsub -XF xterm: request to launch an xterm window
- bugroup: display user groups (charge accounts) and membership
- lshosts: display hosts and their static resource information
```
#BSUB -W 10:00
#BSUB -n 4
#BSUB -R "span[ptile=2]"
#BSUB -e <some directory>/%J.err
#BSUB -o <some directory>/%J.out
#
module load mpich1/gnu
#
cd ~
# execute program
mpiexec -np 4 myprogramname
```
