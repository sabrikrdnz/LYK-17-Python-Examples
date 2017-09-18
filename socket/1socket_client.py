import socket 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("Host: ")
port = int(input("Port: "))

client.connect((host, port))

while True:
	gelenMesaj = client.recv(1024)

	print("[CLIENT] Sunucudan gelen mesaj: " + gelenMesaj.decode('utf-8'))
	mesaj = input("Gidecek Mesaj: ")

	client.send(mesaj.encode('utf-8'))

	if mesaj == "exit":
		break

client.close()
