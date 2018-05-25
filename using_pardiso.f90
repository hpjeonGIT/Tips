include 'mkl_pardiso.f90'
program using_pardiso
  use mkl_pardiso
  IMPLICIT NONE
  INTEGER, PARAMETER :: dp = KIND(1.0D0)
  TYPE(MKL_PARDISO_HANDLE), ALLOCATABLE  :: pt(:)
  INTEGER maxfct, mnum, mtype, phase, n, nrhs, error, msglvl
  INTEGER, ALLOCATABLE :: iparm(:), ia(:), ja(:), jx(:)
  REAL(KIND=DP), ALLOCATABLE :: aa(:), A(:,:), ax(:), B(:), x(:)
  INTEGER:: i, idum(1),j, jcnt, ierr
  REAL(KIND=DP) ddum(1), z
  
  z = 0.0_dp
  N = 16
  allocate(A(N,N), ax(N*N), ia(N+1), jx(N*N), B(N), stat=ierr)

  ! banded matrix - depends on the problem
  A = reshape ((/5.37D-05,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,&
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0, &
       & -1.79D-05,1.0D+03,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,&
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,&
       & 0.0D+0,-1.79D-05,7.16D-05,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,&
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,&
       & 0.0D+0,0.0D+0,-1.79D-05,5.37D-05,0.0D+0,0.0D+0,0.0D+0,-1.79D-05, &
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,&
       & -1.79D-05,0.0D+0,0.0D+0,0.0D+0,5.37D-05,-1.79D-05,0.0D+0,0.0D+0, &
       & -1.79D-05,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,&
       & 0.0D+0,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,1.0D+03,-1.79D-05,0.0D+0,&
       & 0.0D+0,-1.79D-05,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0, &
       & 0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,7.16D-05,-1.79D-05,&
       & 0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0, &
       & 0.0D+0,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,5.37D-05,&
       & 0.0D+0,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,0.0D+0,0.0D+0,&
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,0.0D+0,5.37D-05,&
       & -1.79D-05,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,0.0D+0,&
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,&
       & 7.16D-05,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,&
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,&
       & -1.79D-05,7.16D-05,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,&
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,-1.79D-05,0.0D+0,&
       & 0.0D+0,-1.79D-05,5.37D-05,0.0D+0,0.0D+0,0.0D+0,-1.79D-05,& 
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,-1.79D-05,&
       & 0.0D+0,0.0D+0,0.0D+0,3.58D-05,-1.79D-05,0.0D+0,0.0D+0, &
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0, & 
       & -1.79D-05,0.0D+0,0.0D+0,-1.79D-05,5.37D-05,-1.79D-05,0.0D+0, &
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,&
       & 0.0D+0,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,5.37D-05,-1.79D-05,&
       & 0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,0.0D+0,&
       & 0.0D+0,0.0D+0,-1.79D-05,0.0D+0,0.0D+0,-1.79D-05,3.58D-05/), (/N,N/))
  B = reshape((/ -3.78D-10,1.02D-09,-4.06D-10,-3.98D-11,-3.43D-11,-4.18D-18,&
       & -2.24D-10,1.00D-10,1.18D-10,-5.71D-10,2.55D-10,1.38D-11,-1.27D-11,&
       & 2.88D-10,4.52D-12,-8.84D-11 /), (/16/))

! Making CSR format: https://en.wikipedia.org/wiki/Sparse_matrix
  jcnt = 0
  do i=1, N
     ia(i) = jcnt + 1
     do j=1, N ! asymmetric matrix
        if (dabs(A(i,j)) > 1.e-30 .or. i==j) then
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
  allocate(pt(64), iparm(64),x(N), stat=ierr)
  DO i = 1, 64
     pt(i)%DUMMY =  0 
  END DO
  
  nrhs = 1
  maxfct = 1
  mnum = 1
  iparm = 0
  iparm(1) = 1 ! no solver default
  iparm(2) = 2 ! fill-in reordering from METIS
  iparm(3) = 1 ! OMP_NUM_THREADS
  iparm(6) = 0
  iparm(10) = 13 ! perturbe the pivot elements with 1E-13
  iparm(11) = 1 ! use nonsymmetric permutation and scaling MPS
  iparm(13) = 2 ! use nonsymmetric permutation and scaling MPS
  iparm(18) = -1 ! Output: number of nonzeros in the factor LU
  iparm(19) = -1 ! Output: Mflops for LU factorization  !
  iparm(21) = 1
  error = 0 ! initialize error flag
  msglvl = 1 ! print statistical information = 1
  mtype = 11 ! 1 for real/symm, 2 for real/symm/pos def, -2 for real/sym/indef
  phase = 11 ! only reordering and symbolic factorization
  call pardiso(pt, maxfct, mnum, mtype, phase, n, aa, ia, ja, &
       & idum, nrhs, iparm, msglvl, ddum, ddum, error)
  WRITE(*,*) 'Reordering completed ... '
  IF (error .NE. 0) THEN
     WRITE(*,*) 'The following ERROR was detected: ', error
     STOP
  END IF
   phase = 22 ! only factorization
  CALL pardiso (pt, maxfct, mnum, mtype, phase, n, aa, ia, ja, &
       & idum, nrhs, iparm, msglvl, ddum, ddum, error)
  iparm(8) = 15 ! max numbers of iterative refinement steps
  phase = 33 ! only factorization
  CALL pardiso (pt, maxfct, mnum, mtype, phase, n, aa, ia, ja, &
       & idum, nrhs, iparm, msglvl, b, x, error)
  phase = -1 ! release internal memory
  CALL pardiso (pt, maxfct, mnum, mtype, phase, n, ddum, idum, &
       & idum,idum, nrhs, iparm, msglvl, ddum, ddum, error)
     
  WRITE(*,*) 'The solution of the system is '
  DO i = 1, n
     WRITE(*,*)  x(i)
  END DO

  print *, matmul(A, x)
end program using_pardiso
