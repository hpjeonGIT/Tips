## cray perftools-lite
- load perftools and perftools-lite
- -O3 is supported
- Run then a folder of exe+12345... is produced
- app2 ./exe+12345 for GUI
- pat_report ./exe+12345 for text summary


## Cray perftools-lite-loops
- https://cpe.ext.hpe.com/docs/performance-tools/man1/reveal.html
- Cray compiler only
- Load perftools and perftools-lite
- Build the code without optimization (-O0). Any optimization may yield segfault in the end of the run
- Run then a folder of exe+12345... is produced
- Unload perftools-lite
- Compile the code again with -O3 and -fcray-program-library-path=./myapp.pl
  - -DCMAKE_CXX_FLAGS="-fcray-program-library-path=./myapp.pl"
- reveal ./myapp.pl ./exe+12345

## AMD uProfiler
- When 'Error while mapping data pages. Consider increaseing /proc/sys/kernel/perf_event_mlock_kb or provding ...' happens:
  - Sol: `ulimit -l unlimited`. If not working, see below:
  - ~~If not works, sudo ulimit -Hl unlimited then reboot~~
  - Edit /etc/security/limits.conf then reboot
```
*   hard memlock unlimited
```
  - This is only for local users. If accounts are from LDAP or PAM, edit /etc/systemd/system.conf
```
DefaultLimitMEMLOCK=65536:infinity
```
  - If you use vnc session, ulimit -l must be adjusted before launching vnc session. The session will inherit from the current terminal and you will not be able to adjust memlock
- Collection steps: 
  - mpirun -np 40 .../AMDuProfCLI collect --config tbp --mpi --output-dir ./PROF40 ../bin/a.exe
  - MPI trace only: mpirun -np 40 .../AMDuProfCLI collect --trace mpi=full --output-dir ./TMP ../bin/a.exe
  - TBP + mpi: mpirun -np 40 .../AMDuProfCLI collect --config tbp --trace mpi=full --output-dir ./TMP ../bin/a.exe
  - TBP + mpi + call graph: mpirun -np 40 .../AMDuProfCLI collect --config tbp --call-graph --trace mpi=full --output-dir ./TMP ../bin/a.exe
- Translation:
  - Done automatically when loaded in GUI
  - For very large results, use batch
  - AMDuProfCLI translate -i ./TMP/AMDuProf-a.exe-Custom-MPI --log-path ./log_dir --enable-log --category cpu,mpi
    - This will run multiple-threading processes. Feed some cpus (>4) on a single node
- Analysis:
  - Load the results from GUI of AMDuProf

## nvidia ncu/nsys
- Basically they need sudo privilege
- Or make /etc/modprobe.d/nvidia_prof.conf containing 'options nvidia NVreg_RestrictProfilingToAdminUsers=0'
  - Ref: https://developer.nvidia.com/nvidia-development-tools-solutions-err_nvgpuctrperm-permission-issue-performance-counters
- `ncu --target-processes all -o report_all mpirun -n 4 a.exe -i input` for collecting all ranks together
- To get profile over each rank, the nvidia manual shows to use `report_%q{OMPI_COMM_WORLD_RANK}` but this doesn't work
  - `PMI_RANK` for mpich or intel mpi
  - `MV2_COMM_WORLD_RANK` for mvapich2
  - Instead of rank number, use process number
  - `mpirun -n 4 ncu -o report_%p a.exe -i input`
  - May combine `%h` to append hostname
    
