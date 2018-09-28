host = "192.168.43.201"
port = 8080
serverSocket=socket.socket()
serverSocket.bind((host,port))
serverSocket.listen(5)
client,addr=serverSocket.accept()

def recieve():
	data = client.recv(100)
	return data
data = recieve()
print(data)
