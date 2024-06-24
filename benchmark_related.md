## disk speed
- dd if=/dev/zero of=/tmp/mytmp bs=1M count=1024 conv=fdatasync
- Can be used for mounted file server like gpfs or nfs
- For throughput tests, use ior
