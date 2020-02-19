# CPU Temperature using lm_sensors
- Ref: https://www.unixmen.com/write-nagios-plugin-using-bash-script/
- Find `https://github.com/jackbenny/check_temp/check_temp.sh`
- Copy to `/usr/lib64/nagios/plugins/`
- Adjust sensors command in the check_temp.sh such as
  - RHEL7/CENTOS7 : sensors |grep Package | awk -F '[ °C]' '{ sum+= $5 } END {print sum /NR}'
  - RHEL6/CENTOS6 : sensors |grep Physical | awk -F '[ °C]' '{ sum+= $4 } END {print sum /NR}'
    - Temperature data is averaged when “Physical” terms are triggered
  - TEMP=${TEMP%.*} # round to integer
- Double check if the command works
  - `bash ./check_temp.sh -w 92 -c 100`
    - Warning at 92 degree C and critical at 100 degree C

