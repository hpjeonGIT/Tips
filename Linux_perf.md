## Using perf to count cycles/insructions retired
- sudo yum install perf
- perf stat -e cpu-cycles,instructions ./a.out
