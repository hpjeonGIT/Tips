# For centos/rhel 6 or 7
- Required rpm or yum libraries: libconfuse libconfuse-devel ganglia rrdtool ganglia-gmetad ganglia-gmond ganglia-web ganglia-gmond-python-modules
- php-bcmath and php-ZendFramework might be necessary - they need basic php-common. Depending on the existing version, find appropriate packages
- For server: all of them shown above
- For nodes: ganglia, ganglia-gmond, ganglia-gmond-python-modules

## Server configuration
- Ref: https://www.tecmint.com/install-configure-ganglia-monitoring-centos-linux/
- /etc/ganglia/gmond.conf
  - monitoring daemon configuration. Note that the server needs this as well
  - Sample gmond.conf shown below. Keep globals as default. Just send_metadata_interval might be adjusted as 30 or larger
  - Note that this is unicast setup. Multicast might not be recommended in common configuration
```  
  globals {
   daemonize = yes
   setuid = yes
   user = ganglia # nobody
   debug_level = 0
   max_udp_msg_len = 1472
   mute = no
   deaf = no
   allow_extra_data = yes
   host_dmax = 86400 /* Remove host from UI after it hasn't report for a day */
   cleanup_threshold = 300 /*secs */
   gexec = no
   send_metadata_interval = 30 /*secs */
 }

 cluster {
   name = "some_HPC_cluster_name"
   owner = "your_department"
   latlong = "unspecified"
   url = "unspecified"
 }

 host {
   location = "unspecified"
 }

 udp_send_channel {
   host = server_name_or_ip_addr
   port = 8649 # default is 8649 and recommended
   ttl = 1
 }

 udp_recv_channel { 
   port = 8649 # even though monitoring, server side needs this
 }

 tcp_accept_channel {
   port = 8649 # After daemon is executed, check netstat that 8649 tcp port is opened
 }
 ```
- /etc/ganglia/gmetad.conf 
  - Collecting daemon configuration
  - Mostly use default option but data_source and gridname might be adjusted. the data_source name must match with the used in gmond.conf
```
data_source "some_HPC_cluster_name" localhost # or ip or name of the server

gridname "MyGrid"
```
- Delivered data are stored at `/var/lib/ganglia/rrds/`. To change the location, `rrd_rootdir "/home/rrds"` in gmetad.conf
  - Ref: https://stackoverflow.com/questions/26619473/how-to-change-the-storage-path-from-rrdtool-on-the-ganglia
  - The folder owner:group would be ganglia. If the gmond.conf is configured as nobody, then nobody user:group must be applied
- To test, run as `sudo /usr/sbin/gmond -d 10` or `sudo /usr/sbin/gmetad -d 10`. `-d` is the debug mode
- When confirmed, run as:
  - RHEL6/CENTOS6 : `service gmond start; service gmetad start`
  - RHEL7/CENTOS7 : `systemctl start gmond; systemctl start gmetad`
- To stop, run as:
  - RHEL6/CENTOS6 : `service gmond stop; service gmetad stop`
  - RHEL7/CENTOS7 : `systemctl stop gmond; systemctl stop gmetad`
- To restart, run as:
  - RHEL6/CENTOS6 : `service gmond restart; service gmetad restart`
  - RHEL7/CENTOS7 : `systemctl restart gmond; systemctl restart gmetad`
- In order to start after reboot, those service must be turned-on automatically
  - RHEL6/CENTOS6 : `service gmond enable; service gmetad enable`
  - RHEL7/CENTOS7 : `systemctl enable gmond; systemctl enable gmetad`


## Configuration of nodes
- /etc/ganglia/gmond.conf
  - As this is for node configuration, gmetad.conf is not necessary
```
globals {
  daemonize = yes
  setuid = yes
  user = ganglia # nobody
  debug_level = 0
  max_udp_msg_len = 1472
  mute = no
  deaf = yes
  allow_extra_data = yes
  host_dmax = 86400 /* Remove host from UI after it hasn't report for a day */
  cleanup_threshold = 300 /*secs */
  gexec = no
  send_metadata_interval = 30 /*secs */
}

cluster {
   name = "some_HPC_cluster_name"
   owner = "your_department"
   latlong = "unspecified"
   url = "unspecified"
}

host {
  location = "unspecified"
}

udp_send_channel {
  host = server_name_or_ip_addr
  port = 8649
  ttl = 1
}
```
- For cluster management, `pdsh` might be used
  - `pdsh -w cluster[1-100] yum install -y /nfs/ganglia-gmond.rpm`
  - `pdsh -w cluster[1-100] yum install -y /nfs/ganglia-gmond-python-modules.rpm`
  - `pdsh -w cluster[1-100] 'cp /nfs/gmond.conf /etc/ganglia/'`


## Monitoring CPU temperature
- Built-in Ganglia doesn't monitor CPU temperature
- But gmond-python module may be customized to measure temperature
- May use lm_sensors for measuring temperature in centos/rhel
  - Download lm_sensors.rpm manually
  - `pdsh -w cluster[1-100] yum install -y /nfs/lm_sensors.rpm`
  - After installing lm_sensors, `sensors-detect` must run while this requires several interactive steps - answering yes or no
  - In pdsh command, such interactive jobs are not allowed and we may use standard input. Prepare stdin.txt like:
```
YES
YES
YES
YES

YES

```
  - Questions/Answers might be different per OS/HW/lm_sensors version. Check manually and prepare answers in the correct sequence
  - Then `pds -w cluster[1-100] 'sensors-detect < /nfs/stdin.txt'`. Note that quotation '' is required for the local command
  - Now `sensors` yields cpu temperature. Combining with `grep`, average or detailed temperature value can be measured
- Customizing example.py
  - Let's rename as cpuTemp.py and copy to /usr/lib64/ganglia/python-module/ or ganglia-gmond-python-module install location
  - Note that `cpu_*` is already registered in cpu_stat python script. Avoid similar wording
  - Test from CLI like `python cpuTemp.py` and check if the results are produced as designed
  - Prepare cpuTemp.pyconf using other templates. This file is copied to /etc/ganglia/conf.d
  - `pdsh -w cluster[1-100] 'cp /nfs/cpuTemp.py /usr/lib64/ganglia/python_modules/'`
  - `pdsh -w cluster[1-100] 'cp /nfs/cpuTemp.pyconf /etc/ganglia/conf.d/'`
  
## Web server configuration
- `htpasswd -c /etc/httpd/auth.basic adminganglia`
- Edit /etc/httpd/conf.d/ganglia.conf
```
Alias /ganglia /usr/share/ganglia
<Location /ganglia>
    AuthType basic
    AuthName "Ganglia web UI"
    AuthBasicProvider file
    AuthUserFile "/etc/httpd/auth.basic"
    Require user adminganglia
</Location>
```
- To run httpd,
  - RHEL6/CENTOS6 : `service httpd start` or `service httpd restart`
  - RHEL7/CENTOS7 : `systemctl start httpd` or `systemctl restart httpd`
  
## Visualization
- Open web-browser and enter the address of the server such as: `http://server_name_or_ip_addr/ganglia`
- Enter `adminganglia` and the password configured as above

## Temperature measurement using ipmitool
- Similar python configuration done for lm_sensors package
- But /dev/ipmi0 might be owned as ganglia:ganglia -> is this safe enough?
- `ipmitool sensor |grep Ambi` for ambient temperature
