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
## Alias in module
- Regular csh grammar may not work
```
#%Module1.0#####################################################################
##
##
proc ModulesHelp { } {
        puts stderr "ANTLR4"
}
#
module-whatis   "antlr4 and antlrworks"
#
# for Tcl script use only
set     topdir          /home/hpjeon/sw_local/antrl4
set     version         4.7.1
set     sys             linux86_64
#
set LOCALPATH .:${topdir}/antlr-4.7.1-complete.jar
prepend-path   CLASSPATH $LOCALPATH
set-alias antlr4 "java -Xmx500M -cp ${topdir}/antlr-4.7.1-complete.jar:${LOCALPATH}"
set-alias grun "java org.antlr.v4.runtime.misc.TestRig"
```

## Updating MODULEPATH
- Instead of MODULEPATH, users may use the absolute path like `module load /opt/modulefiles/gcc/11.3`
- `export MODULEPATH=$MODULEPATH:/home/myaccount/private_modules` might be located in ~/.bashrc
- To apply global MODULEPATH, edit `/etc/environment-modules/modulespath` file. The default is `/usr/share/Modules/modulefiles:/etc/modulefiles:/usr/share/modulefiles`

## module command in Cray environment
- `module` is not an actual command but an alias
- Or defined as a function in the shell script. See : https://stackoverflow.com/questions/51192351/adapting-module-alias-invoking-modulecmd-from-tcsh-to-bash
    - In bash: module() { eval "$(/app/modules/0/bin/modulecmd bash "$@")"; }
    - In csh: alias module 'eval `/app/modules/0/bin/modulecmd tcsh \!*`'
