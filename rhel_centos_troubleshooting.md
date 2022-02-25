# installing nvidia driver
- Disable nouveau
  - Google for detail. Needs blacklist
- If kernel is updated, kernel-devel kernel-headers must be updated as well
- sh NVIDIA-***.run --no-rdm
  - Without --no-rdm, OS may refuse to install. Discuss with Security folks for the detail
 - export TMPDIR=/somewhare/more_than_4GBs
 - sh ./cuda**.run
  - Cuda installation may unpack more than 4GB files


## vncserver
- yum install tigervnc-server
  - https://www.itzgeek.com/how-tos/linux/centos-how-tos/configure-vnc-server-on-centos-7-rhel-7.html
  - vncserver@.service might not be necessary. Skip the configuration
- Will need firewall setup
  - --zone=public
  - --add-port=5900-5909/tcp
  
## virtualGL
- https://virtualgl.org/vgldoc/2_1_1/
- Download rpm from sourceforge.net
- `yum install virtualGL-2.6.2.x86_64.rpm`
- Step
  - `init 3`
  - `rmmod nvidia_drm; rmmod nvidia_modeset; rmmod nvidia`
  - `/opt/VirtualGL/bin/vglserver_config`
    - Answer Y x3
- `usermode -a -G vlgusers <username>` # root, all local users, domain users
- `reboot`

## When java application crashes with Canvas3D error message on VNC session
- Ex) Tempestview on VNC session from RHEL6
- Check glxgear opens. If it complains xlib error with display :X.0, then the VNC session may not be able to shoot X-graphics
- To resolve, virtualGL is necessary such as `vglrun java_application` on VNC session
- User account must be added into vglusers group in /etc/groups. If just added, logout/re-login is necessary. For VNC session, terminate and restart

## Using TurboVNC from windows
- Using putty, login to the server
- `vncserver -list`
  - Check any existing display
- First time `vncserver` will ask new password
- Login using TurboVNC
- If Authentication message appears, just click cancel
  - Or fix using https://github.com/TurboVNC/turbovnc/issues/47
- `/opt/VirtualGL/bin/vglrun glxgears`
  - When `Invalid MIT-MAGIC-COOKIE-1 key [VGL] ERROR: Could not open display :0` is shown, `unset XDG_VTNR`
- If refresh is slow or screen is laggy, adjust Enconding option through Options -> Encoding

## environmental module
- Install: yum install environment-modules
- Sample module file
```
##
proc ModulesHelp { } {
        puts stderr "\tProvides antlr"
        }
module-whatis "-------------------------------"
module-whatis "(Name___________) antlr"
module-whatis "(Version________) 4.7.1"
module-whatis "(Dependencies___) "
module-whatis "-------------------------------"
module-whatis ""
# Local TCL 
set     topdir  /opt/antlr
setenv           PARAVIEW_HOME  $topdir
prepend-path     PATH           $topdir/bin
prepend-path     LD_LIBRARY_PATH $topdir/lib
prepend-path     CLASSPATH     $topdir/antlr-4.7.1-complete.jar
set-alias "ll" "ls -l"
#set-alias  antlr4 {java -Xmx500M -cp "$CLASSPATH" org.antlr.v4.Tool $1}
set-alias  antlr4 "java -Xmx500M -cp "$CLASSPATH" org.antlr.v4.Tool"
```
  - Regular alias works using double-quotes
  - When using system variable, regular alias will not work. Using curly braces {} and define as a function. For the input argument, use $1 to parse
- export MODULEPATH=/opt/modulefiles:$MODULEPATH

## yum cache location
- Ref: https://www.thegeekdiary.com/how-to-change-the-default-location-var-cache-yum-of-yum-cache/
- If the partition of /var is too small (10GB might be recommended), yum cache may result in disk shortage
- Edit `/etc/yum.conf` to assign a different location for cache files

## when NFS is not mounted
- Check /lib/modules/__XX_kernel_number__/kernel/fs to see if nfs is enlisted
- Check /proc/filesystems to see if nfs is enlisted
- May need to restart nfslock : `service nfslock restart; service rpcbind restart`
- May rerun netfs : `service netfs restart`
- Check /proc/filesystems if nfs is loaded
- May need reboot

## yum group install
- Pre-selection from kicstart GUI menu
  - If missed, can be done later in CLI using yum group install
  - The names of list is found using `yum group list hidden`
- Sample group install command
  - `yum group install "Development Tools"`

## RHEL8 with legacy driver
- RHEL8 dropped the support of legacy RAID/SAS/SATA driver
  - When install GUI comes, it may not detect any of local disk
- Ref: https://access.redhat.com/discussions/3722151
- May use legacy driver at https://elrepo.org/linux/dud/el8/x86_64/
  - For Intel C600,	dd-isci-1.2.0-3.el8_X.elrepo.iso will work
 - Steps of RHEL8/CENTOS8 install with legacy driver
   - Prepare RHEL8/CENTOS8 install image as DVD or USB
   - Prepare legacy driver as a USB (using dd command : 
     - sudo fdisk -l # check which /dev/sd* is for the mounted USB
     - sudo dd if=name-of.iso of=/dev/sdb
   - Reboot the computer with install image as DVD or USB
   - Insert dd image USB memory stick into the USB port
     - If install USB and dd image USB are already in the USB port simultaneously when booted, booting sequence may not work due to confusion
   - When dd image is made, it would have name of OEMDRV and kicstart will recognize the driver automatically
   - If dd image is not found, add manually
     -  When menu of Install Red Hat Enterprise Linux 8.2 / Test this media & install Red Hat Enterprise Linux ... appears, click tab key
     - It will show actuall command of those menu. For the Install (without Test) menu, the command is `vmlinuz initrd=initrd.img inst.stage2=hd:LABEL-RHEL-8-2-0-BasedOS-x86_64 quiet`
     - Adjust as `vmlinuz initrd=initrd.img inst.stage2=hd:LABEL-RHEL-8-2-0-BasedOS-x86_64 inst.dd=/dev/sda`
       - Removing quite will make the installation verbose, yielding more messages of status. Can check if legacy driver works
       - DD image may be mounted at /dev/sdb or /dev/sdb1. Confirmation is necessary

## When ctrl alt f123 doesn't wrk
- sudo systemctl set-default mult-user.target
- sudo reboot
- If gui login menu doesn't come:
  - sudo systemctl set-default graphical.target ; sudo reboot

## when firefox cannot open cross frame reference file in the local disk
- open about:config
- search origin
- adjust unique_oaque_origin and strict_origin_policy as false

## when gui is frozen
- from tty2
- init 3
- init 5

## when nfs or autofs is slow
- /etc/idmapd.conf
```
[General]
Cache-Expiration=10
Verbosity=5
Domain=my.network.local
Local-Realms = my.network.local, my.company.org, my.company.com
[Mapping]
Nobody-User = nobody
Nobody-Group = nobody
[Translation]
Method = nsswitch
```
- and disable [Static], [Umich_schema], LDAP_SERVER, LDAP_base
- sudo systemctl restart autofs

## when autofs mounted file shows `nobody:nobody`
- May need `echo "N" > /sys/module/nfsd/parameters/nfs4_disable_idmapping`
- In `/etc/idmapd.conf`,`Domain=localdomain`
- Reload using `systemctl restart nfs-idmapd.service; nfsidmap -vc; umount -a -t autofs; systemctl restart autofs`

## disable hibernation
- sudo systemctl mask sleep.target suspend.target hibernate.target hybrid-sleep.target

## installing libncurses5 for RHEL8
- RHEL8 comes with libncurses 6.
- Some app like ddt19 may look for libncurses 5. Then install `sudo yum install ncurses-compat-libs`

## When booting fails:
- For EFI booting:
  - After bios message, there are messages:
```
Could not create MokListRT: Out of Resources
Failed to set MokListRT: Out of Resources
Something has gone seriously wrong:  import_mok_state() failed: Out of Resources
```
- Ref: https://angrysysadmins.tech/index.php/2018/12/grassyloki/centos-7-failed-set-moklistrt/
- Using RHEL media, boot and rescue mode. Enter 1
  - This may take time if fsck runs. Alt-tab and check top if it runs
  - When system is loaded, chroot /mnt/sysimage; cd /boot/efi/EFI/red-hat ;cp grubx64.efi shimx64.efi; reboot
  - After rebooting, exclude shim* mokut* from /etc/yum.conf
  
## management of logical volume
- lsblk # find disk like /dev/sda, /dev/sdb, ...
- pvcreate /dev/sda ; pvdisplay # check if the volume is made
- vgcreate vg_satadisk /dev/sda; vgdisplay # check if the  volume group is produced
- lvcreate -l 100%FREE -n lv_localdisk vg_satadisk; lvdisplay # 100 usage of free space. check if the logical volume is produced
- mkfs.ext4 /dev/vg_satadisk/lv_localdisk # format as ext4
- Edit /etc/fstab
```
/dev/mapper/vg_satadisk-lv_localdata   /localmount  ext4   defaults  1 0
```
- mkdir /localmount
- mount /localmount
- To remove lv,vg,pv, use lvremove, vgremove, pvremove
  - How to delete opened LV: https://serverfault.com/questions/266697/cant-remove-open-logical-volume

## disabling SELinux
- Edit /etc/selinux/config and inject `disabled`
- Reboot

## installing SW using intel 2018 at RHEL8
- intel18 is not supported in RHEL8
- Error messsage: icpc has neither iostream nor iostream.h
- system gcc is 8.3 or 8.4 and you may need older gcc like 5.3
  - Download source and install from source. Patch might be necessary to build using system gcc
  - Set `INCLUDE`, `C_INCLUDE_PATH`, `CPLUS_INCLUDE_PATH` to have include folder of old gcc and intel compiler.

## when authentication window becomes unclicable or undismissable
- alt+F2, then enter 'r' then enter
- refresh the gnome GUI

## when libcrypto conflicts:
- Perforce, matlab?
- Error message: `symbol lookup error: /lib64/libk5crypto.so.3: undefined symbol:EVP_KDF_ctrl, version OPENSSL 1_1_10`
- Solution: disable or rename libcrypto.so.1.1 from lib folder of the application
