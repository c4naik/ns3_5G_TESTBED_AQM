import csv
import sys
import os


#SCRIPT 1 
file1 = open('./voiptrace1.tr', 'r')
Lines1 = file1.readlines()
i=0
file2 = open('./voiptrace2.tr', 'r')
Lines2 = file2.readlines()
j=0
with open('datavoip.csv','w+',newline='') as file:
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


#SCRIPT 1 
file1 = open('./udptrace1.tr', 'r')
Lines1 = file1.readlines()
i=0
file2 = open('./udptrace2.tr', 'r')
Lines2 = file2.readlines()
j=0
with open('dataudp.csv','w+',newline='') as file:
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
        
        
#SCRIPT 1 
file1 = open('./videotrace1.tr', 'r')
Lines1 = file1.readlines()
i=0
file2 = open('./videotrace2.tr', 'r')
Lines2 = file2.readlines()
j=0
with open('datavideo.csv','w+',newline='') as file:
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
        
        
        
#SCRIPT 1 
file1 = open('./gamingtrace1.tr', 'r')
Lines1 = file1.readlines()
i=0
file2 = open('./gamingtrace2.tr', 'r')
Lines2 = file2.readlines()
j=0
with open('datagaming.csv','w+',newline='') as file:
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



gnu = open("gnufile", "w+")

gnu.write("set terminal png\n")
gnu.write("set output \"delayudp.png\"\n set xlabel \"Time (Seconds)\" font \"Verdana,12\"\nset ylabel \"Delay (ms)\" font \"Verdana,12\"\nset grid\nshow grid\nset key font \"Verdana,12\"\nset datafile separator ','\n")

new_file_name = "dataudp"

gnu.write("plot \""+new_file_name+".csv"+"\"using 1:2 with lines title \"Delay UDP"+"\"")
gnu.close()
os.system("gnuplot gnufile")
os.system("rm gnufile dataudp.csv")





gnu = open("gnufile", "w+")

gnu.write("set terminal png\n")
gnu.write("set output \"delayvoip.png\"\n set xlabel \"Time (Seconds)\" font \"Verdana,12\"\nset ylabel \"Delay (ms)\" font \"Verdana,12\"\nset grid\nshow grid\nset key font \"Verdana,12\"\nset datafile separator ','\n")

new_file_name = "datavoip"

gnu.write("plot \""+new_file_name+".csv"+"\"using 1:2 with lines title \"Delay VoIP"+"\"")
gnu.close()
os.system("gnuplot gnufile")
os.system("rm gnufile datavoip.csv")





gnu = open("gnufile", "w+")

gnu.write("set terminal png\n")
gnu.write("set output \"delayvideo.png\"\n set xlabel \"Time (Seconds)\" font \"Verdana,12\"\nset ylabel \"Delay (ms)\" font \"Verdana,12\"\nset grid\nshow grid\nset key font \"Verdana,12\"\nset datafile separator ','\n")

new_file_name = "datavideo"

gnu.write("plot \""+new_file_name+".csv"+"\"using 1:2 with lines title \"Delay Video"+"\"")
gnu.close()
os.system("gnuplot gnufile")
os.system("rm gnufile datavideo.csv")





gnu = open("gnufile", "w+")

gnu.write("set terminal png\n")
gnu.write("set output \"delaygaming.png\"\n set xlabel \"Time (Seconds)\" font \"Verdana,12\"\nset ylabel \"Delay (ms)\" font \"Verdana,12\"\nset grid\nshow grid\nset key font \"Verdana,12\"\nset datafile separator ','\n")

new_file_name = "datagaming"

gnu.write("plot \""+new_file_name+".csv"+"\"using 1:2 with lines title \"Delay Gaming"+"\"")
gnu.close()
os.system("gnuplot gnufile")
os.system("rm gnufile datagaming.csv")

