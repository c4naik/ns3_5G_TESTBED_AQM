import re
import matplotlib.pyplot as plt

# Regular expression pattern for extracting time and throughput from the .tr file
pattern = r"(\d+\.\d+) .*? (\d+) bytes"

# Initialize lists to store time and throughput values
time_values = []
throughput_values = []

# Open the .tr file for reading
with open("my-ascii-trace.tr", "r") as f:
    # Loop through each line in the .tr file
    for line in f:
        # Search for a match using the regular expression pattern
        match = re.search(pattern, line)
        if match:
            # Extract the time and throughput values from the matched string
            time_value = float(match.group(1))
            throughput_value = int(match.group(2)) / 1000000000 # Convert bytes to KB

            # Add the time and throughput values to the lists
            time_values.append(time_value)
            throughput_values.append(throughput_value)

# Plot the throughput vs time graph
plt.plot(time_values, throughput_values)
plt.xlabel("Time (s)")
plt.ylabel("Throughput (KB/s)")
plt.title("Throughput vs Time")
plt.grid(True)
plt.show()
