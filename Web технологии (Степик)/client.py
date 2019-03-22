import socket
while True:
    req = "Hello tcp!"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 1234))
    s.send(req.encode())
    rsp = s.recv(1024)
    print(s)
    s.close()
