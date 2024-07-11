# Set the output format to a PNG image
set terminal png

# Set the output file name
set output 'simulation_delay_plot.png'

# Set titles and labels
set title 'Delay vs. Simulation Time'
set xlabel 'Simulation Time (seconds)'
set ylabel 'Delay (milliseconds)'


# Enable grid
set grid

# Check if the file is using commas as separators and change the datafile separator accordingly
# This line is commented out by default. Uncomment it if your data uses commas.
set datafile separator ','

# Plot the data, explicitly skipping the header row using 'every' with '::1'
plot 'data2.csv' using 1:2 with lines title 'Delay'
