#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(int argc, char *argv[])
{
  clock_t cstart = clock();
  double *v1, *v2, x;
  int nmax = 10000, i, j, n;
  v1 = malloc(nmax*sizeof *v1);
  v2 = malloc(nmax*sizeof *v2);

  for (i=0;i<nmax;i++) {
    v1[i] = (double) rand();
    v2[i] = (double) rand();
  }

  x = 0.0;
  for (i=0;i<nmax;i++) {
    for (j=0;j<nmax;j++) {
      x += sin(v1[i] - v2[j]);
    }
  }

  free(v1);
  free(v2);

  printf("sum=%f\n",x);
  clock_t cend = clock();
  printf("Wall time = %f\n", (double) (cend - cstart)/(double) CLOCKS_PER_SEC);
  printf("Clocks per sec = %e\n", (double) CLOCKS_PER_SEC);
  
  return 0;
}
