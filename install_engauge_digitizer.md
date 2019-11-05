# RHEL7
- sudo yum install qt5-qtbase-devel
  - May need other qt5 libraries
- Install FFTW3
- export FFTW_HOME=...
- qmake-qt5 engauge.pro CONFIG+=log4cpp_null
  - Default qmake in RHEL7 is qt3.3
- make  
