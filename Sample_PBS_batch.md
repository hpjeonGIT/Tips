# Samples of PBS batch command for application

## HFSS ---------------------------------------------------------------------
```bash
#!/bin/bash
#PBS -l walltime=168:00:00
#PBS -l select=1:ncpus=32:mpiprocs=32:ompthreads=1:mem=70gb
#PBS -q @pbsServer
#
# REF: https://wiki.hpcc.msu.edu/display/~colbrydi@msu.edu/2011/06/08/HFSS+script
#
. /etc/profile.d/modules.sh
export NNODES=`sort $PBS_NODEFILE | uniq | wc -l`
export NPROCS=`wc -l < $PBS_NODEFILE`
cd $PBS_O_WORKDIR

module load hfss
export ANSYSEM_HOST_FILE=$PBS_NODEFILE
# export AnsTempDir=/wrk/$USER/tmp  # scratch folder this doesn't work
ansysedt -distributed -machinelist numcores=$NPROCS -auto -monitor -ng -batchsolve -batchoptions "HFSS/HPCLicenseType=pool tempdirectory=/scratch/myscratch"  coaxial.aedt | tee pbs.log
```
## ansys mechanical  ---------------------------------------------------------------------
```bash
#!/bin/bash
#PBS -l walltime=168:00:00
#PBS -l select=1:ncpus=32:mpiprocs=32:ompthreads=1:mem=18gb
#PBS -q @pbsServer
#PBS -N ansysMECH
#
. /etc/profile.d/modules.sh
export NNODES=`sort $PBS_NODEFILE | uniq | wc -l`
export NPROCS=`wc -l < $PBS_NODEFILE`
cd $PBS_O_WORKDIR

mkdir $WORK/$PBS_JOBID
module load ansys
cd $PBS_O_WORKDIR
ansys191 -i YOURINPUT.dat -dir $WORK/$PBS_JOBID -dis -p ansys -np ${NPROCS} -o file.out -s read -l en-us -b -usessh
# Scratch folder locationis given from -dir. Or use TMPDIR variables in the bash
```

# Fluent ---------------------------------------------------------------------
```bash
#!/bin/bash
#PBS -l walltime=168:00:00
#PBS -l select=10:ncpus=32:mpiprocs=32:ompthreads=1:mem=100gb
#PBS -q @servername
export NNODES=`sort $PBS_NODEFILE | uniq | wc -l`
export NPROCS=`wc -l < $PBS_NODEFILE`
. /etc/profile.d/modules.sh
cd $PBS_O_WORKDIR
export OMP_NUM_THREADS=1

module load ansys
echo "Running case now"
lfs setstripe -S 1m -c 8 . # Lustre setup
fluent 3ddp -mpi=intel -g -ssh -t${NPROCS} -cnf=${PBS_NODEFILE} -i input.jou  -pib  -feature_parallel_preferred=anshpc_pack > log.out
## -feature_parallel_preferred=anshpc for anshpc license. Choose pack for very large scale run
```
# Abaqus ---------------------------------------------------------------------
```bash
#!/bin/bash
#PBS -l select=1:ncpus=32:mpiprocs=32:ompthreads=1:mem=150gb
#PBS -l walltime=168:00:00
#PBS -q @server
#PBS -N ABQ
cd $PBS_O_WORKDIR  
export NNODES=`sort $PBS_NODEFILE | uniq | wc -l`
export NPROCS=`wc -l < $PBS_NODEFILE`
. /etc/profile.d/modules.sh
module load abaqus 
abaqus job=__inp_file_name__ cpus=$NPROCS inter scratch=$WORK/tmp
```
# Comsol ---------------------------------------------------------------------
```bash
#!/bin/bash
#PBS -N Q1
#PBS -l walltime=168:00:00
#PBS -l select=1:ncpus=32:mpiprocs=8:ompthreads=4:mem=150gb
#PBS -q @serverName
export NNODES=`sort $PBS_NODEFILE | uniq | wc -l`
export NPROCS=`wc -l < $PBS_NODEFILE`
. /etc/profile.d/modules.sh
cd $PBS_O_WORKDIR
module load comsol
comsol batch -nn $NPROCS -f $PBS_NODEFILE  -np $OMP_NUM_THREADS -tmpdir $WORK/tmp -study std4 -inputfile ${JNAME}.mph  -outputfile output.mph -batchlog log.txt
```

# RSoft FullWave
```bash
#!/bin/bash
#PBS -l select=1:ncpus=16:mpiprocs=16:ompthreads=1
#PBS -l walltime=2:00:00
#PBS -N rsoft_fullwave
#PBS -q @servername

cd $PBS_O_WORKDIR

export NNODES=`sort $PBS_NODEFILE | uniq | wc -l`
export NPROCS=`wc -l < $PBS_NODEFILE`

module load rsoft
rslmd -start
export P4_RSHCOMMAND=rshlocal
fwmpirun -np $NPROCS wg.ind
rslmd -stop
```

