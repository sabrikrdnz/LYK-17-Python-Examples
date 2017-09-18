import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 1500

server.bind((host,port))
server.listen()

print("[SERVER] Bağlantı Bekleniyor..")
client, addr = server.accept()

print("[SERVER] Biri bağlandı: %s" % str(addr))
client.send("Sunucuma Hosgeldin".encode('utf-8'))

gelenMesaj = client.recv(1024)

print("[SERVER] İstemciden gelen mesaj: " + gelenMesaj.decode('utf-8'))

while True:
    gidecekMesaj = input("Göndermek istediğiniz mesaj: ")

    client.send(gidecekMesaj.encode('utf-8'))

    gelenMesaj = client.recv(1024)
    gelenMesaj = gelenMesaj.decode("utf-8")
    print("[SERVER] İstemciden gelen mesaj: " + gelenMesaj)

    if gelenMesaj == "exit":
        break

client.close()

10.47.166.190