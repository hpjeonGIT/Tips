## Testing latency b/w 2 nodes
- Prepare a template file
- bash orchestrator.sh
```sh
#!/bin/bash
for i in {004,005,006}
do 
echo -n "$i"
sed "s/XXX/${i}/" template > $i.host
mpirun -np 2 -machinefile ./$i.host /opt/osu_benchmark/bin/pt2pt/osu_latency |& tee log.$i
```
