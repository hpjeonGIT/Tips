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
