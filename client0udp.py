import socket

HOST = "localhost"
#HOST = "127.0.0.1"
PORT = 50000
BUFSIZE = 4096

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Hi!",(HOST,PORT))

data = client.recv(BUFSIZE)
print(data.decode("UTF-8"))
client.close()
