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
## mobaXterm
- VNC is allowed in the session menu
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
- Then choose like `xrandr -s "1920x1080_60"` or `xrandr -s "640x480_75"`

## Conflict with Anaconda
- Ref: https://unix.stackexchange.com/questions/469909/vncviewer-errorcould-not-connect-to-session-bus-failed-to-connect-to-socket-tm
- Error message: could not connect to session bus :failed to connect to socket/tmp/dbus-XXXXXXXX connection refused
- Cause: anaconda runs dbus-daemon and this may conflict with VNC server
- Solution: disable anaconda setup ($PATH) in the .bashrc and restart the terminal/vncserver command
