import sys
import os
import subprocess
import pygame
from Client import Client
from GameStartMenu import GameStartMenu
from MultiplayerConnectMenu import MutiplayerConnectMenu
from ScreenSize import ScreenSize
from GameRoomMenu import GameRoomMenu
from SingleplayerGame import SingleplayerGame
from MultiplayerGame import MultiplayerGame
from LocalMultiplayerGame import LocalMultiplayerGame
from MultiplayerMenu import MutiplayerMenu



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
        self.client = None

    def run(self):

        pressedButton = self.gameStartMenu.goMenu()

        if pressedButton == "singleplayerButton":
            self.singleplayerGame = SingleplayerGame(self.screen, self.screenSize)
            self.singleplayerGame.singlplayerGameLoop()
        
        elif pressedButton == "multiplayerButton":
            while True:
                pressedButton = self.multiplayerMenu.goMenu()
                
                if pressedButton == "startServerMenuButton":
                    subprocess.run(["start", "cmd", "/c", "python", "src\\Server.py"], shell=True, check=False)
                    
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
                                    pressedButton = self.gameRoomMenu.goMenu(
                                        self.client, self.multiplayerConnectMenu.nameBox.text, self.multiplayerConnectMenu.ipBox.text)
                                    
                                    if pressedButton == "start":
                                        self.multiplayerGame = MultiplayerGame(self.screen, self.screenSize, self.gameRoomMenu.playerId)
                                        self.multiplayerGame.multiplayergameLoop(
                                            self.client)
                                    
                                    elif pressedButton == "leaveLobbyButton":
                                        #self.client.sendMenuData(0)
                                        self.client.clientSocket.close()
                                        break

                        elif pressedButton == "backButton":
                            break
                
                elif pressedButton == "localGameMenuButton":
                    self.localMultiplayerGame = LocalMultiplayerGame(self.screen, self.screenSize)
                    self.localMultiplayerGame.localMultiplayerGameLoop()
                
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
