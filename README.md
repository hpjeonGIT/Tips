# Tips

### multi_block.xmf
... An example of distributed parallel visualization.
... Among 200x3 position data, 100x3 and 100x3 are splitted and each of two processors in paraviewl will be responsible for each block.

### installation note
libunwind: ./configure --prefix /home/hpjeon/hw/libunwind

mpiP: ./configure --prefix=/home/hpjeon/hw/mpiP --with-cc=mpicc --with-f77=mpifort
 CFLAGS=-I/home/hpjeon/hw/libunwind/include LDFLAGS=-L/home/hpjeon/hw/libunwind/
lib --enable-collective-report-default

## References
- CUDA: https://people.maths.ox.ac.uk/gilesm/cuda/lecs/lecs.pdf


## download all git repositories of a user
```
for i in `curl -s https://api.github.com/users/hpjeonGIT/repos?per_page=1000 |grep git_url |awk '{print $2}'| sed 's/"\(.*\)",/\1/'`; do  git clone $i;  done
```
## Using https for git
- When ssh key authentication fails
- One time activity
 - Make a dummy project
 - cd some_folder
 - git pull https://github.com/.../myproject.git
 - This download all the git setup as well
- Backup activity
 - cd some_folder
 - git add *; git commit -m "my commit"
 - git push --set-upstream https://github.com/.../myproject.git master
 - When total file size > 1MB, gitlab may not upload. Check configuration

## pdsh command
- shell command for multiple nodes
- When there are cluster1, cluster2, ... cluster99 nodes,
 - `pdsh -w cluster[1-99] uptime`
 
 ## ssh key renew
- Delete or backup old .ssh folder
- `ssh-keygen;cd .ssh; echo “StrictHostKeyChecking no” > config; cat id_rsa.pub > authorized_keys; chmod 600 authorized_keys`
- Run pdsh all nodes to update ssh key
