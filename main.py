import time
from network_scanner import scan_ports

if __name__ == '__main__':
    startTime = time.time()
    target = input('Enter the host to be scanned: ')
    scan_ports(target)
    print('Time taken:', time.time() - startTime)
