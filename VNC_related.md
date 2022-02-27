## TurboVNC
- When not working, getting log file
- "C:\Program Files"\TurboVNC\vncviewer.exe /help
- "C:\Program Files"\TurboVNC\vncviewer.exe server_name :display_number /loglevel 13 /logfile c:\TEMP\my_vnc.log
```
Started and Winsock (v 2) initialised
WinTab library not available # might be ignored
Buffer size expanded to 4352
Registered connection with app
```
- vncserver might be activated from putty. After vncserver is activated, if TurboVNC yields an error message of Could not open display :0, `unset XDG_VTNR`

## mobaXterm
- VNC is allowed in the session menu
  - May use `Connect through SSH gateway`. This will not need firewall setup as ssh port is used
- To use ssh tunneling, display number(:1) shouldn't use in the ip menu. Instead change the port number such as 5900+1 = 5901
- Resolution is not changed dynamically as TurboVNC does. Adjust using -geometry when VNC is initiated or use xrandr command
```
   1920x1080     60.00*+
   1680x1050     59.95  
   1600x900      60.00  
   1280x1024     75.02    60.02  
   1440x900      59.89  
   1280x800      59.81  
```
- Then choose like `xrandr -s "1920x1080_60"` or `xrandr -s "640x480_75"` or `xrandr -s 1600x1050`
- If VNC is from RHEL6, virtualGL or `vglrun` might be necessary to run 3D graphics applications


## Conflict with Anaconda
- Ref: https://unix.stackexchange.com/questions/469909/vncviewer-errorcould-not-connect-to-session-bus-failed-to-connect-to-socket-tm
- Error message: could not connect to session bus :failed to connect to socket/tmp/dbus-XXXXXXXX connection refused
- Cause: anaconda runs dbus-daemon and this may conflict with VNC server
- Solution: disable anaconda setup ($PATH) in the .bashrc and restart the terminal/vncserver command

## when mouse grabbing crashes VNC (mobaxterm or turbovnc)
- Ref: https://github.com/neutrinolabs/xrdp/issues/755
- May need to update rdp?
- Or run vncconfig
  - Disable 1) Also set primary selection 2) Send primary selection to viewers

## vnc setup using systemd
- vncserver will be deprecated. Migration to system service is necessary in near future
- Ref: https://www.ibm.com/support/pages/how-configure-vnc-server-red-hat-enterprise-linux-8
- `cp /lib/systemd/system/vncserver@.service /etc/systemd/system/vncserver@:3.service`
  - No edit required
- `vi /etc/tigervnc/vncserver.users`
  - Add `:3=USERname`
- sudo -u USERname; vncpasswd; # or the USERname has configured vncpasswd already
- `sudo systemctl start vncserver@:3.service`
- `sudo systemctl enable vncserver@:3.service` # now restarts at reboot
- As shown above, a user will not be able to launch vnc service anymore. Must be registered by admin and the display port will be given
