# Set output to 'output.png'
set output 'output.png'
set terminal png

# Set labels
set xlabel 'Simulation Time (seconds)'
set ylabel 'Delay (milliseconds)'
set title 'Delay vs. Simulation Time'

# Set x-axis range
set xrange [0:5]

# Set grid
set grid

# Load data from CSV file, skipping the first row (header)
# Assuming the first column contains simulation times and the second column contains delays
plot 'data.csv' using 1:2 with linespoints pointtype 7 pointsize 0.5 lt rgb 'blue' notitle

