import socket


def find_service_by_port():
    protocol_name = 'tcp'
    for port in [80, 25]:
        print(f"{port} ----- > service name {socket.getservbyport(port, protocol_name)}")


if __name__ == '__main__':
    find_service_by_port()
