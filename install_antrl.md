## Antlr tool using java
- wget http://www.antlr.org/download/antlr-4.8-complete.jar
- Download C++ target source code from https://www.antlr3.org/works/
  - Unzip and cd runtime/Cpp
  - cmake .. -DANTLR_JAR_LOCATION=/home/hpjeon/sw_local/antlr4/antlr-4.8-complete.jar \
  -DWITH_DEMO=True -DCMAKE_INSTALL_PREFIX=/home/hpjeon/sw_local/antlr4
    - If 'uuid' is not found message from CMake, then `sudo apt-get install uuid-dev`
  - make -j 4; make install    
- Sample module file
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
set     version         4.8
set     sys             linux86_64
#
set LOCALPATH .:${topdir}/antlr-4.8-complete.jar
prepend-path CLASSPATH        $LOCALPATH
prepend-path LD_LIBRARY_PATH  $topdir/lib
prepend-path CPATH            $topdir/include/antlr4-runtime
prepend-path CXX_INCLUDE_PATH $topdir/include/antlr4-runtime
set-alias antlr4 "java -Xmx500M -cp ${topdir}/antlr-4.8-complete.jar:${LOCALPATH} org.antlr.v4.Tool"
set-alias grun "java org.antlr.v4.runtime.misc.TestRig"
```

## Using ANTLR4
- antlr4 -Dlanguage=Cpp calc2.g4
  - calc2.g4 must define grammar name as calc2

## Antlr gui
- Download Linux version from https://www.antlr3.org/works/
