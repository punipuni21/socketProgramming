import socket
import sys
import os
import time

HOST = "localhost"
PORT = 50000
DATAFILE = "data.txt"
SLEEPTIME = 10

if os.name != "posix":
  print("unix系os以外は動かない")
  sys.exit()

host = input("接続サーバ")

while True:
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    client.connect((HOST, PORT))
  except:
    print("接続できません")
    sys.exit()

  loadave = os.getloadavg()
  print(loadave)
  client.sendall(str(loadave).encode("utf-8"))
  client.close()
  time.sleep(SLEEPTIME)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  client.connect((HOST, PORT))
except:
  print("cannot connect")
  sys.exit()

msg = fin.read()
client.sendall(msg.encode("UTF-8"))
client.close()