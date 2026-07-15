# Dia Diagram tool

# At RockyOS8
- sudo yum install dia

# installing dia from source
- Source location: https://github.com/GNOME/dia
- Download master version
- At RockyOS:
  - sudo dnf install gtk2-devel libxml2-devel
  - ./configure --prefix=/opt/dia
  - make -j 20
  - make install

# Alternative of dia
- Dia is deprecated and not maintaned anymore
- May use draw.io: https://github.com/jgraph/drawio-desktop/releases
  - ApplImage can run as a standalone
  - Some glitches in GUI are found
