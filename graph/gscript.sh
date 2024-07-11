#!/bin/bash

# Process data file and calculate throughput
awk 'NR>1 {throughput = ($5 * 8) / (1000000*$6); print $1, throughput}' NrDlRxRlcStats.txt > processed_data.txt

# Gnuplot script to plot the data
gnuplot << EOF
set xlabel "Time (s)"
set ylabel "Throughput (Mbps)"
set title "Throughput vs. Time"
set terminal png size 800,600
set output 'throughput_vs_time.png'
plot 'processed_data.txt' with points title 'Throughput'
EOF

