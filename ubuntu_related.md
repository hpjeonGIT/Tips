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
