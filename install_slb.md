# installing schlumberger SW like eclipse, IX, Visage at RHEL8
- yum install tcsh
- Copy installer from DVD to local disk
- chmod u+x CDROM/ECLIPSE/UNIX/install/*.csh
- cd CDROM/ECLIPSE/UNIX/install
- tcsh ./cdinst.sh
- eclipse, IX, Visage may share same install steps
- Regarding Macros, install from Eclipse only. IX and Visage may share the Macros from Eclipse
- The install path must be shared as ecl folder: ex) `/opt/ecl` or `/share/ecl`
- After installation is completed, system variable of ECLPATH must be defined: ex) `ECLPATH=/opt/ecl`
  - License variable would be `SLBSLS_LICENSE_FILE=port_no@server_name`
- Update PATH variable for each executable and Macros location. Also Tools must be added to run mpirun command

## Running eclipse
- For abc.DATA input file,
  - eclipse.exe abc
  - Do not add the extension name (.DATA)
  - eclrun eclipse abc.DATA
    - eclrun is a general purpose coordinator. Can run eclipse, ix, visage from eclrun command
    - This will produce abc.h5, as a summary file
    - If summary is not necessary, add `--summary-conversion no`
    
## Running IX
- ix.exe --use-sim-ul abc.afi
- eclrun ix --use-sim-ul yes abc.afi
  - This will produce abc.h5 as a summary file

## Running Visage
```
visage.exe -b abc.VBT # serial visage
eclrun visage abc.VBT # serial visage using eclrun
mpirun -np 4 visage_plmpi -b abc.VBT  # visage using platform MPI. Extra configuration is necessary for IB. Check manual
eclrun --np 4 visage abc.VBT   # 4 rank mpi using eclrun. default is Intel mpi
eclrun -t 2 visage abc.VBT     # using 2 OMP threads
eclrun --np 2 -t 2 visage abc.VBT  # using 2 MPI rank while each rank uses 2 OMP threads
eclrun --np -2 -c plmpi visage abc.VBT # Using Platform MPI from eclrun
eclrun rgcoupler sample.MII  # Running Eclipse + Visage coupling
```

## Submit a job from Windows to Linux
- Computing node (Linux) must have ECLPATH definition from .bashrc  
  - Update PATH and license setup in .bashrc
- Using job scheduler (PBSPRO in the example)
  - `eclrun.exe -s compnode  -u user_name -p passwd --queuesystem=PBSPRO -q=workq eclipse abc.DATA --debug=both`
  - Registration of ssh_keygen is recommended instead of sending passwd through CLI
- standalone execution (no job scheduler). 
  - `eclrun.exe -s compnode -u user_name -p passwd eclipse abc.DATA --debug=both`
    - `--queuesystem=local` will assume windows
- Fetching or retrieving results 
  - `eclrun.exe check abc.DATA`
  - TBD. Not working at this moment

## How to check occupied license and remove the current license consumption
- /opt/SLB_2024/tools/linux_x86_64/flexlm1116/lmutil lmstat -a -c 1234@license.server.local
  - Check which feature and which hanlder are used
- /opt/SLB_2024/tools/linux_x86_64/flexlm1116/lmutil lmremove -c 1234@license.server.local -h SomeFeature license.server.local 1234 <handler_no>
