import socket
import threading
import sys

PORT = 50000
BUFSIZE = 4096

def server_handler(client):
  while True:
    try:
      data = client.recv(BUFSIZE)
      print(data.decode("UTF-8"))
    except:
      sys.exit()
  client.close()


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = input("接続先サーバ")

if host == "":
  host = "localhost"

p = threading.Thread(target=server_handler, args=(client,))

p.setDaemon(True)

while True:
  msg = input("")
  client.sendto(msg.encode("UTF-8"), (host, PORT))
  if msg == "q":
    break
  if not p.is_alive():
    p.start()
  
client.close()