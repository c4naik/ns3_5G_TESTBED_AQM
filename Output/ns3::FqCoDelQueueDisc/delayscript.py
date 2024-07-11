import csv
import sys
if len(sys.argv) != 3:
    print("Error :Invalid number of arguements")
    exit()
tracefile1=sys.argv[1]
tracefile2=sys.argv[2]
temp =tracefile1[0:-4]
csvfile= temp + "-delay.csv"
file1 = open(tracefile1, 'r')
Lines1 = file1.readlines()
i=0
file2 = open(tracefile2, 'r')
Lines2 = file2.readlines()
j=0
with open(csvfile,'w',newline='') as file:
    writer=csv.writer(file)
    while i < len(Lines1) and j < len(Lines2):
        line1=Lines1[i].split()
        line2=Lines2[j].split()
        if(int(line1[1]) == int(line2[1])):
            delay=str(1000*(float(line2[0])- float(line1[0])))
            writer.writerow([line1[0],delay])
            i=i+1
            j=j+1
        elif(int(line1[1]) < int(line2[1])):
            i=i+1
        else:
            j=j+1
    while i < len(Lines1):
        i=i+1