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
        self.serverGameLogick = ServerGameLogick(self.clientsSnakesCoords, self.serverScore)
        try:
            while self.playing:
                data = clientSocket.recv(1024)
                if not data:
                    break
                self.clientsSnakesCoords[threadId] = pickle.loads(data)
                if self.clientsSnakesCoords[threadId] == 1:
                    self.clientsSnakesCoords[threadId] = [(20, 20)]
                
                print( f"Received data: {clientIp}, {self.clientsSnakesCoords[threadId]}")
                
                gameIsFinished, collistionsInfo, playTime, self.fruitCoords = self.serverGameLogick.process(threadId)
                
                if gameIsFinished:
                    self.playing = False
                
                self.sendGameData(clientSocket, threadId, collistionsInfo, playTime)

        except Exception as e:
            print(e)
            self.fixDisconectedThreadId(threadId)
            clientSocket.close()
            self.playing = False
            self.serverGameLogick.restartgame()
            with self.lock:
                self.connectedClients -= 1
            return
            
    def sendGameData(self, clientSocket, threadId, collistionsInfo, playTime):

        try:
            if threadId == 0:
                clientSocket.send(pickle.dumps([int(self.playing)] + [collistionsInfo] + [playTime] + [self.serverScore.score] + [self.clientsSnakesCoords[1]] + [self.fruitCoords]))
            else:
                clientSocket.send(pickle.dumps([int(self.playing)] + [collistionsInfo] + [playTime] + [list(reversed(self.serverScore.score))] + [self.clientsSnakesCoords[0]] + [self.fruitCoords]))

        except Exception as e:
            print(e)
            self.fixDisconectedThreadId(threadId)
            clientSocket.close()
            self.playing = False
            self.serverGameLogick.restartgame()
            with self.lock:
                self.connectedClients -= 1
            return
        
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
                print("thrredId=", threadId)
                data = clientSocket.recv(1024)
            
                self.playersReady[threadId] = pickle.loads(data)

                if self.playersReady[threadId] != 0 and self.playersReady[threadId] != 1:
                    self.playersReady[threadId] = 0
                
                print(clientIp, ":", self.playersReady[threadId])
                
                clientSocket.send(pickle.dumps(self.playersReady))
                if self.playersReady == [1, 1]:
                    self.playing = True
                    self.receiveGameData(clientSocket, clientIp, threadId)
                    self.playersReady = [0, 0]
            
            except Exception as e:
                print(e)
                self.fixDisconectedThreadId(threadId)
                clientSocket.close()
                with self.lock:
                    self.connectedClients -= 1
                return
                
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
    
    def fixDisconectedThreadId(self, threadId):
        self.allThreadsIds.remove(threadId)

server = Server()
server.start()
