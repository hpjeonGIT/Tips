Variable range check
```
program real_kinds
  integer,parameter :: p6 = selected_real_kind(7)
  integer,parameter :: p10r100 = selected_real_kind(10,100)
  integer,parameter :: r400 = selected_real_kind(r=400)
  integer, parameter:: i3 = selected_int_kind(3)
  integer, parameter:: i5 = selected_int_kind(5)
 integer, parameter:: i8 = selected_int_kind(8)
 integer, parameter:: i10 = selected_int_kind(10)
 integer, parameter:: i15 = selected_int_kind(15)


  real(kind=p6) :: x
  real(kind=p10r100) :: y
  real(kind=r400) :: z
  integer(kind=i3) :: k3
  integer(kind=i5) :: k5
  integer(kind=i8) :: k8
  integer(kind=i10):: k10
  integer(kind=i15):: k15

  print *, precision(x), range(x)
  print *, precision(y), range(y)
  print *, precision(z), range(z)
  print *, huge(k3)
  print *, huge(k5)
  print *, huge(k8)
  print *, huge(k10)
  print *, huge(k15)

end program real_kinds
```
- Basically selected_int_kind(5) == selected_int_kind(8)
