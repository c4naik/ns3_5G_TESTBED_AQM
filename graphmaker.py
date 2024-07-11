import matplotlib.pyplot as plt
import csv

# Initialize lists to store the data from the CSV
simulation_times = []
delays = []

# Open the CSV file and read the data, skipping the first row (header)
with open('data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip the header row
    for row in csvreader:
        simulation_times.append(float(row[0]))  # Assuming the first column contains float values
        delays.append(float(row[1]))  # Assuming the second column contains float values

# Plotting the data with markers for each data point
plt.plot(simulation_times, delays, marker='o', linestyle='-', color='b', markerfacecolor='yellow', markersize=3)
plt.plot(simulation_times, delays)
plt.xlabel('Simulation Time (seconds)')
plt.ylabel('Delay (milliseconds)')  # Updated label to indicate milliseconds
plt.title('Delay vs. Simulation Time')
plt.xlim(0, 5)  # Set x-axis range from 0 to 5 seconds as requested
plt.grid(True)  # Adds a grid for better readability
plt.show()
