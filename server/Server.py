# pylint: disable=broad-except
import socket
import threading
import pickle
# from DataTransferException import DataTransferException


class Server:
    def __init__(self, serverIp, serverPort, maxClients):

        self.serverIp = serverIp
        self.serverPort = serverPort
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((serverIp, serverPort))
        self.serverSocket.listen(maxClients)
        self.connectedClients = 0
        self.maxClients = maxClients
        self.lock = threading.Lock()
        self.clientsData = [(0, 0), [(0, 0)]]

        print(f"Server is listening on {self.serverIp}:{self.serverPort}")

    def handleClient(self, clientIp):
        with self.lock:
            if self.connectedClients >= self.maxClients:
                print(f"{clientIp} max clients reached; disconnected")
                return False

            print(f"{clientIp} connected")
            self.connectedClients += 1
            return True

    def receiveData(self, clientSocket, clientIp, threadId):
        try:
            while True:
                data = clientSocket.recv(4000)
                if not data:
                    break

                self.clientsData[threadId] = pickle.loads(data)
                print(
                    f"Received data: {clientIp}, {self.clientsData[threadId]}")
                print(self.clientsData[0])
                print(self.clientsData[1])
                self.sendData(clientSocket, threadId)

        except Exception as e:
            print(f"{clientIp}: {e}")
        finally:
            with self.lock:
                self.connectedClients -= 1
            clientSocket.close()

    def sendData(self, clientSocket, threadId):

        try:
            if threadId == 0:

                clientSocket.send(pickle.dumps(self.clientsData[1]))
            else:
                clientSocket.send(pickle.dumps(self.clientsData[0]))

        except Exception as e:
            print(f"Error sending data: {e}")
            clientSocket.close()

    def start(self):
        try:
            threadId = 0
            while True:
                clientSocket, clientIp = self.serverSocket.accept()
                print(f"{clientIp} is trying to connect")

                if not self.handleClient(clientIp):
                    continue

                clientHandler = threading.Thread(
                    target=self.receiveData, args=(clientSocket, clientIp, threadId))
                clientHandler.start()
                threadId += 1

        except KeyboardInterrupt:
            print("Server stopped.")


server = Server("localhost", 11111, 2)
server.start()
