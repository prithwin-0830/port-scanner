import socket

target = input("Enter target IP or hostname: ")

print(f"\nScanning {target}...\n")

common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3389]

for port in common_ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: OPEN")

        sock.close()

    except KeyboardInterrupt:
        print("\nScan stopped by user.")
        break

    except socket.gaierror:
        print("Hostname could not be resolved.")
        break

    except socket.error:
        print("Could not connect to server.")
        break
