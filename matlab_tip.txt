## Control the number of threads
- OMP_NUM_THREADS might be ignored
- maxNumCompThreads will be deprecated in future release
- feature('numThreads',str2num(getenv('OMP_NUM_THREADS')))
- or  feature('numThreads',6)

## Checking License status
### Windows
- cd c:\program files\matlab2013a\etc\win64 (or installed directory)
- run “lmutil lmstat –a”
### Linux
/opt/apps/matlab/R2014a/etc/glnxa64/lmutil lmstat -a -c 27000@license_server

## Debugging in Linux CLI
- http://www.mathworks.com/help/matlab/matlab_external/debugging-on-linux-platforms.html
- matlab –Dgdb
- gdb> handle SIGSEGV SIGBUS nostop noprint 
- gdb> run –nojvm
- your_script (without .m extension)

## Running standalone applications
- External files to be parsed in the matlab app are automatically included in the stand-alone application compilation
- Even deleting the choice from the menu, it updates automatically anyway
- Manually move such files from the folder temporarily
- Ref: https://www.mathworks.com/help/compiler_sdk/ml_code/mcr-component-cache-and-ctf-archive-embedding.html
- In PBS script: SCRATCH_DIR=$WORK/$PBS_JOBID; mkdir $SCRATCH_DIR; export MCR_CACHE_ROOT=$SCRATCH_DIR ; 
- Default MCR cache folder is located in $HOME/.mcrcache

