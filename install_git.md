## 2.56 from github at Rocky8
- https://github.com/git/git
- sudo yum module install rust-toolchain # cargo is required
- sudo dnf install xmlto
- sudo dnf install dockbook2x # from EPEL. When install-info option is added
- sudo make prefix=/opt/git/2.56 install install-doc install-html install-python-script
  - install-html install-doc install-info are optional
  - install-python-script is necessary to build git-p4
  - git-p4 is found at 2.56/libexec/git-core/git-p4: `git p4 --help`
  - Update the python path in the first line of git-4 then you will not need python module 

### 2.33 doesn't need rust-toolchain

## Handshake b/w git and p4
1. Create a git project at a remote server or host on github/gitlab
- For a local git server:
```bash
mkdir /srv/git/Project1.dir
cd /srv/git/Project1.dir
git init --bare
```
2. Build a local repo in a workstation/PC
```bash
export P4PORT=...
export P4USER=...
export P4CLIENT=...
module load perforce git
mkdir handshake; cd handshake
git p4 clone --verbose //depot/some_project
cd some_project
git remote add git_origin git@git.server:/srv/git/Project1.git
git config git-p4.skipSubmitEdit true
git p4 rebase
git push git_origin main
```
3. The git server is updated by someone else. How to update p4?
```bash
git p4 rebase
git fetch git_origin
git checkout main
git cherry-pck <last_commit>..git_origin/main
git p4 submit
```
4. P4 is updated by someone else. How to update the remote git?
```bash
git pull git_origin main
git p4 sync
git p4 rebase
git push git_origin main
```
