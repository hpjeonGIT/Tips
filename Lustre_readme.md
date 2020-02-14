#Lustre best practice
- `lfs df` # shows the number of OST servers
- `lfs getstripe ./tmp` # shows the Lustre configuration of ./tmp folder
- `lfs setstripe -S 1M -c 1 ./tmp` # configures ./tmp as 1M chuck and 1 stripe
- `lfs setstripe -S 4M -c 4 ./tmp` # configures ./tmp as 4M chuck and 4 stripes
