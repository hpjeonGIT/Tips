#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

int main(int argc, char *argv[])
{
  double cstart = omp_get_wtime();
  double *v1, *v2, x;
  int nmax = 10000, i, j, n;
  v1 = malloc(nmax*sizeof *v1);
  v2 = malloc(nmax*sizeof *v2);

  for (i=0;i<nmax;i++) {
    v1[i] = (double) rand();
    v2[i] = (double) rand();
  }

  x = 0.0;
# pragma omp parallel for shared(v1,v2,nmax) private(i,j)\
  reduction(+:x)
  for (i=0;i<nmax;i++) {
    for (j=0;j<nmax;j++) {
      x += sin(v1[i] - v2[j]);
    }
  }

  free(v1);
  free(v2);

  printf("sum=%f\n",x);
  double cend = omp_get_wtime();
  printf("Wall time = %f\n", cend - cstart);
  printf("Clocks per sec = %e\n", (double) CLOCKS_PER_SEC);
  
  return 0;
}
