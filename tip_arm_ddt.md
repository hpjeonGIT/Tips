
### ARM DDT license checkup
- curl http://license_server:port_number/status.html >log
- Open log file and find User Name

## license error
- At Ubuntu20
- Message `Error communicating with License server: XXX.YYY.ZZZ : proxy denied connection`
- Solution: unset http_proxy; unset https_proxy

## running mpmd
- mpich (mpmd) or intel mpi(mpmd) only
- ddt mpirun -n 1 ./a.out : -n 2 ./b.out
- intelmpi : mpiexec.hydra -np 2 ./a.exe : -np 3 ./b.exe
- In cray, mpmd run as: srun --mpi=cray_shasta -n 5 --multi-prog ./cray_job.config
  - In DDT, open GUI and configure slurm(MPMD) then in select the first executable as the main debug executable. Skip arugument section and fill mpirun argument with ` --mpi=cray_shasta -n 5 --multi-prog ./cray_job.config`. Set number of ranks as appropriate (5 in this example)
    
## Change the location of cache or configuration
- Open ~/.allinea/system.config
- Change the default setup of shared_directory=~
  - Any network mounted storage
