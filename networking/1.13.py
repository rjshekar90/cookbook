__author__ = 'Raj'
__copyright__ = 'None'

# !/usr/bin/env python
# Simple client/server module

import argparse
import socket
import sys

(host, data_payload, backlog) = ('localhost', 2048, 5)


def echo_server(enter_port):
    """A simple echo server"""
    # create a TCP socket

    return enter_port


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A simple return port service')
    parser.add_argument("--port", action='store', dest='port', required=True)

    args = parser.parse_args()
    port = args.port
    print(echo_server(port))
