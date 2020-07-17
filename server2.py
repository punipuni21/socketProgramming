import socket
import datetime

PORT = 50000
BUFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))#暗黙的にlocalhostを使用
server.listen()


while True:
  client, addr = server.accept()
  msg = str(datetime.datetime.now())
  client.sendall(msg.encode("UTF-8"))
  print(msg, "接続要求あり")
  print(client)

  data = client.recv(BUFSIZE)
  print(data.decode("UTF-8"))

  client.sendall(msg.encode("UTF-8"))
  client.close()
