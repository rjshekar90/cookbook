
#!/usr/bin/env python
# Network pgm
#handle socket errors gracefully

__author__ = 'Raj'
__copyright__ = 'No One'

import sys
import socket
import argparse


def main():
    #arg parsing
    parser = argparse.ArgumentParser(description='Socket error handler')
    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)

    given_args = parser.parse_args()

    host = given_args.host
    port = given_args.port
    filename = given_args.file

    # create socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err_msg:
        print(f'Socket error is {err_msg}')

    # connect to given host/port
    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print(f'Address related error connectin to server {e}')
        sys.exit(1)
    except socket.error as e:
        print(f'Connection error {e}')
        sys.exit(1)

    #sending data
    try:
        msg = "GET %s HTTP/1.0\r\n\r\n" % filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print(f'Error sending data {e}')
        sys.exit(1)

    # wait to receiove data from remote host
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print(f'error receiving data {e}')
            sys.exit(1)
        if not (len(buf)):
            break
        sys.stdout.write(buf.decode('utf-8'))

if __name__ == '__main__':
    main()






