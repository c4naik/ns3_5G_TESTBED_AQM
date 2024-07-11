#!/bin/bash

# Set the name of your data file
DATA_FILE="NrDlRxRlcStats.txt"

# Set the names of the output graphs
THROUGHPUT_GRAPH="throughput.png"
DELAY_GRAPH="delay.png"

# Create the Gnuplot script for throughput vs time
cat << EOF > throughput.plt
set title "Throughput vs Time"
set xlabel "Time (s)"
set ylabel "Throughput (bps)"
set grid
set style data linespoints
plot for [i=3:4] '$DATA_FILE' using (column(1)):(column(i)*8/column(5)) title columnheader(i)
EOF

# Create the Gnuplot script for delay vs time
cat << EOF > delay.plt
set title "Delay vs Time"
set xlabel "Time (s)"
set ylabel "Delay (s)"
set grid
set style data linespoints
plot for [i=5:5] '$DATA_FILE' using (column(1)):(column(i)) title columnheader(i)
EOF

# Generate the throughput vs time graph
gnuplot -persist throughput.plt

# Generate the delay vs time graph
gnuplot -persist delay.plt

# Clean up the Gnuplot scripts
rm throughput.plt delay.plt
