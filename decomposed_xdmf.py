#!/usr/bin/python
import os
import sys
import xml.etree.ElementTree as ET
from xml.dom import minidom

def main():
    fname_tail = '.h5'
    global Npt, scalars, Ncpus, DIM, fname_hdf5
    DIM = '3'
    scalars = ['energy', 'damage']
    Npt = 1000
    Ncpus = 6
    i_init = 1000
    i_final = 5000
    i_inc = 1000

    for n in range(i_init, i_final+1, i_inc):
        fname_hdf5 = str('%7.7d'%n) + 'step' + fname_tail
        fname_out = str(Ncpus) + 'cpus' + str('%7.7d'%n) + '.xmf'
        print "file name of output is ", fname_out
        xdmf_write(fname_out)

def prettify(elem):
    """Return a Pretty-printed XML string for the Element
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def xdmf_write(fname_out):
    Nmany = Ncpus
    Nmany10 = 10*Nmany
    out = open(fname_out,'w')
    dataitm = [' ' for i in range(Nmany10)]
    grid = [' ' for i in range(Nmany)]
    topo = grid
    geom = grid
    xdmf = ET.Element('Xdmf',Version='2.86')
    comment = ET.Comment('xdmf for HDF5 metadata')
    xdmf.append(comment)
    domain= ET.SubElement(xdmf,'Domain')
    grid_all = ET.SubElement(domain,'Grid',name='part1', CollectionType='none',\
                             GridType='Collection',Name='Collection')
    i_part = Npt / Ncpus
    n = 0
    for i in range(Ncpus):
        i_init = i_part * i
        i_final = i_part * (i+1)
        if (i==(Ncpus-1)):
            i_final = Npt
        i_count = i_final - i_init
        dname = 'domain'+str(i)
        grid[i] = ET.SubElement(grid_all,'Grid', name=dname)
        topo[i] = ET.SubElement(grid[i],'Topology',Type='Polyvertex',\
                                NodesPerElement='1',\
                                NumberOfElements=str(i_count))
        geom[i] = ET.SubElement(grid[i],'Geometry', Type='XYZ')
        dataitm[n] = ET.SubElement(geom[i],'DataItem',ItemType='HyperSlab',\
                                   Dimension=str(i_count) + ' ' + DIM,\
                                   Type = 'HyperSlab')
        n = n + 1
        dataitm[n] = ET.SubElement(dataitm[n-1], 'DataItem',Dimensions='3 2',\
                                   Format='XML', Precision='8')
        dataitm[n].text = '\n              ' + str(i_init) + \
                          ' 0 \n              1 1 \n              '+\
                          str(i_count) + ' ' + DIM + '\n              '
        n = n + 1
        dataitm[n] = ET.SubElement(dataitm[n-2],'DataItem', Datatype='Float',\
                                   Dimensions=str(Npt)+' '+DIM, Format = 'HDF')
        dataitm[n].text = fname_hdf5 + ':' + 'XYZ'
        for target in scalars:
            add_attribute(i_init, i_count, target, grid[i], dataitm, n)
    print >> out, prettify(xdmf)
    out.close()

def add_attribute(i_init, i_count, target, grid, dataitm, n):
    att = ET.SubElement(grid,'Attribute', Center='Node', Name=target,\
                        Type = 'Scalar')
    n = n + 1
    dataitm[n] = ET.SubElement(att,'DataItem',ItemType='HyperSlab',\
                               Dimensions=str(i_count), Type = 'HyperSlab')
    n = n + 1
    dataitm[n] = ET.SubElement(dataitm[n-1], 'DataItem', Dimensions='1 3', \
                               Format = 'XML', Precision='8')
    dataitm[n].text = '\n                ' + str(i_init) + ' 1 ' + \
                      str(i_count) + '\n                '
    n = n + 1
    dataitm[n] = ET.SubElement(dataitm[n-2],'DataItem',DataType='Float',\
                               Dimensions=str(Npt), Format = 'HDF', \
                               Precision = '8')
    dataitm[n].text = fname_hdf5 + ':' + target

if __name__ == '__main__':
    main()
