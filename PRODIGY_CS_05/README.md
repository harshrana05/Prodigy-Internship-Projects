# Packet Sniffer with Npcap

This Python application provides a simple packet sniffer interface using the `tkinter` library for GUI, `scapy` for packet capturing, and `Npcap` for network sniffing capabilities.

## Features
- Start and stop packet sniffing with the click of a button.
- Real-time display of captured packets in a scrollable text area.
- Clear instructions for usage.

## Requirements
- Python 3.x
- `tkinter` library (usually comes pre-installed with Python)
- `scapy` library (for packet manipulation and analysis)
- `Npcap` (for packet capturing on Windows platforms)

## Installation
1. Install Python from the official website: [Python Downloads](https://www.python.org/downloads/)
2. Install the `scapy` library: `pip install scapy`
3. Install `Npcap` from the official website: [Npcap Downloads](https://nmap.org/npcap/)
4. Clone or download the repository.
5. Run the Python script `Packet_sniffer.py`.

## Usage
1. Launch the application.
2. Click on the "Start Sniffing" button to begin packet capture.
3. Click on the "Stop Sniffing" button to stop packet capture.
4. View the captured packets in real-time in the scrollable text area.

## Code Overview

The `packet_sniffer.py` script includes:
- **Logging Configuration:** Logs are saved to `packet_sniffer.log` with a specified format.
- **Packet Handler:** Extracts and logs packet details (source IP, destination IP, protocol, payload) and updates the GUI.
- **Sniff Packets Function:** Starts the packet sniffing process using Scapy, checking for a stop event.
- **PacketSnifferApp Class:** Defines the Tkinter GUI, handles the start and stop actions, and updates the display.
- **Main Execution:** Initializes the Tkinter root window and the `PacketSnifferApp` instance, then starts the Tkinter main loop.

## Notes
- Ensure that you have the necessary permissions and privileges to capture network traffic.
- This application is primarily designed for educational and debugging purposes. Use responsibly and ethically.
