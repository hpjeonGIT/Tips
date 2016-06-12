#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

double rand_double()
{
  return (double) rand()/(double) RAND_MAX;
}

int main()
{
  clock_t s_time, e_time;
  int i, j, nmax=10000;
  double a=3.41, b=7.25, c=1.41487;
  double *v1, *v2, x, dx;
  v1 = malloc(nmax*sizeof *v1);
  v2 = malloc(nmax*sizeof *v2);
  for (i=0;i<nmax;i++){
    v1[i] = rand_double();
    v2[i] = rand_double();    
  }

 

  // default
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += dx;
    }
  }
  e_time = clock();
  printf("default sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);

  // 2x
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += dx*dx;
    }
  }
  e_time = clock();
  printf("multi sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);
  
  // pow(2)
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += pow(dx,2);
    }
  }
  e_time = clock();
  printf("pow 2 sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);
  
  
  // pow(2.1)
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += pow(dx,2.1);
    }
  }
  e_time = clock();
  printf("pow 2.1 sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);

  
  // exp 
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += exp(-dx);
    }
  }
  e_time = clock();
  printf("exp sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);
  
  // sin
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += sin(-dx);
    }
  }
  e_time = clock();
  printf("sin sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);

  // regular equation
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += a*pow(dx,4) + b*pow(dx,2) + c*dx;
    }
  }
  e_time = clock();
  printf("regular eqn sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);

  // expanded equation
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += a*dx*dx*dx*dx + b*dx*dx + c*dx;
    }
  }
  e_time = clock();
  printf("expanded eqn sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);

  
 // optimized equation
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += ((a*dx*dx + b)*dx + c)*dx;
    }
  }
  e_time = clock();
  printf("optimized eqn sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);

  // 2nd optimized equation
  s_time = clock();
  x = 0.0;
  for (i=0;i<nmax;i++){
    for (j=0;j<nmax;j++) {
      dx = abs(v1[i] - v2[j]);
      x += c*dx;
      dx = dx*dx;
      x += dx*(b + dx*a);
    }
  }
  e_time = clock();
  printf("2nd optimized eqn sum %f %f \n", (e_time - s_time)/(double) CLOCKS_PER_SEC, x);

  free(v1);
  free(v2);
  return 0;
}
