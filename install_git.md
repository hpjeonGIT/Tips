## 2.56 from github at Rocky8
- https://github.com/git/git
- sudo yum module install rust-toolchain # cargo is required
- sudo dnf install xmlto
- sudo dnf install dockbook2x # from EPEL. When install-info option is added
- sudo make prefix=/opt/git/2.56 install install-doc install-html install-python-script
  - install-html install-doc install-info are optional
  - install-python-script is necessary to build git-p4
  - git-p4 is found at 2.56/libexec/git-core/git-p4: `git p4 --help`
