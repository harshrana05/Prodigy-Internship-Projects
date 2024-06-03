from scapy.all import sniff, Raw
from scapy.layers.inet import IP, TCP, UDP
import logging
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread, Event

# Configure logging
logging.basicConfig(
    filename='packet_sniffer.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
)

# Initialize the stop event
stop_sniffing_event = Event()

def packet_handler(packet):
    if IP in packet:
        ip_layer = packet[IP]
        source_ip = ip_layer.src
        dest_ip = ip_layer.dst
        protocol = "Other"
        
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        
        payload = packet[Raw].load if Raw in packet else "None"
        
        log_message = f"Source IP: {source_ip}\nDestination IP: {dest_ip}\nProtocol: {protocol}\nPayload: {payload}\n{'-' * 30}"
        logging.info(log_message)
        
        if app:
            app.update_display(log_message)

def sniff_packets(app_instance):
    global app
    app = app_instance
    stop_sniffing_event.clear()
    sniff(prn=packet_handler, store=False, stop_filter=lambda x: stop_sniffing_event.is_set())

class PacketSnifferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Packet Sniffer")
        
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, width=80, height=20)
        self.text_area.pack()
        
        self.start_button = tk.Button(self.root, text="Start Sniffing", command=self.start_sniffing)
        self.start_button.pack()
        
        self.stop_button = tk.Button(self.root, text="Stop Sniffing", command=self.stop_sniffing, state=tk.DISABLED)
        self.stop_button.pack()
        
        self.sniff_thread = None
    
    def update_display(self, message):
        self.text_area.insert(tk.END, message + '\n')
        self.text_area.yview(tk.END)
    
    def start_sniffing(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.sniff_thread = Thread(target=sniff_packets, args=(self,))
        self.sniff_thread.start()
    
    def stop_sniffing(self):
        stop_sniffing_event.set()
        self.root.after(100, self.check_sniff_thread)

    def check_sniff_thread(self):
        if self.sniff_thread.is_alive():
            self.root.after(100, self.check_sniff_thread)
        else:
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)

app = None

if __name__ == "__main__":
    root = tk.Tk()
    app_instance = PacketSnifferApp(root)
    root.mainloop()
