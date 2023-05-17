# Adding or replacing a new gpu card
- BIOS setup: disable secure boot + enable multigpu if available
- shutdown and add/replace a GPU card
- Reboot
- Install drivers
- Ref: https://gist.github.com/wangruohui/df039f0dc434d6486f5d4d098aa52d07
  - /etc/modprobe.d/blacklist-nouveau.conf 
```  
blacklist nouveau
options nouveau modeset=0
```
  - sudo update-initramfs -u; reboot
  - sudo systemctl stop lightdm
  - sudo bash NVIDIA-Linux-x86_64-430.50.run --dkms -s --no-opengl-files ; reboot
  - sudo apt  install nvidia-prime mesa-utils ; sudo prime-select  nvidia

# proprietary driver
- bash nvidia-**.sh
- To remove, nvidia-installer --uninstall
- May not be recommended to use in ubuntu


# update of library for developers
- sudo apt update
- sudo apt install m4 autotools-dev automake libtool libtirpc-dev gettext make gcc gfortran environment-modules bison flex

# VNC for ubuntu
- tigervnc/tightvnc didn't work appropriately for Ubuntu20.04
- Use TurboVNC. Download deb from sourceforge. Download virtualGL deb as well
- GDB didn't work well. Let's use mate session
- sudo apt install ubuntu-mat-desktop
- Edit ~/.vnc/xstartup.turbovnc
```
#!/bin/sh
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
/usr/bin/mate-session
```
- /opt/TurboVNC/bin/vncserver
- /opt/TurboVNC/bin/vncserver -list
- /opt/TurboVNC/bin/vncserver -kill :1

# setup one gpu for display and the 2nd for CUDA only
- Ref: jonasadler.com/post/install_cuda
- sudo nvidia-xconfig -multigpu=on
- Edit /etc/X11/xorg.conf
    - `BusID "PCI:3:0:0"` # PCI ID is found from nvidia-smi
- Reboot

# When there are too many gnome-shell or system is slow
- https://askubuntu.com/questions/1036441/ubuntu-18-04-gnome-shell-high-cpu-usage
- gsettings set org.gnome.desktop.interface  clock-show-seconds false

# Installing hplib at Ubuntu20
- Install pyqt5
- Download hplip-3.23.3.run
- sudo apt install python-is-python3
- sudo bash ./hplip-3.23.3.run 

# installing openssl 1.1.0 at ubuntu20
- perl5 is too new. Use perl5.26 or old

# Perforce 2021 at Ubuntu20
- Deployed libssl.so not matching with system libcrypto. Just rename or remove the enclosed libssl.so and let perforce use the system libss.so
