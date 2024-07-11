import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Parse the XML data
tree = ET.parse('results.xml')
root = tree.getroot()

# Extract the flow statistics
flow_stats = root.find('FlowStats')

# Check if the flow ID is not None
if flow_id is not None:
    # Extract the flow ID and packet count
    flow_id = flow_stats.get('flowId')
    packet_count = flow_stats.get('rxPackets')

    # Extract the delay histogram
    delay_histogram = flow_stats.find('delayHistogram')

    # Check if the delay histogram is not None
    if delay_histogram is not None:
        # Extract the delay values and counts
        delays = []
        counts = []
        for bin in delay_histogram:
            delay = bin.get('min')
            count = bin.get('count')
            delays.append(float(delay))
            counts.append(int(count))

        # Plot the delay histogram
        plt.hist(delays, bins=len(counts), weights=counts, alpha=0.5)
        plt.xlabel('Delay (ns)')
        plt.ylabel('Count')
        plt.title('Delay Histogram for Flow ' + flow_id)
        plt.show()
    else:
        print("No delay histogram found for flow")
else:
    print("No flow ID found")
