import tkinter as tk
from tkinter import scrolledtext
from scapy.all import AsyncSniffer
from tkinter import ttk

sniffer = None  # Global variable to hold the sniffer instance

def start_sniffing():
    global sniffer
    
    def packet_callback(packet):
        text_area.insert(tk.END, f"{packet.summary()}\n")
    
    if sniffer is None:
        sniffer = AsyncSniffer(prn=packet_callback)
        sniffer.start()
        text_area.insert(tk.END, "Started sniffing...\n")
    else:
        text_area.insert(tk.END, "Sniffer is already running.\n")

def stop_sniffing():
    global sniffer
    
    if sniffer is not None:
        sniffer.stop()
        sniffer = None
        text_area.insert(tk.END, "Stopped sniffing.\n")
    else:
        text_area.insert(tk.END, "Sniffer is not running.\n")

# Create the main window
root = tk.Tk()
root.title("Packet Sniffer with Npcap")

# Set window size and position
window_width = 900
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Set custom style for the application
style = ttk.Style()
style.configure("TLabel", font=("Helvetica", 14))
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TFrame", background="#f0f0f0")
style.configure("TScrolledText", font=("Helvetica", 12))

# Create and place widgets
frame = ttk.Frame(root, padding=20, relief="raised", borderwidth=2)
frame.pack(fill=tk.BOTH, expand=True)

header_label = ttk.Label(frame, text="Packet Sniffer", font=("Helvetica", 24, "bold"))
header_label.pack(pady=10)

button_frame = ttk.Frame(frame)
button_frame.pack(pady=10)

start_button = ttk.Button(button_frame, text="Start Sniffing", command=start_sniffing)
start_button.pack(side=tk.LEFT, padx=10)

stop_button = ttk.Button(button_frame, text="Stop Sniffing", command=stop_sniffing)
stop_button.pack(side=tk.LEFT, padx=10)

text_area = scrolledtext.ScrolledText(frame, width=100, height=30, font=("Helvetica", 12))
text_area.pack(pady=10, fill=tk.BOTH, expand=True)

# Instructions label
instructions_label = ttk.Label(frame, text="Click 'Start Sniffing' to begin packet capture. Click 'Stop Sniffing' to stop.")
instructions_label.pack(pady=5)

# Run the application
root.mainloop()
