Byoungseon Jeon, PhD
====================
- HPC/ML Consultant
- Application SW engineer

TECHNICAL SKILLS
----------------
* High performance computing using MPI, OpenMP, CUDA libraries, and HDF5
* Expertise of machine learning, FDM/FEM/FVM, reservoir simulation, peridynamics, molecular dynamics, Monte-Carlo, and density functional theory
* Software development using C/C++, Python, Fortran, R, MATLAB
* Distributed Machine Learning and High Performance Data-Analytics (HPDA) using Python, Horovod, R, Rmpi
* Training/consulting customers for technical topics
* English, Japanese, Korean fluency. Basic Spanish/Arabic

PROFESSIONAL EXPERIENCE
------------------------
* Computational Modeling Engineer, Aramco Americas, Boston MA (July 2019 – present)
  - Developed in-house simulator suites
    - Implemented pre-conditioner, linear solver, IO, and framework using C++, OpenMP, MPI, HYPRE, AmgX, x86 intrinsics, SWIG, Python C-API, cereal, and HDF5
    - CI/CD and test automation using Bash scripting, CMake, and Google test
    - Debugging MPI code using Linaro DDT/gdb and profiling the performance using Cray Perftools, Intel VTune, AMD µProfiler, Nvidia ncu/nsys, and Linaro MAP
    - Python and Bash scripting for the model/DSL conversion, unit-test, post-processing, and data analytics
    - Optimized and improved parallel computing algorithm for large-scale processing
    - Investigated Cray environment and optimized performance over cpu-binding and architecture, trouble-shooting MPI compatibility and MPMD hand-shaking
    - Converted CUDA code into ROCm/HIP for AMD GPUs
    - Visited Saudi R&D center to collaborate with developers
  - Managed HPC HW/SW environment for scientific computing
    - Trouble-shooted daily issues in SW development and HW maintenance, consulting developers
    - Installed/managed open-source SW like LLVM, PETSc, Scalapack, Trilinos, Deal.II, MOOSE, TexMaker, MVAPICH2, OSU benchmark, OpenPBS, Darshan, OpenMPI with UCX and gdrcopy, and commercial SW like Matlab, Mathematica, SLB Eclipse/IX/Visage, DDT, TotalView, providing module environment
    - Installed RHEL7/8, RockyOS8, Ubuntu20 on workstations, and managed Linux cluster using HP CMU and SLURM job scheduler
    - Installed/managed Ganglia/Nagios for Linux cluster monitoring such as ambient/CPU temperature, SLURM status, Infiniband connection, and workload
    - Provided/managed GRAV server for internal documentation of the best practice
    - Trained new hires/interns for Linux cluster environment and workflow
* Senior Computational Scientist, Corning Incorporated, Corning NY (May 2017 - July 2019)
  - Parallelized/optimized in-house/open-source/commercial applications over HPC clusters for machine learning and scientific computing
    - Accelerated DL/CNN image training of Keras/TensorFlow using distributed computing of Horovod, OpenMPI, and NCCL2 (30x speed-up using 32 GPUs)
    - Performed 1 trillion grid simulations of Cellular Automata using Co-Array Fortran with 6000 MPI ranks, and visualized 4 TB snapshots using distributed parallel VisIt, HDF5, and xdmf on Lustre
    - Accelerated ABAQUS scripting 10x through profiling and optimizing sketching/partitioning
    - Implemented OpenMP, MPI, and dense/sparse solver using DGESV/PARDISO for in-house developed scientific codes
  - Responded to customer requests such as modeling of scientific/engineering problems, automation of complex simulations, and Proof-of-Concepts to meet business requirements
    - Delivered ABAQUS Python scripts for CAD automation, parametric study, and crack growth simulations
    - Consulted ABAQUS modeling for beam structures, contact simulation, and spray modeling by SPH
    - Developed PoC of image analysis tools using OpenCV, NumPy, SciPy, tkinter, and mysql-connector for flaw detection, surface characterization, and spray measurement
    - Delivered the best practice of ANSYS, Fluent, ABAQUS, COMSOL, MATLAB, LS-DYNA, HFSS, Lumerical, Rsoft, ParaView, VisIt, OpenFoam/FireFoam, Python, R, and Keras/TensorFlow for HPC Linux environment    
  - Provided comprehensive user documentation, training, and daily support for HPC environment
    - Published documentation of HPC training and scientific SW on the internal GRAV server
    - Performed daily trouble-shooting like PBS job monitoring and license optimization
    - Installed/tested open-source software like UCX, CUDA-aware OpenMPI, KLayout, PyTorch, CNTK, TensorFlow, FireFoam, NWchem, SuiteSparse, ADIOS, IOR, namd, Lammps, Gromacs using configure/Make/Cmake with Intel/GCC/CUDA compilers, and provided module environment
    - Organized and delivered training/workshop for python data analytics, image classification, open source software installation, scripting for ABAQUS, profiling, debugging, and OpenMP/OpenACC
  - Delivered data analytics using state-of-art ML techniques
    - Performed image classification using VGG16, ResNet50, and MobileNet in Keras/Tensorflow for process control
    - Developed R/Python scripts for data engineering on OSIsoft PI data using AFSDK, OLEDB, ODBC, JDBC
    - Performed data analytics using random forest analysis, SVM, auto-correlation in Python/R
* HPC Performance Architect, Intel Corporation, Santa Clara CA (Nov. 2016 - Apr. 2017)
  - Evaluated HPC performance of scientific SW to build weak-scaling model
    - Delivered scientific code profiling and tracing with Intel VTune, ITAC, and MPI Pcontrol with mpiP/mpitrace/IMPI tools on Intel XEON PHI KNL
    - Performed vectorization and optimization through Intel Advisor and SDE
* Senior Research Scientist, Corning Incorporated, Corning NY (May 2014 - Nov. 2016)
  - Parallelized machine learning/scientific applications over HPC cluster and optimized commercial applications
    - Accelerated machine learning algorithm such as exhaustive search (800x speed-up using 1024 CPUs) and greedy search (96x speed-up using 128 CPUs) using R and Rmpi
    - Delivered 1 billion particle peridynamics simulations accelerating an in-house developed code with MPI, OpenMP, and HDF5 on 1,600 CPUs and Lustre
    - Delivered distributed parallel visualization using Paraview and VisIt with VTK/XDMF
    - Profiled and debugged scientific codes with Intel VTune/IDB, Allinea MAP/DDT, Rprof, and gprof/gdb
    - Delivered benchmark of Fluent/ABAQUS for large-scale simulations
    - Performed parallel command processor (PCP) for many serial jobs of parametric study
    - Explored new skills like OpenACC, GPGPU, Intel PHI KNC/KNL, and Lustre parallel file system
    - Optimized python scripts of ABAQUS CAE (4x speed-up in DOE) and debugged UMAT of LS-DYNA
    - Delivered modeling and simulations of glass impact, thermal cracking, drop tests, and dynamic damage evolution
  - Supported SW environment and daily trouble-shooting for HPC clusters
    - Installed and managed open source software like R, FFTW, Python, NumPy, GNUplot, paraview, OpenFOAM, LAMMPS, meep, and mpb using Intel MKL, open-mpi, Intel mpi, and mvapich
    - Provided user training of Linux operation, MATLAB, R, PBS scheduler, C programming, profiling, and debugging
    - Performed daily troubleshooting for scientific/engineering software performance, scripting, resource-monitoring, and conversion codes like from MATLAB to Python/C
    - Mentored junior researchers and trained new hires for scientific programming and parallel computing
* Product Analyst, CTG, Corning NY (Sept. 2013 - May 2014)
  - A contractor for Corning Inc: Scientific Computing in M&S
  - Scientific SW development
    - Delivered web-interface engineering applications for EASA platform
    - Developed a MATLAB GUI application with constrained optimization solver
  - High Performance Computing
    - Parallelized peridynamics code using OpenMP and MPI (108x speed-up using 128 CPUs)
    - Built Calculix from scratch and deployed for multiple-processors
  - Provided user training for MATLAB and Intel PHI
* Post-doctoral Researcher, Harvard University, Cambridge MA (June 2010 - Feb. 2013)
  - Supervisor: Shriram Ramanathan
  - Implemented parallel ReaxFF molecular dynamics using MPI and OpenMP
    - Performed simulations of oxidation kinetics of metallic surfaces like Al/Ni/Fe, V, Cu, and Zr (published in J. Phys. Chem. C, Surf. Sci., J. Chem. Phys., and Phys. Chem. Chem. Phys.)
    - Simulated aqueous corrosion of metallic surface using ReaxFF (published in Appl. Mat. Interfaces)
  - Performed DFT analysis of metal-insulator transition using abinit
    - Explored CUDA for many-body simulations
* Post-doctoral Researcher, University of California, Davis CA (March 2008 - May 2010)
  - Supervisor: Niels Grønbech-Jensen
  - Development of molecular dynamics code and parallel computing algorithm
    - Ion radiation molecular dynamics code using polling method for dynamic branching and enhancing statistics (published in Comp. Phys. Comm.)
    - Parallel ion cascade molecular dynamics using MPI and OpenMP for large scale (presented in Mat. Res. Soc.)
  - Performed First principles calculation of oxides using VASP (presented in ACTINIDES 2009)
  - Led workshop for the development of classical molecular dynamics and DFT programs
    - Managed OSX server with a dozen of iMac and Mac Pro clients
* Research Engineer, Agency for Defense Development, Daejon, South Korea (Feb. 1997 - July 2002)
  - Delivered modeling and simulations of dynamic structures using FDM/FEM
    - OTI HULL for hydrodynamic simulations of jet formation
    - DASSAULT ABAQUS for transmission of stress wave and large deformation by impact
    - MSC PATRAN for CAD, meshing, and post-processing
    - MSC DYTRAN for ballistic simulations
  - Developed simulation software using modern Fortran
    - Mesh free method for large deformation of hyperelasticity
    - Smooth particle hydrodynamics (SPH) for EOS and explosion simulations
  - Performed experiments for the measurement of dynamic material properties
    - Performed Hopkins bar test for high-strain rate deformation
    - Assisted plate impact tests and VISAR setup for EOS measurement
  - Participated in the ballistic tests for armor structures
    - Designed confinement system for ceramic armor structures
    - Performed scaled-down ballistic tests and maintained the facility
    - Assisted field tests and analyzed results

EDUCATION
---------
* Ph.D. in Applied Science, University of California, Davis, CA (GPA:3.88, March 2008)
  - Dissertation: Methods for molecular interactions and large-scale simulations
  - Advisor: Niels Grønbech-Jensen
  - Course-works: quantum chemistry, statistical thermodynamics, advanced numerical methods, mathematical methods for physics, parallel programming
  - Graduate research assistant at Los Alamos National Laboratory (2005 - 2007)
  - Teaching assistant for computer solution of physical problems, numerical solution of engineering and scientific problems (2002 – 2005)
* M.S. in Mechanical Engineering, Korea Advanced Institute of Science and Technology, Daejon, South Korea (Feb. 1997)
  - Thesis: Response to low-velocity impact and delamination buckling behavior of a smart structure embedded with optical fibers
  - Course-works: fracture mechanics, nonlinear solid mechanics, composite mechanics, finite element method
* B.S. in Machine Design and Production Engineering, Hanyang University, Seoul, South Korea (Feb 1995) 
  - Course-works: statics/dynamics, solid/fluid mechanics, thermodynamics, engineering mathematics, numerical method, CAD, system dynamics, mechanical behavior of materials, heat transfer, machine design

CERTIFICATES
------------
* Oracle University
  - Oracle Cloud Infrastructure Foundations Badge (2024)
  - Introduction to Oracle Cloud Essentials Badge (2024)
  - Oracle Cloud Infrastructure 2023 AI Foundations Associate (1Z0-1122-23) (2024)
* Nvidia Academy Certificate of Completion
  - Ansible Essentials for Network Engineers (2024)
  - Introduction to AI in the Data Center (2024)
  - InfiniBand Essentials (2023)
  - Introduction to Base Command Manager (2023)
* Google Cloud Completion Badge
  - Infrastructure and Application Modernization with Google Cloud (2024)
  - Introduction to Generative AI (2024)
  - Digital Transformation with Google Cloud (2024)
  - Google Cloud Fundamentals: Core Infrastructure (2023)
* Deep Learning Courses Certificate of Achievement
  - Data Science: Transformers for Natural Language Processing (2023)
* Udemy certificate of completion
  - Introduction to Software Development Life Cycle (SDLC) (2024)
  - Linux KVM for System Engineers (2024)
  - Beginners Course: Jq Command Tutorials to Parse JSON Data (2024)
  - Learn Perl 5 By Doing It (2024)
  - Complete DevOps Ansible Automation Training (2024)
  - C++ Data Structures & Algorithms + LEETCODE Exercises (2024)
  - Assembly Language Foundation Course for Ethical Hackers (2024)
  - Erlang: The Complete Beginner's Guide (2024)
  - Lua Scripting: Master complete Lua Programming from scratch (2024)
  - COBOL Complete Reference Course! (2024)
  - The Complete Course of TCL Programming 2024 (2024)
  - Anomaly Detection: Machine Learning, Deep Learning, AutoML (2024)
  - Function Acceleration on FPGA with Vitis – part 1: Fundamental (2023)
  - Machine Learning: Natural Language Processing in Python (V2) (2023)
  - Advanced C Programming Masterclass: Pointers & Memory in C (2023)
  - ANTLR Programming masterclass with Python (2023)
  - Master Generative AI (2023)
  - Linux Binary Analysis for Ethical Hackers and Pentesters (2023)
  - Exploit Development Tutorial for Hackers and Pentesters (2023)
  - The Complete Parallelism Course (2023)
  - x86/x64 Assembly Language for Cybersecurity Maniacs (2023)
  - High Performance Computing in Linux (2023)
  - How Computers Work (2023)
  - Programming with Julia (2023)
  - Complete Ruby Programmer – Master Ruby (2023)
  - The Complete Haskell Course: From Zero to Expert! (2023)
  - Kubernetes for the Absolute Beginners - Hands-on (2022)
  - Master Puppet for DevOps Success (2022)
  - OpenStack Essentials (2022)
  - API and Web Service Introduction (2022)
  - SSL/TLS Operations (2022)
  - CompTIA Network+ (N10-008) Video Training Series (2022)
  - Linux System Programming - A programmer's/Practical Approach (2022)
  - Linux Diagnostics and Troubleshooting (2022)
  - Master CMake for Cross-Platform C++ Project Building (2022)
  - Modern C++ Concurrency in Depth (C++17/20) (2022)
  - Complete Modern C++ (C++11/14/17) (2022)
  - Structural Design Patterns in Modern C++ (2022)
  - Creational Design Patterns in Modern C++ (2022)
  - Hands on Debugging in C and C++ (2022)
  - x86 64-bit Assembly Language: Step-by-Step Tutorial (2022)
  - Learn Linux User Space Debugging (2022)
  - Go: The Complete Developer's Guide (2022)
  - Java 17: Learn and dive deep into Java (2022)
  - The Nuts and Bolts of OAuth 2.0 (2022)
  - The Complete Regular Expressions Course with Exercises (2022)
  - Learn and Understand NodeJS (2022)
  - The Complete Quantum Computing Course (2022)
  - Arabic language | The comprehensive course (2021)
  - MongoDB - The Complete Developer's Guide (2021)
  - JavaScript – The complete Guide 2022 (2021)
  - x86 Assembly Language Programming from Ground Up (2021)
  - Learn C++ for Game Development (2021)
  - Learning CUDA10 Programming (2020)
  - Learn Linux Kernel Programming (2020)
  - CUDA Programming Masterclass with C++ (2020)
  - C++ Unit Testing: Google Test and Google Mock (2020)
  - SQL and PostgreSQL: The Complete Developer's Guide (2020)
  - Linux x86 Assembly Language Programming From Ground Up (2020)
* AWS Cloud Practitioner Essentials (2020)
* Exam Readiness: AWS Certified Solutions Architect – Associate (Digital) (2020)
* Certificate of completion by Workforce Development & Learning, Corning
  - Getting results through others (2018)
  - DOL 1: Stepping Into Leadership (2018)
* Course certificate for Data Science and Data Engineering by Datasciencedojo (2017)
* Certificate of training by ANSYS
  - Introduction to ANSYS DesignModeler & Meshing (2014)
  - Introduction to ANSYS Mechanical (2014)

PUBLICATIONS
------------
* Patent
1. J. George, **B. Jeon**, S. T. Nickerson, H.C. Sim, Structural characteristic prediction for a honeycomb body using image abstraction, World Intellectual Property Organization, W0 2022/0 35664 A1 (2022)
* Peer-reviewed Journal Papers
1. R. Stewart, **B. Jeon**, “Decoupling strength and grid resolution in peridynamic theory,” Journal of Peridynamics and Nonlocal Modeling,  pp.1-10 (2019)
2. **B. Jeon**, R. Stewart, I Ahmed, “Peridynamic simulations of brittle structures with thermal residual deformation: strengthening and structural reactivity of glasses under impact,” Proceedings of the Royal Society A 471, 20150231 (2015)
3. R. Copping, **B. Jeon**, C. D. Pemmaraju, S. Wang, S. J. Teat, M. Janousch, T. Tyliszczak, A. Canning, N. Grønbech-Jensen, D. Prendergast, D. K Shuh, “Toward equatorial planarity about uranyl: synthesis and structure of tridentate nitrogen-donor UO2 2+ Complexes,” Inorganic Chemistry 53, 2506-2515 (2014)
4. **B. Jeon**, Quentin Van Overmeere, A.C.T . van Duin, and S. Ramanathan, “Nanoscale oxidation and complex oxide growth on single crystal iron surfaces and external electric field effects,” Physical Chemistry Chemical Physics 15, 1821-1830 (2013)
5. **B. Jeon**, S. Sankaranarayanan, A.C.T. van Duin, and S. Ramanathan, “Reactive molecular dynamics study of chloride ion interaction with copper oxide surfaces in aqueous media,” ACS Applied Materials & Interfaces 4, 1225-1232 (2012)
6. **B. Jeon**, C. Ko, A.C.T . van Duin, and S. Ramanathan, “Chemical stability and surface stoichiometry of vanadium oxide phases studied by reactive molecular dynamics simulations,” Surface Science 606, 516-522 (2012)
7. **B. Jeon**, S. Sankaranarayanan, A.C.T. van Duin, and S. Ramanathan, “Influence of surface orientation and defects on early stage oxidation and ultrathin oxide growth on pure copper,” Philosophical Magazine 91, 4073-4088 (2011)
8. P. Tiwary, A. van de Walle, **B. Jeon**, and N. Grønbech-Jensen, “Interatomic potentials for mixed oxide and advanced nuclear fuels ,” Physical Review B 83, 094104 (2011)
9. **B. Jeon**, S. Sankaranarayanan, A.C.T. van Duin, and S. Ramanathan, “Atomistic insights into aqueous corrosion of copper,” Journal of Chemical Physics 134, 234706 (2011)
10. **B. Jeon**, S. Sankaranarayanan, and S. Ramanathan, “Atomistic modeling of ultra-thin surface oxide growth on a ternary alloy: oxidation of Al-Ni-Fe,” Journal of Physical Chemistry C 115, 6571-6580 (2011)
11. S. M. Valone, B . P. Uberuaga, X.-Y. Liu, **B. Jeon**, A. Chaudhry, and N. Grønbech-Jensen, “Cascade-driven mixing at metal oxide interfaces,” Nuclear Instruments and Methods in Physics Research B 268, 3114-3116 (2010)
12. **B. Jeon**, M. Asta, S. M. Valone, and N. Grønbech-Jensen, “Simulation of ion track ranges in uranium oxide,” Nuclear Instruments and Methods in Physics Research B 268, 2688-2693 (2010)
13. **B. Jeon** and N. Grønbech-Jensen, “Efficient Parallel Algorithm for Statistical Ion Track Simulations in Crystalline Materials,” Computer Physics Communications 180, 231-237 (2009)
14. **B. Jeon**, M. Foster, J. Colgan, G. Csanak, J. D. Kress, L. A. Collins, and N. Grønbech-Jensen, “Energy Relaxation Rates in Dense Hydrogen Plasmas,” Physical Review E 78, 036403 (2008)
15. **B. Jeon**, J. D. Kress, L. A. Collins, and N. Grønbech-Jensen, “Parallel TREE code for two-component ultracold plasma analysis,” Computer Physics Communications 178, 272-279 (2008)
16. **B. Jeon**, J. D. Kress, and N. Grønbech-Jensen, “Thiol density dependent classical potential for methyl-thiol on a Au(111) surface,” Physical Review B 76, 155120 (2007)
17. **B. Jeon**, J.J. Lee, J.K. Kim, J.S. Huh, “Low velocity impact and delamination buckling behavior of composite laminates with embedded optical fibers,” Smart Materials and Structures 8 (1), 41-48 (1999)

PRESENTATIONS
-------------
* Conference Talks
1. **B. Jeon**, “Deep learning for visual inspection of ceramic honeycomb structures,” 2018 Modeling Symposium, Corning, NY (2018)
2. **B. Jeon**, et al, “Profiling and Accelerating Scientific Codes,” 2018 Modeling Symposium, Corning, NY (2018)
3. **B. Jeon**, et al, “Peridynamic simulations of strengthened glasses,” 6th Modeling Symposium, Corning, NY (2016)
4. **B. Jeon**, et al, “Nonlinear material simulations using peridynamics,” 5th Modeling Symposium, Corning, NY (2014)
5. **B. Jeon**, A.C.T. van Duin, and S. Ramanathan, “Computational modeling of surface passive oxide growth and breakdown on metal nano-particles,” Materials Research Society Fall meeting, Boston, MA (2012)
6. **B. Jeon**, A.C.T. van Duin, and S. Ramanathan, “Atomistic simulations of aqueous corrosion of copper and copper oxide films,” Corrosion-Aqueous, Gordon Research Seminar, New London, NH (2012)
7. **B. Jeon**, S. Sankaranarayanan, A.C.T. van Duin, and S. Ramanathan, “Passivity breakdown and pitting nucleation of copper oxide films under aqueous conditions: Simulations by reactive molecular dynamics,” Materials Research Society Fall meeting, Boston, MA (2011)
8. **B. Jeon**, S. Sankaranarayanan, A.C.T. van Duin, and S. Ramanathan, “Early stages of aqueous corrosion of copper using reactive molecular dynamics,” Electrochemical Society Fall meeting, Boston, MA (2011)
9. S. Ramanathan and **B. Jeon**, “Atomistic Modeling of Nanoscale Corrosion Phenomena in Al alloys and the influence of Chlorine,” Discovery & Invention (D&I) Program Review, Arlington, VA (2011)
10. **B. Jeon**, S. Sankaranarayanan, and S. Ramanathan, “Molecular dynamics simulation of oxidation growth on metal alloy substrate: kinetics of early stage oxidation,” NACE CORROSION conference, Houston, TX (2011)
11. **B. Jeon**, A. Chaudhry, M. Asta, S. Valone, and N. Grønbech-Jensen, “Radiation Range and Damage Assessment in UO2 Simulated by Classical Molecular Dynamics,” Materials Research Society Spring meeting, San Francisco, CA (2010)
12. L. Collins, **B. Jeon**, J. Kress, and  N. Grønbech-Jensen, “Dynamics of ultracold neutral plasma,” American Physical Society March meeting, Denver, CO (2007)
13. **B. Jeon**, L. Collins, J. Kress, and  N. Grønbech-Jensen, “Relaxation of laser-induced two component plasma,” American Physical Society March meeting, Denver, CO (2007)
* Poster Presentations
1. **B. Jeon**, et al, “Honeycomb structure surface characterization using computer vision and deep learning,” 2018 Measurement & Control Conference, Corning, NY (2018)
2. **B. Jeon**, et al, “Fracture mechanics modeling capability,” Equipment and Process Engineering, Corning, NY (2014)
3. **B. Jeon**, A.C.T. van Duin, and S. Ramanathan, “Atomistic simulations of aqueous corrosion of copper and copper oxide films,” Corrosion-Aqueous, Gordon Research Conference, New London, NH (2012)
4. **B. Jeon**, “Electronic Structure Studies of Actinide Complexation by Maltol and Benzimidazyl type Ligands,” ACTINIDES 2009, San Francisco, CA (2009)
5. N. Grønbech-Jensen, M. D. Asta, N. Browning, C. Wolverton, A. van de Walle, V. Ozolins, **B. Jeon**, A. Chaudhry, A. Sankar, B. Hanken, J. Aguiar, G. Zhang, A. Thomposon, P. Tiwary, S. Barabash, F. Zhou, “Radiation Damage in Nuclear Fuel for Advanced Burner Reactors: Modeling and Experimental Validation,” Advanced Fuel Cycle Initiative (AFCI) Annual Review meeting, Idaho Falls, ID (2008)
6. **B. Jeon**, “Radiation Range Analysis of High Energy Ions,” Advanced Test Reactor summer school, Idaho Falls, ID (2008)

MANUSCRIPT REFEREEING
---------------------
- The Open Mechanical Engineering Journal (Bentham Open)
- Phys. Chem. Chem. Phys. (Royal Society of Chemistry)
- Computational Materials Science/Vacuum (Elsevier)
- Nanoscale (Royal Society of Chemistry)
- Journal of Physical Chemistry (American Chemical Society)
- Proceedings of ACTINIDES (Institute Of Physics)

HONORS AND AWARDS
-----------------
1. 2nd place in the internal competition for the course of datadojo class (2017)
2. Advanced Fuel Cycle Initiative  (AFCI) Annual Review Meeting Best Poster, Idaho Falls ID (2008) 
3. Core Researcher Award, Agency for Defense Development (2002) 
