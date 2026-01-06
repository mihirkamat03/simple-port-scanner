import socket

def scan_port(ip, port):
    try:
        # Create socket with a short timeout (0.5s) to speed up scanning
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) 
        
        # Connect returns 0 on success (usually used with connect_ex for scanners)
        # But keeping your logic: if connect succeeds, code continues.
        sock.connect((ip, port))
        print(f"[+] Port {port} is Open on {ip}")
        sock.close()
    except:
        # If connection fails/times out, just ignore
        pass

# Main Logic
targets = input("[*] Enter targets (split by ,): ")
ports = int(input("[*] How many ports to scan?: "))

# .split(',') works for 1 or multiple targets automatically
for target in targets.split(','):
    target = target.strip() # Remove extra spaces
    print(f"\n--- Starting Scan for {target} ---")
    
    # Loop from 1 up to the number user entered (inclusive)
    for port in range(1, ports + 1):
        scan_port(target, port)