## Regarding Ceres 2.2 (early 2026) at Rocky8.10/RHEL8
- Requires eigen/3.3
  - 5.0 is not compatible
- glog: v0.5.0 is confirmed to work (not v0.7.1)
  - gflags: v2.3 is confirmed to work
- May need gcc > v10.x
- In CMake setup:
  - For the location of glog, up to cmake folder: `GLOG_DIR=/opt/glog/0.5.0/lib64/share/cmake/glog`
  - With shared build or not. Static/shared libs are not built simultaneosly. Build 2x to have both of them  
