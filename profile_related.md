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
- Sample uprof command:
  - mpirun -np 40 .../AMDuProfCLI collect --config tbp --mpi --output-dir ./PROF40 ../bin/a.exe
  - MPI trace only: mpirun -np 40 .../AMDuProfCLI collect --trace mpi=full --output-dir ./TMP ../bin/a.exe
