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

