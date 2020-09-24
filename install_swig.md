./configure --prefix=/usr/nic/apps/swig/3.0.12  --with-boost=/share/libs/boost/1.68.0_gcc485/ \
--with-python=/share/apps/python_da/2.7.15/ --with-python3=/share/apps/python_custom/3.6.6/ \
--with-ruby=/share/apps/ruby/2.5.1

# Loading C++ shared library in the python interface
- If the update of LD_LIBRARY_PATH is not helping to remove undefined symbols error when import XXX, then use LD_PRELOAD
