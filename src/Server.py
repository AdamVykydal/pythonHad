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
        self.serverGameLogick = None
        self.fruitCoords = [(0, 0)]
        self.playersReady = [0, 0]
        self.playing = 0
        self.threadIdForNextCandidate = 0
        self.allThreadsIds = []
        self.playersNames = ["", ""]
        self.gameOptions = [100, 0, 0]

        print(f"Server is listening on {self.serverIp}:{self.serverPort}")

    def handleClient(self, clientIp):
        with self.lock:
            if self.connectedClients >= self.maxClients:
                print(f"{clientIp} max clients reached; disconnected")
                return False

            print(f"{clientIp} connected")
            self.connectedClients += 1
            return True

    def receiveGameData(self, clientSocket, clientIp, threadId):
        self.serverGameLogick = ServerGameLogick(self.clientsSnakesCoords, self.serverScore, self.gameOptions)
        try:
            while self.playing:
                data = clientSocket.recv(1024)
                if not data:
                    break
                self.clientsSnakesCoords[threadId] = pickle.loads(data)
                
                print( f"Received data: {clientIp}, {self.clientsSnakesCoords[threadId]}")
                
                gameIsFinished, collistionsInfo, playTime, self.fruitCoords = self.serverGameLogick.process(threadId)
                
                if gameIsFinished:
                    self.clientsSnakesCoords = [[(0, 0)], [(0, 0)]]
                    self.fruitCoords = [(0, 0)]
                    self.playing = False
                
                self.sendGameData(clientSocket, threadId, collistionsInfo, playTime)

        except Exception as e:
            print(e)
            self.diconectClient(threadId, clientSocket)
            
    def sendGameData(self, clientSocket, threadId, collistionsInfo, playTime):

        try:
            if threadId == 0:
                clientSocket.send(pickle.dumps([int(self.playing)] + [collistionsInfo] + [playTime] + [self.serverScore.score] + [self.clientsSnakesCoords[1]] + [self.fruitCoords]))
            else:
                clientSocket.send(pickle.dumps([int(self.playing)] + [collistionsInfo] + [playTime] + [list(reversed(self.serverScore.score))] + [self.clientsSnakesCoords[0]] + [self.fruitCoords]))

        except Exception as e:
            print(e)
            self.diconectClient(threadId, clientSocket)
        
    def start(self):
        try:
            while True:
                clientSocket, clientIp = self.serverSocket.accept()
                print(f"{clientIp} is trying to connect")

                if not self.handleClient(clientIp):
                    continue
                
                threadIdGuess = 0
                while True:
                    print(self.allThreadsIds)
                    print(threadIdGuess)
                    if threadIdGuess not in self.allThreadsIds:
                        self.allThreadsIds.append(threadIdGuess)
                        threadId = threadIdGuess
                        break
                    threadIdGuess =+ 1
                
                clientHandler = threading.Thread(target=self.gameMenuConnections, args=(clientSocket, clientIp, threadId))
                clientHandler.start()
                
        except KeyboardInterrupt:
            print("Server stopped.")

    def gameMenuConnections(self, clientSocket, clientIp, threadId):
        while True:
            try:
                data = clientSocket.recv(1024)
                data = pickle.loads(data)
                
                print (data)
                self.playersReady[threadId] = data[0]
                self.playersNames[threadId] = data[1]
                gameOptionsChahnges = data[2]

                self.gameOptions[0] += gameOptionsChahnges[0]
                self.gameOptions[1] += gameOptionsChahnges[1]
                self.gameOptions[2] += gameOptionsChahnges[2]
                
                if self.playersReady[threadId] != 0 and self.playersReady[threadId] != 1:
                    self.playersReady[threadId] = 0
                
                print(clientIp, ":", self.playersReady[threadId],",", self.playersNames[threadId])
                
                clientSocket.send(pickle.dumps([threadId ,self.playersReady, self.playersNames, self.gameOptions]))
                
                if self.playersReady == [1, 1]:
                    self.playing = True
                    self.receiveGameData(clientSocket, clientIp, threadId)
                    self.playersReady = [0, 0]
            
            except Exception as e:
                print(e)
                self.diconectClient(threadId, clientSocket)
                
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
    
    def diconectClient(self, threadId, clientSocket):
        self.playersNames[threadId] = ""
        self.playersReady[threadId] = 0
        self.allThreadsIds.remove(threadId)
        clientSocket.close()
        self.clientsSnakesCoords = [[(0, 0)], [(0, 0)]]
        self.fruitCoords = [(0, 0)]
        self.serverScore.score = [0, 0]
        self.playing = False
        with self.lock:
            self.connectedClients -= 1
            return


server = Server()
server.start()
