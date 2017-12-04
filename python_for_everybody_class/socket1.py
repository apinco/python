import socket

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'
sock = None

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('data.pr4e.org',80))
sock.send(cmd.encode())

while True:
    data  = sock.recv(20)
    if (len(data) < 1): break
    print(data.decode(), end='')

sock.close()