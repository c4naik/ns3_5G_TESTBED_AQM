import sys
import os
import subprocess

def Process(input_file):
    print("HELLO")
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

