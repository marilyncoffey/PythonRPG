#Simple 2D Map example
#Feel free to expand and use
from MapFile import makeMap


class TheMap:

    def __init__(self, mapList, fillChar = "·"):
        self.map = mapList
        self.fillChar = fillChar
        
    def setFillChar(self, posX, posY, fillChar):
        self.map[posX - 1][posY - 1] = fillChar
        
    def getFillChar(self, posX, posY):
        fillChar = self.map[posX - 1][posY - 1]
        return fillChar

        
    def display(self):
        #Each row
        for row in self.map:
            for col in row:
                print(col, end="")
            print()
        print("☻  - You Are Here")
        print("▲  - Trees")
        print("█  - Vendors")
        print("§  - Marf the Dragon (Info/Save)")
        print("♥  - Water Tents")
        print("╔╗ - Fight the Knight")
        print("╚╝")

    def mapUI(self):
        returnList = []
        for row in self.map:
            line = ""
            for string in row:
                line += string
            returnList.append(line)
        returnList.append("☻  - You Are Here      ")
        returnList.append("▲  - Trees             ")
        returnList.append("█  - Vendors           ")
        returnList.append("§  - Marf the Dragon   ")
        returnList.append("♥  - Water Tents       ")
        returnList.append("╔╗ - Fight the Knight  ")
        returnList.append("╚╝                     ")
        return returnList
        

    def movement(self, curPosX = 3, curPosY = 10, playerChar = "☻", char = "·"):
        if newPos == "▲":
            print("The trees are much too dense to get through. Try another route.")
        else:
            #over-write old pos
            self.map[self.playerRow][self.playerCol] = fillChar

            #update pos
            self.playerRow = row
            self.playerCol = col

            #update map character
            self.map[row][col] = "☻"

    def add(self, row, col, char):
        self.map[row][col] = char


'''def main():
    mapList = makeMap()

    faireMap = TheMap(mapList)
    inventory = {"Weapon":"Sword", "Armor":"Shield", "Accessory":"HP Necklace +5", "Consumables":["Mead", "Soda"], "Spaces":[" ", " ", " ", " ", " ", " ", " ", " "]} 
    consumable = inventory.get("Consumables")
    spaces = inventory.get("Spaces")
    player = PlayerCharacter("Art", 10, 10, 10, 50, "sword", 1000, inventory, consumable, spaces, "Child")
    gameMapUI = faireMap.mapUI()
    gameStatsUI = player.statsUI()
    for x,y in zip(gameMapUI, gameStatsUI):
        print(x, "\t\t", y)
        
    

    
    
    

main()
input()
'''
