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
