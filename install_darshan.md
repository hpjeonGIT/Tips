- Ref: https://www.mcs.anl.gov/research/projects/darshan/

# steps to install
- Unpack
- ./prepare.sh
- cd darshan-runtime
- ./configure --prefix=/opt/darshan/3.4.4/rt --with-log-path=/opt/logs --with-jobid-env=PBS_JOBID CC=mpicc
- make; make install
- Edit bin/darshan-mk-log-dirs.pl
```pl
use Env;
if ($DARSHAN_LOGPATH eq "") {
  $LOGDIR="/opt/logs"
} else {
  $LOGDIR=$DARSHAN_LOGPATH;
}
```
  - Now `export DARSHAN_LOGPATH=/tmp` is accecpted
- cd ../darshan-util
- ./configure --prefix=/opt/darshan/3.4.4/util
- make; make installan
  - If QT visualization fails, edit dxt_analyzer.py as `matplotlib.use('Agg')`

# steps to use
- export DARSHAN_LOGPATH=`pwd`
- darshan-mk-log-dirs.pl
- LD_PRELOAD=/opt/darshan/3.4.4/rt/lib/libdarshan.so mpirun -n 8 ./a.out
- darshan-job-summary.pl AAA.darshan will generate AAA.pdf
- darsha-parser AAA.darshan to produce text results
