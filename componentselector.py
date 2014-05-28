#!/usr/bin/python
import re
from sys import argv

# Store input and output file names
script,ifile,ofile = argv

o = open(ofile,'w')

comps = {}
comps_index= []

with open(ifile) as f:
    i = 0
    cc = 0
    for line in f:
        if re.search(">", line):
            cc += 1
            if cc % 1000 == 0:
                print cc
            comps_index.append(i)
            foo = line.split(" ")[0].split("_seq")[0]
            bar = int(line.split(" ")[1].split("=")[1])
            if foo in comps.keys():
                if(bar > comps[foo].keys()[0]):
                    comps[foo] = {bar:i}
            else:
                comps[foo] = {bar:i}
                    
        i+=1

print "Done parsing " + str(cc) + " components."

print_index=[]
for k in comps:
    print_index.append(comps[k].values()[0])

print "Completed indexing step 1."

disp_index=[]

for j in xrange(0,len(comps_index)):
    if j % 1000 == 0:
        print j    
    if comps_index[j] in print_index:
        if j==(len(comps_index)-1):
            disp_index.extend(range(comps_index[j],i))
        else:
            disp_index.extend(range(comps_index[j],comps_index[j+1]))

print "Completed indexing step 2."

with open(ifile) as f:
    i = 0
    cc = 0
    for line in f:
        if cc % 1000 == 0:
            print cc
        if i in disp_index:
            if re.search(">",line):
                o.write(line.split(" ")[0].split("_seq")[0])
                o.write("\n")
            else:
                o.write(line)
            cc+=1
        i+=1

o.close()
