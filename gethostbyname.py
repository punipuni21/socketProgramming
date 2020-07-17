import socket

while True:
    try:
        hostname=input("ホスト名を入力(q出終了):")
        if(hostname=="q"):
            break
        print(socket.gethostbyname(hostname))
    except:
        print('変換できませんでした')