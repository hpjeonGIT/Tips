## installing on RHEL8.X
- mount iso and copy all files to local disk
- bash install # GUI will appear
  - If  there is an error message of `unable to launch matlabwindow application`: https://www.mathworks.com/matlabcentral/answers/513449-what-unable-to-launch-the-matlabwindow-application-during-installation
  - Rename or remove bin/glnxa64/librypto.so.1.1
- For silent or CLI installation without GUI
  - Using `installer_input.txt` as a template, make a new txt file having install information
  - bash install -inputFile installer_input.txt

## activation or adding individual license
1. May copy individual license into ~/.matlab/R202XX_licenses/ folder
2. GUI: `/opt/matlab/202X/bin/activate_matlab.sh` then enter info as necessary
3. CLI or silent: `/opt/matlab/202X/bin/activate_matlab.sh -propertyFile ./activate.ini -v`
- Sample `activate.ini`:
```
isSilent=true
activateCommand=activateOffline
licenseFile=/somewhere/license.lic
activationKey=xx-xx-xx-xx
installLicenseFileDir=
```
- Depending on the method of activation - offline or activationkey or installLicenseFile, the file may change
