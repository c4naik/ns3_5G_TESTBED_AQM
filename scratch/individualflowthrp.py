import sys
import os
import subprocess

def Process(input_file):
    script = """
    #!/bin/bash

    # Run the first AWK script
    awk '{{
        output_file = $3 ".txt"
        print $0 > output_file
        }}' {0}   
     rm "rnti.txt"
     # Get a list of the unique values in the third field
    unique_values=$(awk '{{print $3}}' {0} | sort -u)
    unique_values=$(echo $unique_values | rev | cut -d' ' -f2- | rev)
    echo $unique_values > unique_values.txt
    # Loop over the unique values from the first script
    for i in $unique_values
    do
        # Define the output file from the first script and the input file for the second script
        output_file2="${{i}}.txt"
        output_file_new="output${{i}}.txt"
        intermediate_file1="intermediate${{i}}1.txt"
        intermediate_file2="intermediate${{i}}2.txt"

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
        }}' $output_file2 | sort -n > $intermediate_file1

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
        }}' $intermediate_file2 | sort -n > $output_file_new

        # Remove the intermediate files
        rm $intermediate_file1 $intermediate_file2 $output_file2
    done
    """.format(input_file)

    process = subprocess.Popen(script, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

Process("NrDlRxRlcStats.txt")


with open('unique_values.txt', 'r') as f:
    unique_values = f.read().split()

new_file_name = "output"
for j in range(len(unique_values)):
    gnu = open("gnufile"+str(j+1), "w")
    gnu.write("set terminal png\n")
    gnu.write("set output \"Individual-flow-throughput"+str(j+1)+".png\"\n set xlabel \"Time (Seconds)\" font \"Verdana,12\"\nset ylabel \"Throughput (Mbps)\" font \"Verdana,12\"\nset grid\nshow grid\nset key font \"Verdana,12\"\n")
    gnu.write("plot \""+new_file_name+str(j+1)+".txt"+"\" using 1:2 with lines title \"Flow "+str(j+1)+"\"")
    gnu.close()
    os.system("gnuplot gnufile"+str(j+1))
    os.system("rm gnufile"+str(j+1))

for k in range(len(unique_values)):
    os.system("rm "+new_file_name+str(k+1)+".txt")
os.system("rm unique_values.txt")
