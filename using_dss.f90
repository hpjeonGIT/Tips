program using_dss
  IMPLICIT NONE
  include 'mkl_dss.fi'
  INTEGER, PARAMETER :: dp = KIND(1.0D0)
  !.. All other variables
  INTEGER error, N,NRHS
  INTEGER, ALLOCATABLE :: ia(:), ja(:), jx(:)
  REAL(KIND=DP), ALLOCATABLE :: aa(:), A(:,:), ax(:), B(:), x(:)
  INTEGER:: i, idum(1),j, jcnt, ierr
  INTEGER*8:: handle
  REAL(KIND=DP) ddum(1)

  N = 16
  allocate(A(N,N), ax(N*N), ia(N+1), jx(N*N), B(N), x(N), stat=ierr)
  A = reshape ((/3.4225E-08,-1.7112E-08,0,0,-1.7113E-08,0,0,0,0,0,0,0,0,0,0,0, &
     & -1.7112E-08,3.4223E-08,-1.7112E-08,0,0,-1.225E-15,0,0,0,0,0,0,0,0,0,0, &
     & 0,-1.7112E-08,5.1337E-08,-1.7112E-08,0,0,-1.7113E-08,0,0,0,0,0,0,0,0,0,&
     & 0,0,-1.7112E-08,3.4225E-08,0,0,0,-1.7113E-08,0,0,0,0,0,0,0,0,&
     & -1.7113E-08,0,0,0,3.4228E-08,-1.225E-15,0,0,-1.7115E-08,0,0,0,0,0,0,0,&
     & 0,-1.225E-15,0,0,-1.225E-15,4.9E-15,-1.225E-15,0,0,-1.225E-15,0,0,0,0,0,0,&
     & 0,0,-1.7113E-08,0,0,-1.225E-15,5.1341E-08,-1.7113E-08,0,0,-1.7115E-08,0,0,0,0,0,&
     & 0,0,0,-1.7113E-08,0,0,-1.7113E-08,5.1341E-08,0,0,0,-1.7115E-08,0,0,0,0,&
     & 0,0,0,0,-1.7115E-08,0,0,0,5.1344E-08,-1.7114E-08,0,0,-1.7115E-08,0,0,0,&
     & 0,0,0,0,0,-1.225E-15,0,0,-1.7114E-08,5.1343E-08,-1.7114E-08,0,0,-1.7115E-08,0,0,&
     & 0,0,0,0,0,0,-1.7115E-08,0,0,-1.7114E-08,6.8457E-08,-1.7114E-08,0,0,-1.7115E-08,0,&
     & 0,0,0,0,0,0,0,-1.7115E-08,0,0,-1.7114E-08,5.1343E-08,0,0,0,-1.7115E-08,&
     & 0,0,0,0,0,0,0,0,-1.7115E-08,0,0,0,5.7048E-08,-2.2819E-08,0,0,&
     & 0,0,0,0,0,0,0,0,0,-1.7115E-08,0,0,-2.2819E-08,7.9867E-08,-2.2819E-08,0,&
     & 0,0,0,0,0,0,0,0,0,0,-1.7115E-08,0,0,-2.2819E-08,7.9866E-08,-2.2818E-08,&
     & 0,0,0,0,0,0,0,0,0,0,0,-1.7115E-08,0,0,-2.2818E-08,5.7047E-08/), (/N,N/))
  B = reshape((/2.538E-09, 2.538E-09, 2.538E-09, 2.538E-09, 2.538E-09, 2.538E-09,&
     & 2.538E-09, 2.538E-09, 2.538E-09, 2.538E-09, 2.538E-09, 2.538E-09, &
     & 2.538E-09, 2.538E-09, 2.538E-09, 2.538E-09/), (/16/))

  jcnt = 0
  do i=1, N
     ia(i) = jcnt + 1
     do j=i, N
        if (dabs(A(i,j)) > 1.e-20 .or. i==j) then
           jcnt = jcnt + 1
           ax(jcnt) = A(i,j)
           jx(jcnt) = j
        end if
     end do
  end do
  ia(N+1) = jcnt + 1

  allocate(ja(jcnt), aa(jcnt))
  ja(1:jcnt) = jx(1:jcnt)
  aa(1:jcnt) = ax(1:jcnt)
  deallocate(jx,ax)
  allocate(x(N), stat=ierr)

  NRHS = 1
  error = dss_create(handle, MKL_DSS_DEFAULTS)
  error = dss_define_structure( handle, MKL_DSS_SYMMETRIC, &
       &  ia, N, N,  ja, jcnt)
  error = dss_reorder( handle, MKL_DSS_DEFAULTS, idum)
  error = dss_factor_real( handle, MKL_DSS_DEFAULTS, aa)
  error = dss_solve_real( handle, MKL_DSS_DEFAULTS, B, nRhs,  x)
  error = dss_delete( handle, MKL_DSS_DEFAULTS )
  print *, x
  print *, matmul(A,x)
  deallocate(x, A, aa, ia, ja, B, stat=ierr)
end program using_dss
