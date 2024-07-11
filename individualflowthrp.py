import sys
import os
import subprocess

def Process(input_file):
    script = """
    #!/bin/bash

    
        output_file_new="output.txt"
        intermediate_file1="intermediate1.txt"
        intermediate_file2="intermediate2.txt"

        # Run the second AWK script
        awk ' {{
            time=sprintf("%.2f", $1);
            sum[time]+=$2;
        }}
        END {{
        
            for (j in sum) {{
                
                result = (sum[j] * 800) / (1024 * 1024);
                print j, result;
            }}
        }}' $input_file | sort -n > $intermediate_file1

        
    """.format(input_file)

    process = subprocess.Popen(script, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

Process("voiptrace2.tr")




new_file_name = "output"

gnu = open("gnufile", "w")
gnu.write("set terminal png\n")
gnu.write("set output \"Individual-flow-throughput"+".png\"\n set xlabel \"Time (Seconds)\" font \"Verdana,12\"\nset ylabel \"Throughput (Mbps)\" font \"Verdana,12\"\nset grid\nshow grid\nset key font \"Verdana,12\"\n")
gnu.write("plot \""+new_file_name+".txt"+"\" using 1:2 with lines title \"Flow "+"\"")
gnu.close()
os.system("gnuplot gnufile")
os.system("rm gnufile")

os.system("rm "+new_file_name+".txt")
