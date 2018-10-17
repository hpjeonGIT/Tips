#!/usr/bin/python

import sys
import os
word = sys.argv
#
# Check command
if (len(word) == 1):
    print " file name is required as an argument"
    sys.exit()
#
# Check the availability of the input file
fname=  word[1]
fcheck = os.path.isfile(fname)
if not (fcheck):
    print fname, " does not exist in the current directory"
    sys.exit()
fname_pre = os.path.splitext(fname)[0]
fname_ext = os.path.splitext(fname)[1]
outfname = 'ccx_model.inp'
print fname, " will be converted into ", outfname
#
# Open input/output files
inp = open(fname,'r')
out = open(outfname,'w')
xyz = open('tmp_xyz.xyz', 'w')
print >> out, "**" 
print >> out, "** ccx input file from conversion of ansys input"
print >> out, "**"
#
# pre-setup
tag_nlgeom = False
n_size = 12*20
n_big = 1000000
n_mptemp = 0
n_mpdata = 0
mptemp = [[ 0.0 for i in range (40)] for j in range (n_size)]
mpdata =[[ 0.0 for i in range (40)] for j in range (n_size)]
mp_owner = [0 for j in range (n_size)]
name_mpdata = ['name' for j in range(n_size)]
n_bf = 0
n_dof = 0
tref = 0.0
bf_data = [0.0 for i in range(n_big)]
bf_id = [0 for i in range (n_big)]
dof_data = [[0 for j in range (2) ] for i in range (n_big)]
el_type = []
line = inp.readline()
while (line):
    line = line.replace(',',' ')
    word = line.split()
    if (len(word) > 0):
        cmmnd = word[0]
        cmmnd = cmmnd.lower()
        #
        if (cmmnd == 'et'):
            el_type.append(int(word[2]))
        # nonlinear geometry check
        if (cmmnd == 'nlgeom'):
            opt = int(word[1]); 
            if (opt == 1):
                tag_nlgeom = True
        # nodal data conversion
        if (cmmnd == 'nblock'):
            nnode = int(word[3]);
            line = inp.readline()
            print >> out, "*NODE, NSET=Nall"
            for i in range (nnode):
                line = inp.readline()
                line = line.replace(',', ' ')
                word = line.split()
                if (len(word) == 6):
                    x = float(word[3]);  y = float(word[4]);z = float(word[5]);
                elif (len(word)== 5):
                    print i+1, "node is missing z pos"
                    x =  float(word[3]); y = float(word[4]); z = 0.0
                elif (len(word)== 4):
                    print i+1, "node is missing y/z pos"
                    x =  float(word[3]); y = 0.0 ; z = 0.0
                print >> out,'%6d, %14.7e, %14.7e, %14.7e' % (i+1, x, y, z)
                print >> xyz, x, y, z
        if (cmmnd == 'eblock'):
            nelem = int(word[3])
            line = inp.readline()            
            ntype = 0
            comp = 0
            for i in range (nelem):
                line = inp.readline()
                line = line.replace(',', ' ')
                word = line.split()
                mat_id = int(word[0])
                if (mat_id != comp):
                    ntype = ntype + 1
                    print >> out, '*ELEMENT, TYPE=C3D8, ELSET=ELSET%d'%( ntype)
                    comp = mat_id                
                print >> out, '%6d,%6d,%6d,%6d,%6d,%6d,%6d,%6d,%6d' \
                    % (int(word[10]), int(word[11]), \
                 int(word[12]), int(word[13]), int(word[14]), int(word[15]), \
                 int(word[16]), int(word[17]), int(word[18]))
        if (cmmnd == 'mptemp'):
            nitem = int(word[2])           
            n_id = 0
            for n in range (len(word) - 4):
                mptemp[n_mptemp][n_id] = float(word[n + 4])
                n_id = n_id + 1
            nline = (nitem-1)/3
            for n in range (nline):
                line = inp.readline()
                line = line.replace(',', ' ')
                word = line.split()
                for i in range (len(word) - 4):
                    #print  word, len(word), n_mptemp, n_id, i+4
                    mptemp[n_mptemp][n_id] = float(word[i + 4])
                    n_id = n_id + 1
            n_mptemp = n_mptemp + 1
        if (cmmnd == 'mpdata'):
            nitem = int(word[2])    
            mp_owner[n_mpdata] = int(word[4])
            name_mpdata[n_mpdata] = word[3]
            n_id = 0
            for n in range (len(word) - 6):
                mpdata[n_mpdata][n_id] = float(word[n + 6])
                n_id = n_id + 1
            nline = (nitem-1)/3
            for n in range (nline):
                line = inp.readline()
                line = line.replace(',', ' ')
                word = line.split()
                for i in range (len(word) - 6):
                    mpdata[n_mpdata][n_id] = float(word[i + 6])
                    n_id = n_id + 1
            n_mpdata = n_mpdata + 1

        if (cmmnd == 'd'):
            node = int(word[1])
            if (word[2] == 'UY'):
                dof = 2
            elif (word[2] == 'UX'):
                dof = 1
            elif (word[2] == 'UZ'):
                dof = 3
            else:
                print "bc error"
                sys.exit()
            dof_data[n_dof][0] = node
            dof_data[n_dof][1] = dof
            n_dof = n_dof + 1
        if (cmmnd == 'bf'):
            node = int(word[1])
            bf_id[n_bf] = node
            bf_data[n_bf] = float(word[3])
            n_bf = n_bf + 1
        if (cmmnd == 'tref'):
            tref = float(word[1])
                
            
                    
    line = inp.readline()

print >> out, '*ELSET, ELSET=ELALL'
print >> out, 'ELSET1, ELSET2'
print >> out, '*BOUNDARY'
for m in range (n_dof):
    print >> out, '%6d, %1d' %(dof_data[m][0], dof_data[m][1])

#
# Material section"
for n in range (n_mpdata):
    if (mp_owner[n] == 1):
        id_1 = n
        break
print >> out, "** order of ", name_mpdata[id_1], name_mpdata[id_1+1], \
    name_mpdata[id_1+2], name_mpdata[id_1+3], name_mpdata[id_1+5], \
    name_mpdata[id_1+4], name_mpdata[id_1+6], name_mpdata[id_1+8]
print >> out, "** continued ",    name_mpdata[id_1+7], " temperature"
print >> out, '*MATERIAL, NAME=M1'
print >> out, '*ELASTIC, TYPE=ENGINEERING CONSTANTS'
for m in range (40):
    print >> out, '%14.7e,%14.7e,%14.7e,%14.7e,%14.7e,%14.7e,%14.7e,%14.7e' \
        %(mpdata[id_1  ][m],mpdata[id_1+1][m],mpdata[id_1+2][m],\
          mpdata[id_1+3][m],mpdata[id_1+5][m],mpdata[id_1+4][m],\
          mpdata[id_1+6][m],mpdata[id_1+8][m]) 
    print >> out, '%14.7e,%14.7e' %(mpdata[id_1+7][m], mptemp[0][m])
print >> out, '*EXPANSION, TYPE=ORTHO, ZERO=', tref
for m in range (40):
    print >> out, '%14.7e,%14.7e,%14.7e,%14.7e' \
        %(mpdata[id_1+9][m], mpdata[id_1+10][m], mpdata[id_1+11][m], \
              mptemp[id_1+9][m])
print >> out, '*DENSITY'
print >> out, '%14.7e,%14.7e' % (mpdata[id_1+12][0], mptemp[id_1+12][0])
print >> out, '*CONDUCTIVITY, TYPE=ISO'
for m in range (11):
    print >> out, '%14.7e,%14.7e' %(mpdata[id_1 + 13][m],mptemp[id_1+13][m])
print >> out, '*SPECIFIC HEAT'
for m in range (11):
    print >> out, '%14.7e,%14.7e' %(mpdata[id_1+14][m], mptemp[id_1+14][m])
print >> out, '*SOLID SECTION, ELSET=ELSET1, MATERIAL=M1'
#
# Second material"
for n in range (n_mpdata):
    if (mp_owner[n] == 6):
        id_1 = n
        break
print >> out, '*MATERIAL, NAME=M2'
print >> out, '*ELASTIC, TYPE=ENGINEERING CONSTANTS'
for m in range (40):
    print >> out, '%14.7e,%14.7e,%14.7e,%14.7e,%14.7e,%14.7e,%14.7e,%14.7e' \
        %(mpdata[id_1  ][m],mpdata[id_1+1][m],mpdata[id_1+2][m],\
          mpdata[id_1+3][m],mpdata[id_1+5][m],mpdata[id_1+4][m],\
          mpdata[id_1+6][m],mpdata[id_1+8][m]) 
    print >> out, '%14.7e,%14.7e' %(mpdata[id_1+7][m], mptemp[id_1][m])
print >> out, '*EXPANSION, TYPE=ORTHO, ZERO=', tref
for m in range (40):
    print >> out, '%14.7e,%14.7e,%14.7e,%14.7e' \
        %(mpdata[id_1+9][m],mpdata[id_1+10][m],mpdata[id_1+11][m],\
              mptemp[id_1+9][m])
print >> out, '*DENSITY'
print >> out, '%14.7e,%14.7e' % (mpdata[id_1+12][0], mptemp[id_1+12][0])
print >> out, '*CONDUCTIVITY, TYPE=ORTHO'
for m in range (11):
    print >> out, '%14.7e,%14.7e,%14.7e,%14.7e' %(mpdata[id_1 + 13][m],\
        mpdata[id_1 + 14][m],mpdata[id_1 + 15][m],mptemp[id_1+13][m])
print >> out, '*SPECIFIC HEAT'
for m in range (11):
    print >> out, '%14.7e,%14.7e' %(mpdata[id_1+16][m], mptemp[id_1+16][m])
print >> out, '*SOLID SECTION, ELSET=ELSET2, MATERIAL=M2'


print >> out, '*INITIAL CONDITIONS, TYPE=TEMPERATURE'
print >> out, 'Nall,', tref
print >> out, '*STEP, NLGEOM'
print >> out, '*STATIC, DIRECT'
print >> out, '0.1, 0.1'
print >> out, '*TEMPERATURE'
for m in range (n_bf):
    print >> out, '%6d, %14.7e' % (bf_id[m], bf_data[m])
print >> out, '*EL PRINT, ELSET=ELALL, TOTALS=ONLY'
print >> out, 'ELSE, ELKE, EVOL'
print >> out, '*EL FILE'
print >> out, 'S, E'
print >> out, '*NODE FILE'
print >> out, 'U, NT'
print >> out, '*END STEP'
inp.close()
out.close()
xyz.close()
