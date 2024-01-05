import socket
import threading

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
        
        print(f"Server is listening on {self.serverIp}:{self.serverPort}")
    
    def handleClient(self, clientSocket, clientIp):
        with self.lock:
            if self.connectedClients >= self.maxClients:
                print(f"{clientIp} max clients reached; disconnected")
                return False
            
            print(f"{clientIp} connected")
            self.connectedClients += 1
            return True
    
    def receiveData(self, clientSocket, clientIp):
        try:
            while True:
                data = clientSocket.recv(1024)
                if not data:
                    break 
                print(f"Received data: {clientIp}, {data.decode('utf-8')}")
                
                self.sendData(clientSocket)
        
        except Exception as e:
            print(f"{clientIp}: {e}")
        finally:
            with self.lock:
                self.connectedClients -= 1
            clientSocket.close()
    
    def sendData(self, clientSocket):
        try: 
            messageToSend = "Ahoj, jsem Server!"
            clientSocket.send(messageToSend.encode("utf-8"))
            
        except Exception as e:
            print(f"Error sending data: {e}")
            clientSocket.close()
    
    def start(self):
        try:
            while True:
                clientSocket, clientIp = self.serverSocket.accept()
                print(f"{clientIp} is trying to connect")

                if not self.handleClient(clientSocket, clientIp):
                    continue 

                clientHandler = threading.Thread(target=self.receiveData, args=(clientSocket, clientIp))
                clientHandler.start()
        
        except KeyboardInterrupt:
            print("Server stopped.")

server = Server("localhost", 11111, 2)
server.start()