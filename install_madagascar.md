## Installation steps for Ubuntu 24.04

1. download conda and install. Update $PATH to load python3 of conda
	- Must be older than 3.12 like 3.11 or 3.9 (imp package not compatible)
	- 2023.07 is confirmed to work
	- https://repo.anaconda.com/archive/
2. Download SCons (SCons-4.8.1.tar.gz) from sourceforge
3. unzip the source of SCons
4. at scons-4.8.1, `python3 setup.py install`
5. `sudo apt install libXaw-dev` (for sfpen build)
5. download madagascar 4.0 from sourceforge then unzip
```
./configure --prefix=~/sw_local/mada_4.0
make install
```
6. Testing
```
source ~/sw_local/mada_4.0/share/madagascar/etc/env.sh
cd ~/TEMP
sfspike n1=1000 k1=300 > spike.rsf
sfin spike.rsf
sfattr < spike.rsf
sfbandpass fhi=2 phase=y < spike.rsf > filter.rsf
sfwiggle clip=0.02 title="Welcome to Madagascar" < filter.rsf > filter.vpl
sfpen < filter.vpl
```
7. Ref: https://ahay.org/wiki/Installation
