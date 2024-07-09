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
