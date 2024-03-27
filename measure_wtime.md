## In C
```c
clock_t t0,t1;
t0 = clock();
...
t1 = clock();
printf("Took = %4.6f sec\n", (double)((double)(t1-t0)/CLOCKS_PER_SEC));
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
cat("Took ", t1 - t0, "sec\n")
```

## In Python
```python
import time
t0 = time.time()
...
t1 = time.time()
print("Took ", t1-t0, "sec\n")
```

## In Matlab
```matlab
tic
...
toc
```

## In Java
```Java
long t0 = System.currentTimeMillis();
...
long t1 = System.currentTimeMillis();
System.out.print("Took " + (t1-t0) +  "mseconds\n");
```

## In Javascript
```javascript
let t0, t1;
t0 = new Date();
...
t1 = new Date();
alert("Took" + (t1-t0) + "mseconds");
```
## In GoLang
```go
...
import ( "fmt" ; "time" )
...
var t0 time.Time
t0 = time.Now()
...
fmt.Println("Took " + time.Since(t0).String())
```

## In Ruby
```ruby
t0 = Time.now
t1 = Time.now
print("Took " , t1-t0 ,"seconds\n")
```

## In Julia
```julia
@time ... # do something
```

## In Perl
```Perl
use Time::HiRes qw (time);
...
my $t0 = time();
...
my $t1 = time();
printf("Took %.2f sec\n", $t1-$t0);
```
