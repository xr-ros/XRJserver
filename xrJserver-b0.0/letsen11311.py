import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.bind(('0.0.0.0', 11311))
# my_socket.settimeout(5)
my_socket.listen(3)
my_socket.settimeout(5)

while True:
    try:
        my_socket.accept()
        my_socket.recv(2000)
    except KeyboardInterrupt:
        break
    except socket.timeout:
        continue
