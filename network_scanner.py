from socket import *

def scan_ports(target):
    t_IP = gethostbyname(target)
    print('Starting scan on host:', t_IP)
    
    open_ports = []
    for i in range(50, 500):
        s = socket(AF_INET, SOCK_STREAM)
        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            open_ports.append(i)
            print('Port %d: OPEN' % (i,))
        s.close()
    return open_ports
