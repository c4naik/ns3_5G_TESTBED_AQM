# Set output to 'output.png'
set output 'output.png'
set terminal png

# Set labels
set xlabel 'Simulation Time (seconds)'
set ylabel 'Delay (milliseconds)'
set title 'Delay vs. Simulation Time'


# Set grid
set grid
set xrange [0:5]
set yrange [0:100]

# Load data from CSV file, skipping the first row (header)
# Assuming the first column contains simulation times and the second column contains delays
plot 'data2.csv' using 1:2 with lines

