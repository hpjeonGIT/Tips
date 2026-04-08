## NVTX code
- cuda 12.8.1:
  - g++ -O3 ex_nvtx.cpp -L /opt/cuda/12.8.1/targets/x86_64-linux/lib -lnvToolsExt -ldl
  - nsys profile --trace=nvtx ./a.out
  - nsys-ui report.nsys-rep
- cuda 13.2:
  - g++ -O3 ex_nvtx.cpp -L /opt/cuda/13.2/targets/x86_64-linux/lib -lnvtx3interop -ldl
  - nsys profile --trace=nvtx ./a.out
  - nsys-ui report.nsys-rep

## nsys-ui or other GUI tool
- At RHEL/ROCKY, xcb-util-cursor is required
  - If sudo dnf install xcb-util-cursor doesn't work, find packages from https://pkgs.org/
