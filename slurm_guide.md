## commands for slurm
- `sinfo` # shows the status of nodes
- `scontrol show node mynode132`
  - Shows the status of mynode132
  - If it is down, show the Reason why it is down
## commands for slurm admin
  - ssh into the ndoe or pdsh (HP CMU) to check the status of slurm daemon
    - `sudo pdsh -w mynode231 'ps -ef |grep slurmd'`
  - If not running, run as `sudo pdsh -w mynode231 '/opt/slurm/sbin/slurmd'`
  - Bring downed nodes into up
    - `sudo /opt/slurm/bin/scontrol update nodename=mynode113 state=resume`
  - Bring the working nodes into down
    - `sudo /opt/slurm/bin/scontrol update nodename=brcnode123 state=down`
## when slurm job is frozen
  - When CG is the job status
    - Restart daemon in the head node
    - Restart daemon in the computing node
    - Remove the node from SLURM and mount again

## when sacctmgr yields an error message of connection related
```
sacctmgr: error: slurm_persist_conn_open_without_init: failed to open persistent connection to localhost:6819: Connection refused
sacctmgr: error: slurmdbd: Sending PersistInit msg: Connection refused
sacctmgr: error: Problem talking to the database: Connection refused
```
- Start or restart slurmdbd
  - For RHEL6, `service slurmdbd restart`

## When orphaned or dangled jobs exist
- scancel will not be able to remove them. Not found from squeue
- Restart of slurmd will not resolve
- `sacctmgr show RunawayJobs`
  - Will ask fix or not. Enter `y` to fix and enter

## when job submission fails
- Check the time b/w slurm head node and computing nodes. They must sync each other

## Installing slurm
- check install guide and use rpmbuild then can use systemctl
- When slurmctld yields the message of `not a valid controller`
    - In slurm.conf, use `SlurmctrldHost=hostName(IP.Number.here)`
- When slurmd yields the message of `unable to determine this slurmd's NodeName`
  - In slurm.conf, use node name of `hostname -s` at `ControlMachine=nodeName`
- When compute node is invalid from `sinfo`
  - Make sure that the detail of node in slurm.conf match the results of `slurmd -C` in each node
  - No. of cores, threads per core, memsize, ...
