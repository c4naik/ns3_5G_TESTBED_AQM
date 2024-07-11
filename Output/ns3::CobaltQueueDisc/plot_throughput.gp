# Set the output format to a PNG image
set terminal png

# Set the output file name
outputfilename = "./Images/Throughput/" . name . "-throughput.png"
set output outputfilename

# Set titles and labels
set title 'Throughput vs. Simulation Time'
set xlabel 'Simulation Time (seconds)'
set ylabel 'Throughput (Mbps)'

# Set x-axis range
set xrange [0:5]

# Enable grid
set grid

# Check if the file is using commas as separators and change the datafile separator accordingly
# This line is commented out by default. Uncomment it if your data uses commas.
set datafile separator ','

# Plot the data, explicitly skipping the header row using 'every' with '::1'
plot datafile using 1:2 with linespoints linestyle 1 linecolor 'blue' pointtype 7 pointsize 0.5 pointcolor 'yellow' title 'Throughput'
