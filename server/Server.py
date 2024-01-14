# pylint: disable=broad-except
import socket
import threading
import pickle
from ServerGameLogick import ServerGameLogick
from ServerScore import ServerScore

class Server:
    def __init__(self):

        self.serverIp = self.getLocalIp()
        self.serverPort = 11111
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.serverIp, self.serverPort))
        self.serverSocket.listen(2)
        self.connectedClients = 0
        self.maxClients = 2
        self.lock = threading.Lock()
        self.serverScore = ServerScore()
        self.clientsSnakesCoords = [[(0, 0)], [(0, 0)]]
        self.serverGameLogick = ServerGameLogick(self.clientsSnakesCoords, self.serverScore)
        self.fruitCoords = [(0, 0)]

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

                self.clientsSnakesCoords[threadId] = pickle.loads(data)
                print(
                    f"Received data: {clientIp}, {self.clientsSnakesCoords[threadId]}")
                
                collistionsInfo, self.fruitCoords = self.serverGameLogick.process(threadId)
                
                self.sendData(clientSocket, threadId, collistionsInfo)

        except Exception as e:
            print(f"{clientIp}: {e}")
        finally:
            with self.lock:
                self.connectedClients -= 1
            clientSocket.close()

    def sendData(self, clientSocket, threadId, collistionsInfo):

        print([self.serverScore.score])
        try:
            if threadId == 0:
                clientSocket.send(pickle.dumps([collistionsInfo] + [self.serverScore.score] + [self.clientsSnakesCoords[1]] + [self.fruitCoords]))
            else:
                clientSocket.send(pickle.dumps([collistionsInfo] + [list(reversed(self.serverScore.score))] + [self.clientsSnakesCoords[0]] + [self.fruitCoords]))

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

    
    def getLocalIp(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            localIp = s.getsockname()[0]
            s.close()
            return localIp
        except socket.error as e:
            print("Nelze získat lokální IP adresu:", e)
            return None



server = Server()
server.start()
