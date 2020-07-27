## some commands for HPe CMU
- HP Cluster Management Utility
- Java GUI may work: `java -jar cmugui.jar`
- pdsh is one of the commands from CMU

## For RHEL6/CMU 7.X
- sudo /opt/cmu/bin/cmu_power -p BOOT -n compnodeXX # boot a node
```
powering off compnode10 ...
spawning 1 task(s)       ................
waiting for 1 task(s)    ................ { last:compnode10 }
sleeping 10 seconds      ................
powering on compnode10 ...
spawning 1 task(s)       ................
waiting for 1 task(s)    ................ { last:compnode10 }
/opt/cmu/bin/cmu_power finished
```
- sudo /opt/cmu/bin/cmu_monstat --nodes=compnode11 # show the list of sensors and values
- sudo /opt/cmu/bin/cmu_power -p OFF -a # Shutdown all nodes
- sudo /opt/cmu/bin/cmu_power -p OFF -n "compnode001 compnode002 ..." # Shutdown specific nodes
- for i in {81..90} ; do sudo /opt/cmu/bin/cmu_power -p OFF -n "compnode$i" ; done # Shutdown through loop
- for i in {81..90} ; do sudo /opt/cmu/bin/cmu_power -p STATUS -n "compnode$i" ; done # Check status through loop

## For RHEL7/CMU 8.X
- cmu_power -p REBOOT -n compcnodeXX # boot a node

## Nitty-Gritty
- CMU configuration: /opt/cmu/etc/cmuserver.conf
- Ref: https://community.hpe.com/t5/Server-Clustering/NO-Netboot-reboot-not-working-CMU-7-2-ProLiant-SL4540-Gen8-RHES/td-p/6482202#.XkVtBOhKjuo
- Log file of each node from CMU command: /opt/cmu/tmp/ # Find *.output files

## when disk mout is not working
- /etc/fstab is the configuration
- sudo pdsh -w node# 'service netfs restart' # restarting nfs. Will not fix HW failure.
- ssh into the node and run `ip a`. Check if ib card is detected.
- ssh into the node and run ` hostname -l` to see if ib card is detected.
- sudo pdsh -w node#  `ibhosts` to see if ib card is detected or working correctly.
- If ib status is not correct, HW replacement might be necessary.
