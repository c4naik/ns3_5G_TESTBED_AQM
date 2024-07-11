import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Parse the XML file
tree = ET.parse('results.xml')
root = tree.getroot()

# Extract flow stats
flows = root.find('FlowStats')
flow_list = []
throughput_list = []

for flow in flows:
    flow_id = flow.get('flowId')
    tx_bytes_elem = flow.find('txBytes')
    rx_bytes_elem = flow.find('rxBytes')
    time_first_rx_elem = flow.find('timeFirstRxPacket')
    time_last_rx_elem = flow.find('timeLastRxPacket')

    if tx_bytes_elem is not None and rx_bytes_elem is not None and time_first_rx_elem is not None and time_last_rx_elem is not None:
        tx_bytes = int(tx_bytes_elem.text)
        rx_bytes = int(rx_bytes_elem.text)
        time_first_rx = float(time_first_rx_elem.text[1:-2])
        time_last_rx = float(time_last_rx_elem.text[1:-2])

        throughput = (rx_bytes * 8.0) / (time_last_rx - time_first_rx) / (1024*1024*1024)
        flow_list.append(flow_id)
        throughput_list.append(throughput)

# Plot the throughput
plt.bar(flow_list, throughput_list)
plt.xlabel('Flow ID')
plt.ylabel('Throughput (Kbps)')
plt.title('Throughput per Flow')
plt.show()
