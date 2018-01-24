
#!/usr/bin/env python

#python network cookbook code1

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    print(f'host name is: {host_name}')
    print(f'ip addr is: {ip_address}')

if __name__ == '__main__':
    print_machine_info()
