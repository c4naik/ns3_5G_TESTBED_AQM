# Set the data files
flow_ids_file = 'flow_ids.dat'
throughputs_file = 'throughputs.dat'

# Set the number of flows
num_flows = system('wc -l < ' . flow_ids_file)

# Set the plot title, x and y labels
set title 'Throughput per Flow'
set xlabel 'Flow ID'
set ylabel 'Throughput (Kbps)'

# Set the key out of the plot area
set key outside

# Set the grid
set grid

# Plot the data
plot for [i=1:num_flows] flow_ids_file using (i-1):(column(i)) with linespoints
