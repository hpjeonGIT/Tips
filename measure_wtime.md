## In C
```c
clock_t t0,t1;
t0 = clock();
...
t1 = clock();
printf("Sum array CPU wall time = %4.6f\n",
      (double)((double)(t1-t0)/CLOCKS_PER_SEC));
```

## In C using OpenMP
```c
double t0,t1;
t0 = omp_get_wtime(); 
...
t1 = omp_get_wtime(); 
printf("Took %f seconds\n", t1-t0);
```

## In C using MPI
```c
double t0,t1;
t0 = MPI_Wtime();
...
t1 = MPI_Wtime();
printf("Took %f seconds\n",t1-t0);
```

## In fortran
```fortran
real:: t0,t1,t2,secnds
t0 = 0.0
t1 = secnds(t0)
...
t2 = secnds(t1)
print *, t2
```

## In R
```R
t0 <- Sys.time()
...
t1 <- Sys.time()
cat(t1 - t0)
```

## In Python
```python
import time
t0 = time.time()
...
t1 = time.time()
print(t1-t0)
```

## In Matlab
```
tic
...
toc
```
