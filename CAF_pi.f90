! For SMP
!ifort -coarray pi.f90
!export FOR_COARRAY_NUM_IMAGES=6
! For Distributed
! cat caf.conf
! -machinefile hosts -genvall -genv I_MPI_FABRICS shm:ofa -n 6  ./a.out
! ifort -coarray=distributed -coarray-config-file=caf.conf pi.f90
! ./a.out
!ref: http://pleiades.ucsc.edu/ams250/2017/lectures/Lecture-30-PGAS.pdf
program caf_pi
  implicit none
  integer :: j
  integer :: seed(2)
  integer*8 :: N_steps, i_step, hits
  double precision :: x, y
  double precision :: pi_sum, pi
  double precision :: pi_global[*]
  seed(1) = 17*this_image()
  if (this_image() == 1) then
     print*, 'num images = ', num_images()
  end if
  call random_seed(put=seed)
  hits = 0_8
  N_steps = 10000000_8
  do i_step=1_8, N_steps
     call random_number(x)
     call random_number(y)
     if ( (x*x + y*y) <= 1.d0) then
        hits = hits + 1_8
     endif
  enddo
  pi_global = 4.d0*dble(hits)/dble(N_steps)
  SYNC ALL
  if (this_image() == 1) then
     pi_sum = 0.d0
     do j=1,num_images()
        pi_sum = pi_sum + pi_global[j]
     enddo
     pi = pi_sum / num_images()
     print *, 'pi = ', pi
  endif
end program caf_pi
