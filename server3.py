import socket
import datetime
import threading

PORT = 50000
BUFSIZE = 4096

def client_handler(client, clientno, msg):
  """
  クライアントとの接続処理スレッド
  """
  data = client.recv(BUFSIZE)
  print("(",clientno,")", data.decode("UTF-8"))

  client.sendall(msg.encode("UTF-8"))
  client.close()



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))#暗黙的にlocalhostを使用
server.listen()

clientno = 0

while True:
  client, addr = server.accept()
  clientno += 1
  msg = str(datetime.datetime.now())
  print(msg, "接続要求あり(",clientno,")")
  print(client)

  p = threading.Thread(target=client_handler, args=(client, clientno, msg))
  p.start()

  