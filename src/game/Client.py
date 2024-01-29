# pylint: disable=broad-except
import socket
import pickle

class Client:
    def __init__(self, serverIp, serverPort):
        self.serverIp = serverIp
        self.serverPort = serverPort
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.snakePartsToSend = []

    def connectToServer(self):
        try:
            if (self.clientSocket.connect_ex((self.serverIp, self.serverPort))) == 0:
                pass
            else:
                return False
            return True
        except:
            return False
       
    def sendSnakeData(self):
        print("snakeSending:", self.snakePartsToSend)
        try:
            self.clientSocket.send(pickle.dumps(self.snakePartsToSend))
        except socket.error as e:
            print(f"sending data error {e}")

    def sendMenuData(self, menuData):
        try:
            print("menuSending:", menuData)
            self.clientSocket.send(pickle.dumps(menuData))
        except socket.error as e:
            print(f"sending data error {e}")

    def reciveGameData(self):
        try:
            data = self.clientSocket.recv(1024)
            if not data:
                self.sendSnakeData()
                data = self.clientSocket.recv(1024)
            data = pickle.loads(data)
            print(f"Received data: {data}")
            return bool(data[0]), data[1], data[2], data[3], data[4], data[5]

        except pickle.PickleError as e:
            print(e)
            self.clientSocket.close()

    def reciveMenuData(self):
        try:
            data = self.clientSocket.recv(1024)
            data = pickle.loads(data)
            print(f"Received data: {data}")
            return data[0], data[1], data[2], data[3]

        except pickle.PickleError as e:
            print(e)
            self.clientSocket.close()
    
    def prepareDataForSend(self, snakeParts):
        self.snakePartsToSend = []
        for snakePart in snakeParts:
            self.snakePartsToSend.append(
                (snakePart.coords.x, snakePart.coords.y))
        
