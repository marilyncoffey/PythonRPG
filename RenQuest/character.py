import random

class Character(object):
    healed = 0
    def __init__(self,name, atk, dex, cha, hp, weapon):
        self.name = name
        self.attack = atk
        self.dex = dex
        self.charisma = cha
        self.charHP = hp
        self.weapon = weapon

    #to string
    def __str__(self):
        result = ""
        result += "\nName: " + self.name
        result += "\nATK: " + str(self.attack)
        result += "\nDEX: " + str(self.dex)
        result += "\nCHA: " + str(self.charisma)
        result += "\nHP: " + str(self.charHP)

    #knight build
    def setHP(self, newHP):
        self.charHP = newHP

    def getDex(self):
        return self.dex

    def getHP(self):
        return self.charHP

    def knightAttack(self):
        toHit = (random.randint(1, 20) + self.attack + self.weapon.get_toHit())
        return toHit

    def knightSpecial(self):
        print("The Knight is weak and looks like he will soon fall. He looks to the crowd and begins chanting 'Fight. The. Knight.' His spirits seem bolstered and his morale restored!")
        heal = random.randint(1, self.charisma)
        healed += 1
        return heal

    def battleStatsUI(self):
        returnList = []
        returnList.append("|Name: " + self.name)
        returnList.append("|ATK: " + str(self.attack))
        returnList.append("|DEX: " + str(self.dex))
        returnList.append("|CHA: " + str(self.charisma))
        returnList.append("|HP: " + str(self.charHP))
        return returnList

class Player(Character):
    def __init__(self, name, atk, dex, cha, hp, weapon, money, inventory, consumables, spaces, playerClass):
        super().__init__(name, atk, dex, cha, hp, weapon)
        self.money=money
        self.inventory=inventory
        self.consumables = consumables
        self.spaces = spaces
        self.playerClass=playerClass
        self.weapon=weapon

    #to string
    def __str__(self):
        result=super().__str__(self, inventory, playerClass, money)
        result+="Type: "+ self.playerClass + "\n"
        result+="Money: " + str(self.money) + "\n"
        result+="Weapon: " + self.weapon + "\n"
        return result

    def healthValidation(self, inventory):
        playerHP = inventory.get("Hit Points")
        dead = False
        if playerHP > 5:
            message = "You're doing an excellent job staying hydrated!"
            level = 1
        elif playerHP <= 5 and playerHP >= 3:
            message = "You're looking pretty worn out! You might need to get some water soon."
            level = 2
        elif playerHP <=2 and playerHP >=1:
            message = "You're in serious danger of dehydration! Get some water immediately!"
            level = 3
        elif playerHP <= 0:
            dead = True
            message = '''
            .---------.
       _    |:: [-=-] |
      | |   |_________|
      |~|
      |_|                    ,;;;;,
       I\\  ,__ ,;;;, __,    ///\\\\\\\\\\
       I |{   / . . \\   }   / "  \\\\||
       I | ) (   _   ) (    \_= _///
       I |{___'-. .-'___}\___ )_\\
       I ||~/,'~~~~~,\\\~~|'---((  \\
       I \\ //        \\\ |     \\ \\ \\
       I  \\/         // |     | /-/
       I (/         (/  |     |/||\\
       I  |             |     |    |
       I  |             |     |____/
       I  :-----_o_-----:      || |
       I  | /~~|===|~~\\ |      (( |
       I  ||   |===|   ||      ||_/
      /^\\ "~   '^^^'   ""     ((__|

Your vision suddenly goes white, and then fades to nothing. An indeterminable time later, you wake up in a hospital bed.\n
A doctor is by your bedside, flicking between pages on a clipboard. "Well," she says, "The good news is that you're awake.\n
The bad news, however, is that you suffered a massive heat stroke brought on by dehydration. You were rushed in as quickly \n
as possibly, but not before irreversible brain damage occurred. You have a long, difficult recovery ahead of you, and most \n
likely, you'll never regain full physical or mental functionality again."'''
            level = 4
        return message, dead, level
    
    def statsUI(self, pInventory):
        inventory = pInventory
        returnList = []
        returnList.append("|Name: " + inventory.get("Name"))
        returnList.append("|ATK: " + str(inventory.get("Attack")))
        returnList.append("|DEX: " + str(inventory.get("Dexterity")))
        returnList.append("|CHA: " + str(inventory.get("Charisma")))
        necklace = self.inventory.get("Accessory", " ")
        neckHP = necklace.get_ac()
        returnList.append("|HP: " + (str(inventory.get("Hit Points") + neckHP)))
        returnList.append("|Money: " + str(inventory.get("Money")))
        weapon = self.inventory.get("Weapon", " ")
        weaponName = weapon.get_name()
        returnList.append("|Weapon: " + weaponName)
        armor = self.inventory.get("Armor", " ")
        armorName = armor.get_name()
        returnList.append("|Armor: " + armorName)
        necklace = self.inventory.get("Accessory", " ")
        accName = necklace.get_name()
        returnList.append("|Accessory: " + accName)
        returnList.append("|Consumables: ")
        consumables = inventory.get("Consumables")
        for x in consumables:
            returnList.append("|\t" + str(x))
        for x in self.spaces:
            returnList.append("|\t" + x)
        return returnList

    def playerBattleStatsUI(self, pInventory):
        inventory = pInventory
        returnList = []
        returnList.append("|Name: " + inventory.get("Name"))
        returnList.append("|ATK: " + str(inventory.get("Attack")))
        returnList.append("|DEX: " + str(inventory.get("Dexterity")))
        returnList.append("|CHA: " + str(inventory.get("Charisma")))
        returnList.append("|HP: " + str(inventory.get("Hit Points")))
        return returnList
    
    #Getters
        def getName(self):
            return self.name
        def getplayerClass(self):
            return self.playerClass
        def getATK(self):
            return self.ATK
        def getDEX(self):
            return self.DEX
        def getCHA(self):
            return self.CHA
        def getHP(self):
            return self.charHP
        def getMoney(self):
            return self.money
        def getInventory(self):
            return self.inventory


    #Player Regular Attack method
    def regAttack(self):
        toHit = (random.randint(1, 20)) + self.attack + self.weapon.get_toHit()
        return toHit

    #Player Special Attack Method
    def specialAttack(self, playerClass):
        if playerClass == "Adult":
            toHit=(random.randint(1, 20)) + self.attack + self.weapon.get_toHit()
            drunkRage=(random.randint(1,6))
            return toHit, drunkRage

        elif playerClass == "Child":  
            knightTurn = False
            return knightTurn
                    
        elif playerClass == "LARPer":
            toHit=(random.randint(1, 20)) + self.attack + self.weapon.get_toHit()
            return toHit

        elif playerClass == "Anime Fan":
            print("You begin a Subs vs. Dubs lecture which invigorates you and makes you feel healthy again!")
            heal = random.randint(1, 15)
            return heal
            
        elif playerClass == "King Arthur":
            toHit=(random.randint(1, 20)) + self.attack + self.weapon.get_toHit()
            return toHit
