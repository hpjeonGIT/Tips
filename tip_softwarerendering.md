# When HW graphics or OpenGL support is not available or crashes

# matlab
- matlab -softwareopengl

# ansys workbench
- runwb2 -oglmesa
## Enabling mesa for mechanical only in WB
- export LD_LIBRARY_PATH+=/share/ansys_inc/v192/Framework/bin/Linux64/Mesa
- runwb2

# Paraview
- paraview --mesa-llvm

# Abaqus
- abaqus cae -mesa

# tecplot
- tec360 -mesa

# comsol
- comsol -3drend sw 
- comsol -3drend ogl # for opengl
- comsol -3drend dx9 # for directX in windows

# For any java 3d application using Canvas3d library
- export LIBGL_ALWAYS_SOFTWARE=1
- Tempest worked using this method
