## Nagios is a cluster management tool like Ganglia
  - However, Ganglia shows snapshots of the system while it lacks alerting mechanism
  - Nagios actually doesn't show much of snapshots
  - Sensor data are recognized as Exit codes such as 0: OK, 1: Warning, 2: Critical, 3: Unknown
  - It may spam admins with notice/warnings when criteria are met

## Nagios server on RHEL7/CENTOS7
- Ref: https://www.itzgeek.com/how-tos/linux/centos-how-tos/monitor-centos-7-rhel-7-using-nagios-4-0-7.html
- Pre requisite
    - Most of prerequisites are bundled in the developer version of RHEL7. Extra packages need to be installed
    - `yum install gd-devel --enablerepo=rhel-7-workstation-optional-rpms`
- User configuration
    - `useradd nagios`
    - `groupadd nagcmd`
    - `usermod -a -G nagcmd nagios`
    - `usermod -a -G nagcmd apache`
- Install of Nagios main core
    - Unpack nagios-4.*.tar.gz
    - `./configure --with-nagios-group=nagios --with-command-group=nagcmd`
    - `make all`
    - `make install`
    - `make install-init`
    - `make install-config`
    - `make install-commandmode`
    - `make install-webconf`
    - `make install-exfoliation` # `make install-classicui` for classic nagios theme
    - `htpasswd -c /usr/local/nagios/etc/htpasswd.users nagiosadmin`
    - `systemctl restart httpd`
    - Edit `/usr/local/nagios/etc/objects/contacts.cfg` for admin info
- Nagios plugins
    - Unpack nagios-plugins-2.3.1.tar.gz
    - `./configure --with-nagios-user=nagios --with-nagios-group=nagios`
    - `make`
    - `make install`
- Verification
    - `/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg`
```
...
Total Warnings: 0
Total Errors:   0
...
Things look okay - No serious problems were detected during the pre-flight check
```
- Starting service
    - `systemctl start nagios` # starting the service
    - `systemctl enable nagios` # enable autostart after reboot
    - `systemctl status nagios`
- May edit /etc/httpd/conf/httpd.conf for the listening port
- Configuration for receiving data from other computing nodes
    - `yum install nagios-plugins-nrpe --enablerepo=epel`
    - Edit `/usr/local/nagios/etc/nagios.cfg` and enable `cfg_dir=/usr/local/nagios/etc/servers`
    - `mkdir /usr/local/nagios/etc/servers`
    - Edit `/usr/local/nagios/etc/objects/commands.cfg`
```
# .check_nrpe. command definition
define command{
    command_name check_nrpe
    command_line /usr/lib64/nagios/plugins/check_nrpe -H $HOSTADDRESS$ -t 30 -c $ARG1$
    }
```    
    - Edit `/usr/local/nagios/etc/servers/client.mynodes.local.cfg`
        - Add members/service as necessary
```
define host{
            use                     linux-server           
            host_name               mynode10
            address                 1.2.3.4
}                                   
define host{
            use                     linux-server
            host_name               mynode33
            address                 1.2.3.44
}
define hostgroup{                   
            hostgroup_name          mycoms           
            alias                   Linux servers            
            members                 mynode10
            members                 mynode33
}                                   
define service{                     
            use                     local-service            
            hostgroup_name          mycoms
            service_description     SWAP Uasge            
            check_command           check_nrpe!check_swap                       
}                                   
define service{                     
            use                     local-service            
            hostgroup_name          mycoms
            service_description     Current Load            
            check_command           check_nrpe!check_load
}
define service{
            use                     local-service
            hostgroup_name          mycoms
            service_description     home Disk
            check_command           check_nrpe!check_home
}
define service{
            use                     local-service
            hostgroup_name          mycoms
            service_description     cpu Temperature
            check_command           check_nrpe!check_temp
}
define service{
            use                     local-service
            hostgroup_name         mycoms
            service_description    Memory consumption 
            check_command           check_nrpe!check_mem
}
```
    - Verification: `/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios.cfg`
    - `systemctl restart nagios`

## Nagios for RHEL7/CENTOS7 remote nodes
- Ref: https://kifarunix.com/how-to-install-nagios-plugins-and-nrpe-agents-on-centos-7-rhel-7-fedora-29/
- Ref: https://www.itzgeek.com/how-tos/linux/centos-how-tos/monitor-remote-linux-system-with-nagios-3.html
- `yum install -y nrpe --enablerepo=epel`
    - Install nrpe-3.2.1-8.el7.x86_64.rpm and nagios-common-4.4.3-1.el7.x86_64.rpm
- `yum install nagios-plugins-{load,users,procs,disk,swap,nrpe,uptime} -y --enablerepo=epel`
    - nagios-plugins-disk-2.3.1-3.el7.x86_64.rpm,nagios-plugins-load-2.3.1-3.el7.x86_64.rpm,nagios-plugins-2.3.1-3.el7.x86_64.rpm,nagios-plugins-nrpe-3.2.1-8.el7.x86_64.rpm,nagios-plugins-procs-2.3.1-3.el7.x86_64.rpm,nagios-plugins-swap-2.3.1-3.el7.x86_64.rpm,nagios-plugins-uptime-2.3.1-3.el7.x86_64.rpm ,nagios-plugins-users-2.3.1-3.el7.x86_64.rpm
- Check `/usr/lib64/nagios/plugins/`
- Edit `/etc/nagios/nrpe.cfg` # the names in [ ] must match with `/usr/local/nagios/etc/servers/client.mynodes.local.cfg` of the server
```
command[check_swap]=/usr/lib64/nagios/plugins/check_swap -w 20 -c 5
command[check_load]=/usr/lib64/nagios/plugins/check_load -r -w .15,.10,.05 -c .30,.25,.20
command[check_home]=/usr/lib64/nagios/plugins/check_disk -w 20% -c 10% -p /home
command[check_temp]=bash /usr/lib64/nagios/plugins/check_temp.sh -w 82 -c 92
command[check_mem]=bash /usr/lib64/nagios/plugins/check_mem.sh -w 80 -c 90
```
- Edit `/etc/nagios/nrpe.cfg` for `allowed_hosts=server_ip_address`
- `systemctl start nrpe`
- `systemctl enable nrpe`
- `firewall-cmd --add-port=5666/tcp --permanent; firewall-cmd --reload`
- For the Nagios server
    - Edit /usr/local/nagios/etc/servers/client.mynodes.local.cfg for the new host name and the update of hostgroup

## CPU Temperature using lm_sensors
- Ref: https://www.unixmen.com/write-nagios-plugin-using-bash-script/
- Find `https://github.com/jackbenny/check_temp/check_temp.sh`
- Copy to `/usr/lib64/nagios/plugins/`
- Adjust sensors command in the check_temp.sh such as
  - RHEL7/CENTOS7 : sensors |grep Package | awk -F '[ °C]' '{ sum+= $5 } END {print sum /NR}'
  - RHEL6/CENTOS6 : sensors |grep Physical | awk -F '[ °C]' '{ sum+= $4 } END {print sum /NR}'
    - Temperature data is averaged when “Physical” terms are triggered
  - TEMP=${TEMP%.*} # round to integer
- Double check if the command works
  - `bash ./check_temp.sh -w 92 -c 100`
    - Warning at 92 degree C and critical at 100 degree C

## memcheck using bash
- https://github.com/ckujau/nagios-plugins/edit/master/check_mem.sh
- RHEL7
  - Edit the code to use MemAvailable only
```
memAvail_kb=$(awk '/^MemAvailable:/ {print $2}' /proc/meminfo)
memUsed_kb=$(( memTotal_kb - memAvail_kb ))
```
- RHEL6
  - MemAvailable is not availalbe in /proc/meminfo
  - Let's use MemFree
```  
memFree_kb=$(awk '/^MemFree:/ {print $2}' /proc/meminfo)
memUsed_kb=$((  memTotal_kb - memFree_kb ))
```

## Alerting
- When using SMTP server
  - Ref: SMTP setup : https://support.hpe.com/hpesc/public/docDisplay?docId=emr_na-c02905871
  - sendmail and postfix uses the same port (25). One of them must be stopped to use the other
  - sudo service sendmail stop; sudo service postfix restart # or vice-versa. RHEL6
  - sudo systemctl stop sendmail ; sudo systemctl start postfix # or vice-versa. RHEL7
  - Check /var/log/maillog after testing sendmail or mail
  - When using sendmail
    - Adjust /etc/mail.rc as set smtp=ip_address at /etc/mail.rc
- In Nagios
  - Email address at /usr/local/nagios/etc/objects/contacts.cfg
  - Email command at /usr/local/nagios/etc/objects/commands.cfg
  - Main nagios configuration at /usr/local/nagios/etc/nagios.cfg
    - By default, it loads /usr/loca/nagios/etc/objects/commands.cfg, contacts.cfg, timeperiods.cfg, templates.cfg
  - Adjust /usr/local/nagios/etc/objects/templates.cfg for conditions or alerting level
    - w: warning
    - u: unknown
    - c: critical
    - r: recovery
    - f: flapping
    - n: none - disable alert
    - d: down
    - u: unreachable
    - s: send notification
    - notification_interval 120
      - Re-notify the same service problem every 120 min or 2hours

## slurm checking script
```
#!/bin/bash
	STATE_OK=0
	STATE_WARNING=1
	STATE_CRITICAL=2
	STATE_UNKNOWN=3
hname=$HOSTNAME
#echo ${hname}
if [ ${hname} = headnodeXXXX ] ; then
  stat=$(ps -ef |grep slurmctld |wc -l)
  if [ $stat -gt 1 ] ; then
    echo "SLURM STATUS - slurmctd found | slurmctd found"
    exit $STATE_OK
  else	
    echo "SLURM STATUS - slurmctd not found | slurmctd not found"
    exit $STATE_WARNING
  fi
else
 stat=$(scontrol show node ${hname} |grep State)
 C=${stat:9:1}
 if [ $C = "D" ]; then
   echo "SLURM STATUS - node down | node down"
   exit $STATE_WARNING
 elif [ $C = "A" ]; then
   echo "SLURM STATUS - node allocated | node up"
   exit $STATE_OK
 elif [ $C = "I" ]; then
   echo "SLURM STATUS - node idle | node up"
   exit $STATE_OK
 else 
   echo "SLURM STATUS - node unknown | node ?"
   exit $STATE_UNKNOWN
 fi
fi
```
- exit code is used to determine the status at Nagios
- echo command is necessary to show 1) Status information and 2) Performance data. They are split using a pipe (|)
- /etc/nagios/nrpe.cfg must be adjusted using `command[check_slurm]=bash /usr/lib64/nagios/plugins/check_slurm.sh`

## infiniband status checking script
```
#!/bin/bash
STATE_OK=0
STATE_WARNING=1
STATE_CRITICAL=2
STATE_UNKNOWN=3
#
stat1=$(ibstat mlx5_0 1 | grep State:)
stat2=$(ibstat mlx5_0 1 | grep state:)
txt1=${stat1:7:4}
txt2=${stat2:16:6}
#
if    [[ $txt1 = "Acti" &&  $txt2 = "LinkUp" ]] ; then
  echo "IB STATUS - Active | LinkUp"
  exit $STATE_OK
elif  [[ $txt1 = "Down" && $txt2 = "Disabl" ]] ; then
  echo "IB STATUS - Down | Disabled "
  exit $STATE_CRITICAL
elif  [[ $txt1 = "Acti" || $txt2 = "LinkUp" ]] ; then
  echo "IB STATUS - " $txt1 "|" $txt2
  exit $STATE_CRITICAL
else
   echo "IB STATUS - "  $txt1 "|" $txt2
   exit $STATE_UNKNOWN
fi
```
- Edit /usr/local/nagios/etc/servers/client.XXXnodes.local.cfg of Nagios server
```
define service{
use                     local-service
hostgroup_name          mynodes
service_description     IB status
check_command           check_nrpe!check_ib
}
```
- Edit /etc/nagios/nrpe.cfg of computing nodes: `command[check_ib]=bash /usr/lib64/nagios/plugins/check_ib.sh`
- Copy check_ib.sh into /usr/lib64/nagios/plugins of all computing nodes
- Start/restart nrpe daemon of computing nodes
- Start/restart nagios daemon of the Nagios server
