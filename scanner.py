import socket

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) 
        sock.connect((ip, port))
        print(f"[+] Port {port} is Open on {ip}")
        sock.close()
    except:
        # If connection fails/times out, just ignore
        pass

targets = input("[*] Enter targets (split by ,): ")
ports = int(input("[*] How many ports to scan?: "))

for target in targets.split(','):
    target = target.strip()
    print(f"\n--- Starting Scan for {target} ---")
    
    for port in range(1, ports + 1):
        scan_port(target, port)