# installing nvidia driver
- Disable nouveau
  - Google for detail. Needs blacklist
- If kernel is updated, kernel-devel kernel-headers must be updated as well
- sh NVIDIA-***.run --no-rdm
  - Without --no-rdm, OS may refuse to install. Discuss with Security folks for the detail
 - export TMPDIR=/somewhare/more_than_4GBs
 - sh ./cuda**.run
  - Cuda installation may unpack more than 4GB files
