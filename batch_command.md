### Estimating the number of cpus
export NPROCS=`wc -l < $PBS_NODEFILE`

## Abaqus
abaqus job=__inp_file_name__ cpus=$NPROCS inter scratch=$WORK/tmp

## HFSS
ansysedt -distributed -machinelist numcores=$NPROCS -auto -monitor -ng -batchsolve -batchoptions "HFSS/HPCLicenseType=pack"   Diplexer_TGV_L.aedt | tee pbs.log

ansysedt -distributed -machinelist numcores=$NPROCS -auto -monitor -ng -batchsolve -batchoptions "HFSS/HPCLicenseType=pool" Diplexer_TGV_L.aedt | tee pbs.log

## Comsol
comsol batch -nn $NPROCS -f $PBS_NODEFILE  -np $OMP_NUM_THREADS -tmpdir $WORK/tmp -study std4 -inputfile ${JNAME}.mph  -outputfile output.mph -batchlog log.txt

## FireFoam
(time mpirun -np $NPROCS fireFoam -parallel) |& tee log.$NPROCS.fireFoam

## Fluent
fluent 3ddp -mpi=intel -g -ssh -t${NPROCS} -cnf=${PBS_NODEFILE} -i input.jou  -pib  -feature_parallel_preferred=anshpc_pack > log.out

fluent 3ddp -mpi=intel -g -ssh -t${NPROCS} -cnf=${PBS_NODEFILE} -i input.jou  -pib  -feature_parallel_preferred=anshpc > log.out

## MPI a.out
(time mpirun -n $NPROCS  $APP) |&  tee $NPROCS.log
