import csv
import math
import sys

if len(sys.argv) != 2:
    print("Error :Invalid number of arguements")
    exit()
tracefile =sys.argv[1]
filename =str(tracefile[0:-4]) + "-throughput.csv"
i=0
file1 = open(tracefile, 'r')
Lines1 = file1.readlines()
with open(filename,'w',newline='') as file:
    writer=csv.writer(file)
    datasize=0
    while i < len(Lines1):
        lines=Lines1[i].split()
        time = float(lines[0])
        tempvalue=math.trunc(time*10)/10 
        ceilvalue=tempvalue+0.1 
        while tempvalue < ceilvalue:
            datasize+=int(lines[1])
            i+=1
            if i >= len(Lines1):
                break
            lines= Lines1[i].split()
            time=float(lines[0])
            tempvalue=math.trunc(time*10)/10
        throughput=(datasize*8)/(1024*1024) # in mbps
        writer.writerow([ceilvalue-0.1,throughput])    
        datasize=0