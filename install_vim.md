## vim with Python3 support
```
./configure --prefix=/share/apps/vim/8.X --disable-nls --enable-cscope --enable-gui=no --enable-multibyte --enable-python3interp=yes \
--with-feature=huge --with-python3-command=/share/apps/python/3.6/bin/python3 --with-tlib=ncurses --without-x
make -j 10
make install
```
- If ycmd crashes, re-configure with `--enable-python3interp=dynamic`
- At RHEL8.4, it needs the location of python config directory. Append following: `--with-python3-config-dir=/sare/apps/python/3.6/lib/python3.6/config-3.6m-x86_64-linux-gnu`
- After `make -j10;make install;` run `vim --version` and check if `+python3` or `-python3` is found.

### YouCompleteMe package with vim
- no rpm or debian package. Installed at individual home folder
- Download or install Vundle at `~/.vim/bundle`
  - https://github.com/VundleVim/Vundle.vim
  - When unpack the zip, it will be Vundle.vim-XXX. Rename the folder as Vundle.vim. Final form will be ~/.vim/bundle/Vundle.vim
- Download and untar YouCompleteMe source at `~/.vim/bundle/YouCompleteMe`
- llvm (clang must be enabled) and gcc (>8.x) are required
- vim must be compiled with python3 support
- `cd ~/.vim/bundle/YouCompleteMe`
- `CC=/share/apps/gcc/8.4/bin/gcc CXX=/share/apps/gcc/8.4/bin/g++ python3 install.py`
  - Auto completion for regular files
- `CC=/share/apps/gcc/8.4/bin/gcc CXX=/share/apps/gcc/8.4/bin/g++ python3 install.py --clang-completer --system-libclang`
  - Auto completion for c family
  - If `--system-libclang` is not given, it will try to download clang libs
- `dos2unix ~/.vim/bundle/YouCompleteMe/plugin/youcompleteme.vim`
- `dos2unix ~/.vim/bundle/YouCompleteMe/autoload/youcompleteme.vim`
- Edit `~/.vimrc`
```
set nocompatible              " be iMproved, required
filetype off                  " required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
Plugin 'VundleVim/Vundle.vim'
Plugin 'Valloric/YouCompleteMe'
call vundle#end()            " required
filetype plugin indent on    " required
set nocompatible
filetype on
```
- Libraries of gcc/llvm/clang/python must exist in `LD_LIBRARY_PATH`
- Run vim, and `:YcmDiags` for diagnosis message. Or `:YcmComplete` shows the status
- Error message will be shown at /tmp/*.log files
- At RHEL8.4, PYTHONPATH needs the lib-dynload like `PYTHONPATH=/share/apps/python/3.6.8/lib/python3.6/lib/python3.6:/share/apps/python/3.6.8/lib/python3.6/lib/python3.6/site-packages:/share/apps/python/3.6.8/lib/python3.6/lib/python3.6/lib-dynload`
