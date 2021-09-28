## for RHEL/CENTOS 8.x
- Download meson source from PyPi and install on python3
- download and install the rpm of ninja-build from EPEL or pkgs.org
```
yum install atk-devel
yum install gtk3-devel
```
- Untar ghex source
```
meson --prefix /opt/ghex/3.18.4 ghex-3.18.4
meson compile
meson install
```
- To use:
```
export XDG_DATA_DIRS+=:/opt/ghex/3.18.4/share
ghex
```
