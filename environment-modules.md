# In Ubuntu 16.X
- Ref: https://askubuntu.com/questions/343692/module-load-command-does-not-work
- sudo apt-get install environment-modules
- Edit ~/.bashrc
```
module() { eval `/usr/bin/modulecmd bash $*`; }
export MODULEPATH=/home/hpjeon/sw_local/modulefiles
```
- Edit ~/sw_local/modulefiles/python/3.8.1
```
#%Module1.0#####################################################################
##
##
proc ModulesHelp { } {
        puts stderr "Python/3.8.1"
}

module-whatis   "Python/3.8.1"

# for Tcl script use only
set     topdir          /home/hpjeon/sw_local/python/3.8.1
set     version         3.8.1
set     sys             linux86_64

setenv   PYTHON_HOME            $topdir
prepend-path    PATH            $topdir/bin
prepend-path    MANPATH         $topdir/man
prepend-path    LD_LIBRARY_PATH $topdir/lib
prepend-path    CPATH           $topdir/include
```
- Open a new terminal. Now `module av` works
```
$ module av

---------------------- /home/hpjeon/sw_local/modulefiles -----------------------
python/3.8.1
```
