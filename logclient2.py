import socket
import sys

HOST = "localhost"
PORT = 50000
DATAFILE = "data.txt"

fin = open(DATAFILE,"rt")



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
  client.connect((HOST, PORT))
except:
  print("cannot connect")
  sys.exit()

msg = fin.read()
client.sendall(msg.encode("UTF-8"))
client.close()