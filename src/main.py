import random
import time
import os

import shipGenerator

def cls():
    os.system("cls")

def returnEmptyMap(): ##I had to do this because python doesnt have a "new" keyword.
    return  [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]

class gameInstance:
    def __init__(self, mapSize, startingShips):
        self.playerMaps = [returnEmptyMap(), returnEmptyMap()]
        self.startingShips = startingShips

        self.deadShip = "9"

    def populateMap(self):
        for player in range(2):
            cls()
            print(f"PLAYER CHOSING: {player+1}")
            for ship in self.startingShips:
                print(f"CurrentShip: {ship}")
                response = shipGenerator.plotShip(ship, [int(input(f"x coord of {ship}: ")),int(input(f"y coord of {ship}: "))], str(input("vertical or horisontal [vert/hori]: ")), self.playerMaps[player])
                print(response[0])
                if len(response) > 1:
                    self.playerMaps[player] = response[1]
                else: print("Ship Not Plotted")
         
    def attackTile(self, pos, player):
        if player == 0: player = 1
        else: player = 0
        if self.playerMaps[player][pos[1]][pos[0]] != 0 and self.playerMaps[player][pos[1]][pos[0]] != self.deadShip:
            self.playerMaps[player][pos[1]][pos[0]] = self.deadShip
            return "Hit"
        return "Miss"
    
    def isAlive(self, player):
        for row in self.playerMaps[player]:
            for location in row:
                if location == self.deadShip or location == 0: continue
                else: return True
        return False

    def gameLoop(self):
        self.populateMap()
        player = random.randint(0,1)
        while self.isAlive(0) == True and self.isAlive(1) == True:
            print(self.isAlive(0))
            print(self.attackTile([int(input("x coord: ")), int(input("y coord: "))], player))
            if player == 0: player = 1
            else: player = 0
        print(f"Winner is: {player+1}")
        
        
        
if __name__ == "__main__":
    game = gameInstance(10, ["cruiser"])
    game.gameLoop()
