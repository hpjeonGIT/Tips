## Using pre-built
- Download pre-built binary: http://portal.nersc.gov/project/visit/releases/2.13.3/visit2_13_3.linux-x86_64-rhel7-wmesa.tar.gz
- Download installation script:http://portal.nersc.gov/project/visit/releases/2.13.3/visit-install2_13_3
- bash visit-install2_13_3 2.13.3 linux-x86_64-rhel7-wmesa /share/apps/visit/2.13.3_mesa # Version number is provided using dot

## Using batch script
- Record the operation in an interactive mode: Commands -> Record -> do something /print screen -> Save
- Save the python steps into a new file. And import sys and sys.exit in the head/bottom of the script
- Run as visit -np 100 -machinefile hostlist -cli -nowin -s batch_visit.py
