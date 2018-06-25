import os
import sys                                                          
import time
import numpy as np
import shutil


Xgrid = 4640
Ygrid = 4640
Zgrid = 4640
Ncpus = 32
HDF5Name = "zf100.h5"
DataName = "IntArray"
xdmfName = str(Ncpus)+'domain_Z_'+HDF5Name+'.xdmf'
dist_data = [0 for i in range(Ncpus)]
sum_data  = [0 for i in range(Ncpus)]
for i in range (Ncpus):
    dist_data[i] = Zgrid/Ncpus

if sum(dist_data) != Zgrid:
    dist_data[-1] -= (sum(dist_data) - Zgrid)

for i in range (1, Ncpus):
    sum_data[i] += sum_data[i-1] + dist_data[i-1]


print(dist_data)
print(sum_data)

def fillout(i):
      with open(xdmfName,'a') as f:
        f.write('<Grid Name="mesh" GridType="Uniform">\n')
	f.write('<Topology name="topo" TopologyType="3DCoRectMesh"\n')
        f.write('Dimensions = "%d %d %d" > </Topology>\n'
                % (dist_data[i], Ygrid, Xgrid))
	f.write('<Geometry name="geo" Type="ORIGIN_DXDYDZ">\n')
        f.write('<DataItem Format="XML" Dimensions="3">0 0 %d</DataItem>\n' 
                % (sum_data[i]))
        f.write('<DataItem Format="XML" Dimensions="3">1 1 1</DataItem>\n')
        f.write('</Geometry>\n')
        f.write('<Attribute Name="img" Center="Node">\n')
        f.write('<DataItem ItemType="HyperSlab" Dimensions="%d %d %d " Type="HyperSlab">\n'%(dist_data[i], Ygrid, Xgrid))
        f.write('<DataItem Dimensions="3 3" FORMAT="XML" PRECISION="4">\n')
        f.write('%d 0 0\n'%(sum_data[i]))
        f.write('1 1 1\n')
        f.write('%d %d %d\n'%(dist_data[i], Ygrid, Xgrid))
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
    for i in range (Ncpus):
        fillout(i)

    with open(xdmfName,'a') as f:
        f.write('</Grid>\n')
        f.write('</Domain>\n')
        f.write('</Xdmf>\n')
