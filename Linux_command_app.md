# Ansys mechanical APDL
- copy ansys_inc/v192/ansys/data/models/CrankSlot_Flexible.inp into $WORK
- ansys192 -np 2  < CrankSlot_Flexible.inp > log.out
- file.rst, file.db will be produced
- launcher -> Select PrepPost from License -> Click run
- In the menu, General Postproc -> Results Viewer -> Select file.rst

# Fluent
- Unzip Modeling Flow Through porous.zip into  $WORK
- fluent 3d -g                                                       # run fluent 3d  without grahics
- file/read-case-data catalytic_converter.cas.gz # read input
- it 10                                                                  # do 10 iterations
- wcd "tmp.cas"                                               # save as jeonb.cas
- exit                                                                   # exit fluent terminal
- fluent 3d                                                          # open as GUI
- File-> Read -> Case & Datat -> select tmp.cas
- Click Postprocessing tab -> Graphics zone -> Contours -> Select velocity or Pressure

# HFSS
- copy ansoft/AnsysEM19/1/Linux64/Examples/HFSS/RF\ Microwave/coaxial_resonator.aedt to $WORK
-  ~~AnsTempDir=/lustre/tmp~~ # this is not honored
ansysedt -distributed -machinelist numcores=2 -auto -monitor -ng -batchsolve -batchoptions "HFSS/HPCLicenseType=pool tempdirectory=/work/jeonb/tmp" coaxial_resonator.aedt
- ansysedt  # GUI, open coaxial_resondator and Check Filed Overlays

# Abaqus
- abaqus fetch job=lap*.inp # extracting a sample input
- abaqus j=lap_joint inter cpus=2 (or 4, 8, 16, 32)
- Using htop, check if cpus are used as many as requested
- May take > 1 min with 2 cpus
- abaqus cae
- Open lap_joint.odb and visualize

# Comsol
- Copy comsol54/applications/Heat_Transfer_Module/Heat_Exchangers/heat_exchanger_iso.mph to $WORK
- comsol batch -nn 1 -np 1 -inputfile heat_exchanger_iso.mph -outputfile tmp.mph
-- Batch command using 1 cpu
- comsol
-- GUI. Open tmp.mph and check Results -> Temperature











