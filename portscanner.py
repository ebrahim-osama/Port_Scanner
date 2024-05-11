import socket
import sys
import threading
from concurrent.futures import ThreadPoolExecutor

def scan(name, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((name, port))
        #sock.send(b'200 OK\r\n')
        #banner = str(sock.recv(256), 'ascii')
        service = socket.getservbyport(port)
        print("[+] {}/{} is open".format(port, service))
        print("[+] Protocol: TCP")
        # print("[+] Banner: ")
        # print(banner)
    except socket.error as e:
        if 'timed out' in str(e):
            error = 'filtered'
        else:
            error = "closed"
            print("[-] {}/tcp is {}".format(port, error))
    finally:
        sock.close()
        

def main():
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <host> <start_port> <end_port>")
        sys.exit(1)

    tgt_host = sys.argv[1]
    start_port = int(sys.argv[2])
    end_port = int(sys.argv[3])

    socket.setdefaulttimeout(1)
    
  
    max_threads = 50
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan, tgt_host, port)

if __name__ == "__main__":
    main()
