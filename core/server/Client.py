import socket
import time


class Client:
    def __init__(self):
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.clientSocket.connect(("localhost", 11111))

    def sendData(self):
        try: 
            messageToSend = "Ahoj, jsem klient!"
            self.clientSocket.sendto(messageToSend.encode("utf-8"))
        except:
            self.clientSocket.close()
    
    def reciveData(self):
        try:
            data = self.clientSocket.recv(1024)
              
            print(f"Received data: {data.decode('utf-8')}")
        
        except: 
            self.clientSocket.close()

client = Client()

while True:
    
    client.sendData()
    client.reciveData()
    #time.sleep(5)
    