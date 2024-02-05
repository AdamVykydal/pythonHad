import sys
import subprocess
import pygame
from game.Client import Client
from menu.GameStartMenu import GameStartMenu
from menu.MultiplayerConnectMenu import MutiplayerConnectMenu
from gameFunctions.ScreenSize import ScreenSize
from menu.GameRoomMenu import GameRoomMenu
from game.SingleplayerGame import SingleplayerGame
from game.MultiplayerGame import MultiplayerGame
from game.LocalMultiplayerGame import LocalMultiplayerGame
from menu.MultiplayerMenu import MutiplayerMenu
from menu.LocalGameRoomMenu import LocalGameRoomMenu
from menu.LocalMultiplayerGameResults import LocalMultiplayerGameResults
from menu.SingleplayerGameResults import SingleplayerGameResults
from menu.MultiplayerGameResults import MultiplayerGameResults



class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode()
        self.screenWidth, self.screenHeight = self.screen.get_size()
        self.screenSize = ScreenSize(self.screenWidth, self.screenHeight)
        self.singleplayerGame = None
        self.multiplayerGame = None
        self.localMultiplayerGame = None
        self.gameStartMenu = GameStartMenu(self.screen, self.screenSize)
        self.multiplayerConnectMenu = MutiplayerConnectMenu(self.screen, self.screenSize)
        self.gameRoomMenu = GameRoomMenu(self.screen, self.screenSize)
        self.multiplayerMenu = MutiplayerMenu(self.screen, self.screenSize)
        self.localGameRoomMenu = LocalGameRoomMenu(self.screen, self.screenSize)
        self.singleplayerGameResult = None
        self.multiplayerGameResults = None
        self.localMultiplayerGameResults = None
        self.client = None
        self.gameResults = None

    def run(self):

        pressedButton = self.gameStartMenu.goMenu()

        if pressedButton == "singleplayerButton":
            self.singleplayerGame = SingleplayerGame(self.screen, self.screenSize)
            points, playTime = self.singleplayerGame.singlplayerGameLoop()
            
            self.singleplayerGameResult = SingleplayerGameResults(self.screen, self.screenSize)
            self.singleplayerGameResult.goMenu(points, playTime)
            
            self.singleplayerGame = self.singleplayerGameResult = None
        
        elif pressedButton == "multiplayerButton":
            while True:
                pressedButton = self.multiplayerMenu.goMenu()
                
                if pressedButton == "startServerMenuButton":
                    subprocess.run(["start", "cmd", "/c", "python", "src\Server.py"], shell=True, check=False)
                    
                elif pressedButton == "connectToServerMenuButton":
                    while True:
                        pressedButton = self.multiplayerConnectMenu.goMenu()
                        
                        if pressedButton == "connectButton":
                            try:
                                serverConected = self.connectToGameServer(
                                    self.multiplayerConnectMenu.ipBox.text)
                            except:
                                serverConected = False
                            
                            if serverConected:
                                
                                while True:
                                    pressedButton, playerId, playerNames = self.gameRoomMenu.goMenu(
                                        self.client, self.multiplayerConnectMenu.nameBox.text, self.multiplayerConnectMenu.ipBox.text)
                                    
                                    if pressedButton == "start":
                                        self.multiplayerGame = MultiplayerGame(self.screen, self.screenSize, playerId, playerNames)
                                        gameResults, snake1Statistics, snake2Statistics = self.multiplayerGame.multiplayergameLoop(self.client)
                                        
                                        self.multiplayerGameResults = MultiplayerGameResults(self.screen, self.screenSize)
                                        self.multiplayerGameResults.goMenu(gameResults, snake1Statistics, snake2Statistics)
                                        
                                        self.multiplayerGame = self.multiplayerGameResults = None
                                    
                                    elif pressedButton == "leaveLobbyButton":
                                        self.client.clientSocket.close()
                                        break

                        elif pressedButton == "backButton":
                            break
                
                elif pressedButton == "localGameMenuButton":
                    while True:
                        pressedButton = self.localGameRoomMenu.goMenu()
                        
                        if pressedButton == "playButton":
                            self.localMultiplayerGame = LocalMultiplayerGame(self.screen, self.screenSize, self.localGameRoomMenu.gameOptions)
                            gameResults, snake1Statistics, snake2Statistics = self.localMultiplayerGame.localMultiplayerGameLoop()
                            
                            self.localMultiplayerGameResults = LocalMultiplayerGameResults(self.screen, self.screenSize)
                            self.localMultiplayerGameResults.goMenu(gameResults, snake1Statistics, snake2Statistics)

                            self.localMultiplayerGame = self.localMultiplayerGameResults = None

                        elif pressedButton == "backButton":
                            break
                
                elif pressedButton == "backButton":
                    break
        
        elif pressedButton == "settingsButton":
            pass
        
        elif pressedButton == "endButton":
            pygame.quit()
            sys.exit()

    def connectToGameServer(self, serverIp):
        self.client = Client(serverIp, 11111)
        serverConected = self.client.connectToServer()
        return serverConected
