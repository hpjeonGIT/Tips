# For RHEL or CENTOS
- /etc/sysconfig/network-scripts/ifcfg-**
~~- May need quote "" for RHS~~
- Find MAC address using `ip addr`
- Enter `HWADDR=MAC address` in ifcfg-** file
- `NETWORKING=yes` and `HOSTNAME=abc.def.local` into /etc/sysconfig/network
- `systemctl disable NetworkManager; reboot`
~~- `systemctl restart network; systemctl status network~~

# when one of NIC doesn't work
- `ifdown port0`
- `ifup port1`
- Adjust /etc/sysconfig/network-scripts/ifcfg-port* to BOOTON port
- Run `ip route` and check the configuration
