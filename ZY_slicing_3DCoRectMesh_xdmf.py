import os
import sys                                                          
import time
import numpy as np
import shutil


Xgrid = 3096
Ygrid = 3096
Zgrid = 3096
Zcpu = 12
Ycpu = 8
Ncpus = Zcpu*Ycpu
HDF5Name = "zf150.h5"
DataName = "IntArray"
xdmfName = str(Ncpus)+'domain_ZY_'+HDF5Name+'.xdmf'
zdata = [0 for i in range(Zcpu)]
zsum  = [0 for i in range(Zcpu)]
ydata = [0 for i in range(Ycpu)]
ysum  = [0 for i in range(Ycpu)]

for i in range (Zcpu):
    zdata[i] = Zgrid/Zcpu

if sum(zdata) != Zgrid:
    zdata[-1] -= (sum(zdata) - Zgrid)

for i in range (1, Zcpu):
    zsum[i] += zsum[i-1] + zdata[i-1]

for i in range (Ycpu):
    ydata[i] = Ygrid/Ycpu

if sum(ydata) != Ygrid:
    ydata[-1] -= (sum(ydata) - Ygrid)

for i in range (1, Ycpu):
    ysum[i] += ysum[i-1] + ydata[i-1]


print(zdata); print(zsum)
print(ydata); print(ysum)

def fillout(i,j):
      with open(xdmfName,'a') as f:
        f.write('<Grid Name="mesh" GridType="Uniform">\n')
	f.write('<Topology name="topo" TopologyType="3DCoRectMesh"\n')
        f.write('Dimensions = "%d %d %d" > </Topology>\n'
                % (zdata[i], ydata[j], Xgrid))
	f.write('<Geometry name="geo" Type="ORIGIN_DXDYDZ">\n')
        f.write('<DataItem Format="XML" Dimensions="3">0 %d %d</DataItem>\n' 
                % (ydata[j],zdata[i]))
        f.write('<DataItem Format="XML" Dimensions="3">1 1 1</DataItem>\n')
        f.write('</Geometry>\n')
        f.write('<Attribute Name="img" Center="Node">\n')
        f.write('<DataItem ItemType="HyperSlab" Dimensions="%d %d %d " Type="HyperSlab">\n'%(zdata[i], ydata[j], Xgrid))
        f.write('<DataItem Dimensions="3 3" FORMAT="XML" PRECISION="4">\n')
        f.write('%d %d 0\n'%(zsum[i],ysum[j]))
        f.write('1 1 1\n')
        f.write('%d %d %d\n'%(zdata[i], ydata[j], Xgrid))
        f.write('</DataItem>\n')
        f.write('<DataItem Format="HDF" DataType="Int" Precision="4"\n')
        f.write('Dimensions=" %d %d %d "> %s:%s</DataItem>\n'
                %(Zgrid, Ygrid, Xgrid, HDF5Name, DataName))
        f.write('</DataItem>\n')
	f.write('</Attribute>\n')
        f.write('</Grid>\n')


if __name__=="__main__":
    with open(xdmfName,'w') as f:
        f.write('<?xml version="1.0" ?>\n')
        f.write('<Xdmf Version="2.1" xmlns:xi="http://www.w3.org/2003/XInclude">\n')
        f.write('<Domain>\n')
        f.write('<Grid name="part1" CollectionType="None" GridType="Collection" Name="Collection">\n')
    #
    for i in range (Zcpu):
        for j in range(Ycpu):
            fillout(i,j)

    with open(xdmfName,'a') as f:
        f.write('</Grid>\n')
        f.write('</Domain>\n')
        f.write('</Xdmf>\n')
