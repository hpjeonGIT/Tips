- RHEL7 has PHP 5.x while GRAV requires PHP 7.1.X or newer
- Installing PHP7.3.8 from source may need libzip from source install
  - ./buildconf --force ; ./configure --prefix=/usr/local/apps/7/php/7.3.8 --disable-cgi --with-zlib --with-gettext --with-gdbm --with-sqlite3 --enable-sqlite-utf8 --enable-mbstring --enable-calendar --with-curl=/usr/lib --with-gd --with-jpeg-dir=/usr/lib64/libjpeg.so --with-png-dir=/usr/lib64/libpng.so --enable-soap --enable-bcmath --with-openssl --enable-ftp --with-libdir=lib64 --with-kerberos --enable-zip --with-libzip=/share/apps/7/libzip/1.5.2
- Unpack grav-admin-v1.6.9.zip and grav-v1.6.9.zip at $HOME/webroot/grav
  - grav for regular usage
    - No interactive editing
  - grav-admin for admin feature
- Starting GRAV
  - cd ~/webroot/grav/grav
  - Or
  - cd ~/webroot/grav/grav-admin
  - php -S ip_address:port_number system/router.php
  - Will need firewall setup using root: firewall-cmd --permanent --zone=public --add-port=1234-1239/tcp; firewall-cmd --reload
- In order to restart with cleaning cache
  - bin/grav clearcache then restart using php command
- Installing themes
  - Unzip learn2 theme then clean cache using grav cache command
  - Edit user/themes/learn2/css-compiled/theme.css, user/themes/learn2/scss/them/_fonts.scss and disable google fonts import
  -Enabling extra markdown
    - Edit user/config/system.yaml for extra: true
    - Not recommended to have extra markdown
- In learn2 theme, code block or fenced paragraph shows an indent at the first line
  - Quark theme is OK
  - No cause found. Installing hightlight plugin solves the problem including blank line issues

- Using anchor
  - In a page to be referred, add anchor as :  `<a name="paraview">ParaView</a>`
  - In a page to implant a link, add the link as : `[paraview](../../02.Mysw/default.md#paraview)`

- default webpage
  - When ip_address:port# yields 404 woops message
  - admin -> Configuration -> Content -> Redirect default route -> Yes

- Adding Grav into systemd service
    - /etc/systemd/system/grav.service
```
[Unit]
Description=Grav server
After=network.target
[Service]
Environment="LD_LIBRARY_PATH=/opt/libzip/1.9.2/lib64"
ExecStart=/opt/php/8.1.7/bin/php -S  11.22.33.44:5909 system/router.php
WorkingDirectory=/opt/grav/grav-admin
Restart=always
User=foo
[Install]
WantedBy=multi-user.target
```
  - sudo systemctl daemon-reload
  - sudo systemctl start grav
  - sudo systemctl enable grav
  - sudo systemctl status grav
