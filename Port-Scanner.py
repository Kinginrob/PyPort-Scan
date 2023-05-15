import socket
import threading
from tkinter import *

# Create a new tkinter window
root = Tk()
root.title("Port Scanner")
root.geometry("500x400")

# Create text boxes
ip_entry = Entry(root, width=30)
ip_entry.grid(row=0, column=1, padx=20)

start_entry = Entry(root, width=30)
start_entry.grid(row=1, column=1)

end_entry = Entry(root, width=30)
end_entry.grid(row=2, column=1)

# Create text box labels
ip_label = Label(root, text="Target IP")
ip_label.grid(row=0, column=0)

start_label = Label(root, text="Start Port")
start_label.grid(row=1, column=0)

end_label = Label(root, text="End Port")
end_label.grid(row=2, column=0)

# Create result box
result_box = Text(root, height=10, width=50)
result_box.grid(row=4, column=0, columnspan=2)

# Function to scan ports
def port_scanner(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        connection = sock.connect((ip, port))
        result_box.insert(END, f'Port {port} is open\n')
        connection.close()
    except: 
        result_box.insert(END, f'Port {port} is closed or the host is down\n')

# Function to get the values from the text boxes and start the scan
def start_scan():
    target_ip = ip_entry.get()
    start = int(start_entry.get())
    end = int(end_entry.get())
    for port in range(start, end+1):
        thread = threading.Thread(target=port_scanner, args=(target_ip, port))
        thread.start()

# Create a button to start the scan
scan_button = Button(root, text="Start Scan", command=start_scan)
scan_button.grid(row=3, column=0, columnspan=2)

root.mainloop()
