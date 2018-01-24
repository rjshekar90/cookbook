

#!/usr/bin/env python

__author__ = 'Raj'

#python remote machine get_remote_machine_ip_addr

import socket

def get_remote_machine_info(remote_host):

    try:
        print(f'ip address is: {socket.gethostbyname(remote_host)}')
    except socket.error as err_msg:
        print(f'remote host {remote_host} responded with {err_msg}')

if __name__ == '__main__':
    get_remote_machine_info('www.google.cfl')




