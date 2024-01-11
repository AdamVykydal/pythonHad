# pylint: disable=broad-except
import socket
import time
import pickle


class Client:
    def __init__(self, serverIp, serverPort):
        self.serverIp = serverIp
        self.serverPort = serverPort
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.snakePartsToSend = []

    def connectToServer(self):
        while True:
            if (self.clientSocket.connect_ex((self.serverIp, self.serverPort))) == 0:
                break
            print(
                f"waiting for server on adress:{self.serverIp}:{self.serverPort}")
            time.sleep(2)

    def sendData(self):
        try:
            self.clientSocket.send(pickle.dumps(self.snakePartsToSend))
        except socket.error as e:
            print(f"Chyba při odesílání dat: {e}")

    def reciveData(self):
        try:
            data = self.clientSocket.recv(1024)
            data = pickle.loads(data)
            print(f"Received data: {data}")
            return data

        except pickle.PickleError as e:
            print(e)
            self.clientSocket.close()

    def prepareDataForSend(self, snakeParts):
        self.snakePartsToSend = []
        for snakePart in snakeParts:
            print(snakePart.coords.x, snakePart.coords.y)
            self.snakePartsToSend.append(
                (snakePart.coords.x, snakePart.coords.y))
