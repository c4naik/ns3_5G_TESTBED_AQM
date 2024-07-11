#!/bin/bash

input_file="voiptrace2.tr"
output_file_new="output.txt"
intermediate_file1="intermediate1.txt"
intermediate_file2="intermediate2.txt"

# Run the second AWK script
awk '{
    time=sprintf("%.2f", $1);
    sum[time]+=$2
}
END {
    for (j in sum) {
        result = (sum[j] * 800) / (1024 * 1024);
        print j, result
    }
}' $input_file | sort -n > $intermediate_file1

# Run the third AWK script
awk 'BEGIN {
    OFS = "\t"
    getline
    prev = sprintf("%.2f", $1)
    print
}
{
    for (i = prev + 0.01; sprintf("%.2f", i) < $1; i += 0.01)
        print sprintf("%.2f", i), "0.00"
    print
    prev = sprintf("%.2f", $1)
}' $intermediate_file1 | sort -n > $intermediate_file2

# Run the fourth AWK script
awk 'BEGIN {
    FS=OFS=" "
}
{
    rounded[$1] = sprintf("%.1f", $1)
    sum[rounded[$1]] += $2
    count[rounded[$1]]++
}
END {
    for (value in sum) {
        printf "%s %.3f\n", value, sum[value] / count[value]
    }
}' $intermediate_file2 | sort -n > $output_file_new

# Remove the intermediate files
#rm $intermediate_file1 $intermediate_file2

new_file_name="output"

# Write the gnuplot script to a file
echo "set terminal png" > gnufile
echo "set output \"Individual-flow-throughput.png\"" >> gnufile
echo "set xlabel \"Time (Seconds)\" font \"Verdana,12\"" >> gnufile
echo "set ylabel \"Throughput (Mbps)\" font \"Verdana,12\"" >> gnufile
echo "set grid" >> gnufile
echo "show grid" >> gnufile
echo "set key font \"Verdana,12\"" >> gnufile
echo "plot \"$new_file_name.txt\" using 1:2 with lines title \"Flow \"" >> gnufile

# Run the gnuplot script
gnuplot gnufile

# Remove the gnuplot script file
rm gnufile

# Remove the output file
#rm $new_file_name.txt

