import sys
import os
import subprocess

def Process(input_file):
    script = f"""
    #!/bin/bash

    # Define the input file
    input_file="{input_file}"
    
    
        output_file="output.txt"
        intermediate_file1="intermediate1.txt"
        intermediate_file2="intermediate2.txt"

        # Run the second AWK script
        awk ' {{
            time=sprintf("%.2f", $1);
            sum[time]+=$5
        }}
        END {{
            for (j in sum) {{
                result = (sum[j] * 800) / (1024 * 1024);
                print j, result
            }}
        }}' $input_file | sort -n > $intermediate_file1

        # Run the third AWK script
        awk 'BEGIN {{
            OFS = "\t"
            getline
            prev = sprintf("%.2f", $1)
            print
        }}
        {{
            for (i = prev + 0.01; sprintf("%.2f", i) < $1; i += 0.01)
                print sprintf("%.2f", i), "0.00"
            print
            prev = sprintf("%.2f", $1)
        }}' $intermediate_file1 | sort -n > $intermediate_file2

        # Run the fourth AWK script
        awk 'BEGIN {{
            FS=OFS=" "
        }}
        {{
            rounded[$1] = sprintf("%.1f", $1)
            sum[rounded[$1]] += $2
            count[rounded[$1]]++
        }}
        END {{
            for (value in sum) {{
                printf "%s %.3f\\n", value, sum[value] / count[value]
            }}
        }}' $intermediate_file2 | sort -n > $output_file

        # Remove the intermediate files
        rm $intermediate_file1 $intermediate_file2 
    """

    process = subprocess.Popen(script, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

Process("NrDlRxRlcStats.txt")  #Input file name



gnu = open("gnufile", "w")

gnu.write("set terminal png\n")
gnu.write("set output \"overall-throughput.png\"\n set xlabel \"Time (Seconds)\" font \"Verdana,12\"\nset ylabel \"Throughput (Mbps)\" font \"Verdana,12\"\nset grid\nshow grid\nset key font \"Verdana,12\"\n")

new_file_name = "output"

gnu.write("plot \""+new_file_name+".txt"+"\"using 1:2 with lines title \"Total Traffic "+"\"")
gnu.close()
os.system("gnuplot gnufile")
os.system("rm gnufile output.txt")
