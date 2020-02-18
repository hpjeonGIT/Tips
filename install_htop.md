# download source tar
- If download from github, autogen.sh needs to run
- source tar will need configure only
- If `onfigure: error: You may want to use --disable-unicode or install libncursesw.`
  - Add --disable-unicode
- If -lncurses is not found,
  - Use LDFLAGS as `export LDFLAGS="-L/opt/ncurses_6.2/lib -lncurses"`
  - LD_LIBRARY_PATH will need update
