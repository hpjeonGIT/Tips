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
- `traceroute 8.8.8.8`
- `tracepath 8.8.8.8`
- `ip neighbor`
  - STALE seems OK
- `ip addr flush portname` to clear the port - this may help
- `netstat -rn` to see gateway
- `nmcli -f ip4 device show interface-name` 
- `dhclient interface_name` may refresh dhcp client?
- If 802.1x security is applied in the network port, enable 802.1x secruity from Network Manager
