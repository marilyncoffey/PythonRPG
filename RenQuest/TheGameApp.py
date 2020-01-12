import renquestIntro
import character
import Map
import MapFile
import os
import msvcrt
import Items
import vendorclass
import sys
import random
import pickle

class TheGame(object):
    def __init__(self, playerName, knightChar, player):
        self.playerName = playerName
        self.knightChar = knightChar
        self.player = player

    def display(self, aList, bList):
        for x,y in zip(aList, bList):
            print(x, "\t\t", y)

    '''def set
	self.playerChar(for adding to inventory)
	self.curPos (for changing position)'''

    def mapMovement(self, theMap, curPosX, curPosY, fillChar, playerChar = "☻"):
        self.gameMap = theMap
        self.curPosX = curPosX
        self.curPosY = curPosY
        self.oldPos = fillChar
        self.playerChar = playerChar
        
    def vendors(self, curPosX, curPosY, pClass, pInventory, aMap, thePlayer):
        playerClass = pClass
        posX = curPosX
        posY = curPosY
        inventory = pInventory
        faireMap = aMap
        player = thePlayer
        shopping = True
        if posX == 3 and posY == 7:
            print("Welcome to Boffer's Blades! Look around and let me know how I can help you.")
            weaponVend = vendorclass.vendor("weapon", 15, 20)
            while shopping: 
                choice = weaponVend.printMenu()
                if choice == "1":
                    weapon = weaponVend.sell(playerClass, player.inventory)
                elif choice == "2":
                    weaponVend.charm(self.player.inventory.get("Charisma"))
                elif choice == "3":
                    weapon, caught = weaponVend.steal(self.player.inventory.get("Dexterity"), playerClass)
                    if caught == True:
                        print("You lose the game")
                        input()
                        sys.exit()
                elif choice == "4":
                    shopping = False
            inventory["Money"] = (inventory.get("Money") - weapon.get_price())
            inventory["Weapon"] = weapon
            inventory["Hit Points"] = inventory.get("Hit Points") - 1
            os.system('cls')
            print("That encounter took some effort, watch those hit points!")
            gameMapUI = faireMap.mapUI()
            gameStatsUI = player.statsUI(player.inventory)
            self.display(gameMapUI, gameStatsUI)
        if posX == 3 and posY == 12:
            print("As you approach the tent, you hear the sounds of beautiful music.")
            print('''
___|\_______|________|_______________________O__________@____________
___|/_______|________|_|___|__________|__@__|_____@__|_|____O._______||
__/|____4___|__O_____|_|___|__O.______|_|@__|____|___|_|___|O.______o||
_(_/^\__4__@|_|_____@__|___|_|________|_|@__|____|___|_|___|________o||
__\|/'_____@__|________|__@|_|________|_|________|___|_____|_________||
   d          |           @  |          |
''')
            print("\nYou can feel the music lifting your spirits and giving you confidence. \nAlmost like the sound of this music is going to make you harder to hit.")
            inventory["Dexterity"] = inventory.get("Dexterity") + 1
            inventory["Hit Points"] = inventory.get("Hit Points") - 1
            input("Press any key to continue.")
            os.system('cls')
            print("All that dancing kind of wore you out. Be sure to drink plenty of water!")
            gameMapUI = faireMap.mapUI()
            gameStatsUI = player.statsUI(player.inventory)
            self.display(gameMapUI, gameStatsUI)
        if posX == 4 and posY == 16:
            choice = input("You see trash. Do you want to investigate? y/n: ")
            if choice == "y":
                chance = random.randint(1, 100)
                if chance < 50:
                    print("you see bees...run!")
                    print('''
                 _  _
                | )/ )
             \\ |//,' __
             (")(_)-"()))=-
                (\\
                             _   _
  HEELP                     ( | / )
                          \\ \|/,' __
    \_o_/                 (")(_)-"()))=-
       )                     <\\
      /\__
_____ \ ________________________________
''')
                    input("Press any key to continue.")
                    inventory["Hit Points"] = inventory.get("Hit Points") - 2
                    os.system('cls')
                    print("That encounter took some effort, watch those hit points!")
                    gameMapUI = faireMap.mapUI()
                    gameStatsUI = player.statsUI(player.inventory)
                    self.display(gameMapUI, gameStatsUI)
                elif chance >= 50:
                    soda = Items.Consumable("soda", 3, 0)
                    print("you see an unopened soda and put it in your bag")
                    consumable = player.inventory.get("Consumables")
                    consumable.append(soda)
                    input("Press any key to continue.")
                    inventory["Hit Points"] = inventory.get("Hit Points") - 1
                    os.system('cls')
                    print("That encounter took some effort, watch those hit points!")
                    gameMapUI = faireMap.mapUI()
                    gameStatsUI = player.statsUI(player.inventory)
                    self.display(gameMapUI, gameStatsUI)
        if posX == 5 and posY == 5:
            print("The sign above this establishment says 'Red Dragon Tavern & Snack Bar'...\nperhaps getting some food for later would be a good idea.")
            water = Items.Consumable("water", 5, 2)
            mutton = Items.Consumable("mutton", 4, 6)
            mead = Items.Consumable("mead", 3, 4)
            liquor = Items.Consumable("liquor", 4, 5)
            turkey = Items.Consumable("turkey leg", 3, 5)
            shopping = True
            consumable = player.inventory.get("Consumables")
            while shopping:
                os.system('cls')
                gameMapUI = faireMap.mapUI()
                gameStatsUI = player.statsUI(player.inventory)
                self.display(gameMapUI, gameStatsUI)
                choice = input('''
╔══════════════════════════════════╗
║What food or drink would you like?║
╠══════════════════════════════════╣
║1 - Buy water for $2              ║
║2 - Buy mead for $4               ║
║3 - Buy liquor for $5             ║
║4 - Buy mutton for $6             ║
║5 - Buy turkey leg for $5         ║
║6 - Leave this area               ║
╚══════════════════════════════════╝
''')
                if choice == "1":
                    consumable.append(water)
                    inventory["Money"] = (inventory.get("Money") - water.get_price())
                elif choice == "2":
                    if playerClass == "Child":
                        print("I don't believe you're old enough to purchase that.")
                    else:
                        consumable.append(mead)
                        inventory["Money"] = (inventory.get("Money") - mead.get_price())
                elif choice == "3":
                    if playerClass == "Child":
                        print("I don't believe you're old enough to purchase that.")
                    else:
                        consumable.append(liquor)
                        inventory["Money"] = (inventory.get("Money") - liquor.get_price())
                elif choice == "4":
                    consumable.append(mutton)
                    inventory["Money"] = (inventory.get("Money") - mutton.get_price())
                elif choice == "5":
                    consumable.append(turkey)
                    inventory["Money"] = (inventory.get("Money") - turkey.get_price())
                elif choice == "6":
                    inventory["Consumables"] = consumable
                    inventory["Hit Points"] = inventory.get("Hit Points") - 1
                    shopping = False
            os.system('cls')
            print("Man it's hot outside, better stay hydrated!")
            gameMapUI = faireMap.mapUI()
            gameStatsUI = player.statsUI(player.inventory)
            self.display(gameMapUI, gameStatsUI)
        if posX == 6 and posY == 18:
            print("As you step into the tent, you see business cards with the name 'Patricia's Protectives' \non them. A pleasant looking gentleman smiles at you and says to ask if you have any questions.")
            armorVend = vendorclass.vendor("armor", 17, 25)
            while shopping: 
                choice = armorVend.printMenu()
                if choice == "1":
                    armor = armorVend.sell(playerClass, player.inventory)
                elif choice == "2":
                    armorVend.charm(self.player.inventory.get("Charisma"))
                elif choice == "3":
                    armor, caught = armorVend.steal(self.player.inventory.get("Dexterity"), playerClass)
                    if caught == True:
                        print("You lose the game")
                        input()
                        sys.exit()
                elif choice == "4":
                    shopping = False
            inventory["Money"] = (inventory.get("Money") - armor.get_cost())
            inventory["Armor"] = armor
            inventory["Hit Points"] = inventory.get("Hit Points") - 1
            os.system('cls')
            print("That encounter took some effort, watch those hit points!")
            gameMapUI = faireMap.mapUI()
            gameStatsUI = player.statsUI(player.inventory)
            self.display(gameMapUI, gameStatsUI)
        if posX == 7 and posY == 9:
            puck = vendorclass.vendor("puck", 0, 0)
            puck.theTrickster(player, player.inventory)
            inventory["Hit Points"] = inventory.get("Hit Points") - 1
            os.system('cls')
            print("Even thinking can take it's toll when it's hot. Visit a ♥ to buy some water!")
            gameMapUI = faireMap.mapUI()
            gameStatsUI = player.statsUI(player.inventory)
            self.display(gameMapUI, gameStatsUI)
        if posX == 10 and posY == 10:
            print("You hear the sounds of hooves and clanging metal. Interested, you move \ncloser. You see a couple of people wearing what look to be galvanized metal \ntrashcans shaped into the crude approximation of armor wailing on each other \nwith mop handles.")
            print('''

                   .oo.
                       .\\.                                            ..
                     ,'..''\\                                  ...oooo''
                     |  \\_/'                          ...oooo''
                     /''.'\\               .   ...oooo''
                    |  | '|           ...o!oo''
                    |  |  |.  ...oooo''./    '\\
                    |  '\\, """"\\     ./    ./\\ '\\.
                  /\\ooo''|""""-/ -../    / \\''   '\\.
                 /  '\\.  '|.''\\--/-+-+-+-+-+-+-+-+.'
           ....- \\.    \\.  '\\-'/',,   /'---/' """
        ././     ''\\.-.-.\\   '\\|   '',,\\--;
       /-/|             |-'\\.  '>       '\\\\
      !--!|            /---/' ./'          |
      !--!!          ./---/' ,/|           |
    ./'-/'|          |----\\  \\-|           |
  ./'--/  |..........|''''''./'|...........|
 -'-'-'   '/---/\\---|'          '/-\\--\\'"""
          /--/'  |--\\          ./---\\--\\
         |--|     \--\\.       ./--/' \\--\\
         |--|      |--|     ./--/'    \\--\\.
         '\\-|      '\\-|    /--/'       \\--|
          |..\\      |..\\  |..\\          |..\\

''')
            print("\nYou watch these fine gentlemen beat the hell out of each other for a few minutes. \nYou feel like you've learned a few things about fighting someone in armor.")
            inventory["Attack"] = inventory.get("Attack") + 1
            inventory["Hit Points"] = inventory.get("Hit Points") - 1
            input("Press any key to continue.")
            os.system('cls')
            print("Standing out in the sun like this sure is making you thirsty. Better get some water!")
            gameMapUI = faireMap.mapUI()
            gameStatsUI = player.statsUI(player.inventory)
            self.display(gameMapUI, gameStatsUI)

    def waterTent(self, player, aMap, pInventory, pMaxHP):
        thePlayer = player
        faireMap = aMap
        inventory = pInventory
        maxHP = pMaxHP
        water = Items.Consumable("water", 5, 2)
        pHP = inventory.get("Hit Points")
        if pHP <= 3:
            print("Wow, you look like you're about to die. Consider this on the house")
            inventory["Hit Points"] = maxHP
        else:
            shopping = True
            while shopping:
                choice = input('''
    ╔══════════════════════════════════╗
    ║Buy some damn water               ║
    ╠══════════════════════════════════╣
    ║1 - Buy water for $2              ║
    ║2 - Leave this area               ║
    ╚══════════════════════════════════╝
    ''')
                if choice == "1":
                    inventory["Hit Points"] = maxHP
                    inventory["Money"] = (inventory.get("Money") - water.get_price())
                    print("As you down the cool water, you feel fully refreshed and ready for more adventures!")
                    input()
                elif choice == "2":
                    shopping = False
                    inventory["Hit Points"] = inventory.get("Hit Points") - 1
                    os.system('cls')
                    print("Weird how even buying water makes you thirsty.")
                    gameMapUI = faireMap.mapUI()
                    gameStatsUI = player.statsUI(player.inventory)
                    self.display(gameMapUI, gameStatsUI)
    def theInfoDragon(self, theGame):
        print('''
                \\||/
                |  @___oo
      /\\  /\\   / (__,,,,|
     ) /^\\) ^\\/ _)
     )   /^\\/   _)
     )   _ /  / _)
 /\  )/\\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \\)___)\\
 | \\____(      )___) )___
  \\______(_______;;; __;;;
''')
        saveGame = open('savegame.txt', 'wb')
        savegameDict["name"] = name
        savegameDict["playerClass"] = playerClass
        savegameDict["ATK"] = atk
        savegameDict["DEX"] = dex
        savegameDict["CHA"] = cha
        savegameDict["HP"] = HP
        savegameDict["Money"] = money
        savegameDict["inventory"] = inventory
        pickle.dump(savegameDict, saveGame)
        saveGame.close()
        
        info = ["sun", "street", "hydrate", "vendors", "joke1", "joke2", "joke3"]
        pick = random.choice(info)
        if pick == "sun":
            print('Marf the Dragon says: "Never look directly into the sun!"')
            input()
        elif pick == "street":
            print('Marf the Dragon says: "Always look both ways before crossing the street!"')
            input()
        elif pick == "hydrate":
            print('Marf the Dragon says: "Keep an eye on your health. You lose some every time you encounter things."')
            input()
        elif pick == "vendors":
            print('Marf the Dragon says: "We have some of the best vendors here, make sure you visit them all!"')
            input()
        elif pick == "joke1":
            print('Marf the Dragon says: "Why are dragons such good story tellers?"')
            input()
            print('"They have very impressive tails!"')
            input()
        elif pick == "joke2":
            print('Marf the Dragon says: "What did the dragon say when he saw the knight?"')
            input()
            print('"Look, canned food!!"')
            input()
        elif pick == "joke3":
            print('Marf the Dragon says: "What\'s the difference between a dragon and a mite?"')
            input()
            print('"A dragon can have mites bit a mite can\'t have dragons."')
            input()
        print("You walk away from Marf the Dragon whosometimes thinks he's really funny. \nIt may be the heat, but you could have sworn he did some kind of magic to preserve \nthat exact moment and all that had transpired here at the faire.")
                
                    
#Random encounters(self, encounterList)
#	Random roll to determine if random encounter
#	If encounter, instantiate from random encounter class
#	Use random encounter methods to complete encounter'''

    def battle(self, thePlayer, pInventory, theKnight, kWeapon):
        player = thePlayer
        inventory = pInventory
        consumables = inventory.get("Consumables")
        playerClass = inventory.get("Player Class")
        knight = theKnight
        knightWeapon = kWeapon
        water = Items.Consumable("water", 5, 2)
        mutton = Items.Consumable("mutton", 4, 6)
        mead = Items.Consumable("mead", 3, 4)
        liquor = Items.Consumable("liquor", 4, 5)
        turkey = Items.Consumable("turkey leg", 3, 5)
        soda = Items.Consumable("soda", 3, 0)
        #battle intro - print from txt file, use text from outline
        file = open("KnightIntro.txt", "r")
        for x in file:
            renquestIntro.slowPrint(x, .025)
        file.close()
        input("\nHit enter to step into the ring.")
        
        fighting = True
        knightImg = ('''
      _,.
    ,` -.)
   ( _/-\\\\-._
  /,|`--._,-^|            ,
  \\_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \\   `---'   \   /  /
    |           |./  /
    /           //  /
\\_/' \\         |/  /
 |    |   _,^-'/  /
 |    , ``  (\\/  /_
  \\,.->._    \\X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()
''')
        adultImg = ('''\n
                 ,#####,
                 #_   _#                              /\\
                 |a` `a|                             / /
                 |  u  |                            / /
                 \\  =  /                          / /
                 |\\___/|                         / /
        ___ ____/:     :\\____ ___               / /
      .'   `.-===-\\   /-===-.`   '.            / /
     /      .-"""""-.-"""""-.      \\          / /
    /'             =:=             '\\        / /
  .'  ' .:    o   -=:=-   o    :. '  `.      / /
  (.'   /'. '-.....-'-.....-' .'\\   '.)    / /
  /' ._/   ".     --:--     ."   \\_. '\\  / /
 |  .'|      ".  ---:---  ."      |'.  |  / /
 |  : |       |  ---:---  |       | :  |\\ /
  \\ : |       |_____._____|       | : ///\\
  /   (       |----|------|       )   \\/  \\
 /... .|      |    |      |      |. ...\\
|::::/''     /     |       \\     ''\\::::|
'""""       /'    .L_      `\\     //""""'
           /'-.,__/` `\\__..-'\\  //
          ;      /     \\      ;  O
          :     /       \\     |
         -----------------------------
''')
        childImg = ('''
               ,,,,,,,,,,,  
              //////// \\\\\\\\
             // ==     == \\\\
              (  o    o  )\\\\
     .        (     L    )\\
    / \        (  .___  )\\\\
    | |         (______)\\\\
    | |           |   |\\\\
    |.|    ------/  ^  \\----
    |.|   /     ~~~o~~~~    \\
    |:|  I         o         I
    |:| I    I     o     I    I
  `--8--'   II     o     II   I
   I 8 II   II     o  |`-._/\_.-`|
    IO  I   II     o  |    ||    |
     I______II     o  |___o()o___|
             I%%%%%%@%|__((<>))__|
             I        \\   o\\/o   /
             I         \\   ||   /    
             I     i    \\  ||  /
             I     I     '.||.'
             I     I     I ``
             I     I     I
              I____I____I
            __I    II   I__
           (_______II______)
''')
        larperImg = ('''
                        ______
      ,-'""`-,         /\\     \\  
    ,'        `.      /  \\     \\
   /    _,,,_   \\    /    \\#####\\
  /   ,'  |  `\\/\\\\  /    # \\     \\
 /   /,--' `--.  ` /    #   \\_____\\ 
 |   /      ___\\_  \   #    /     /
 |  | /  ______|    \ #    /     /
 |  | |  |_' \'|    / /\  /     /  
 \\ ,' (   _) -`|   / /  \/_____/       
  '--- \\ '-.-- /  / /           
 ______/`--'--<  / /            
 |    |`-.  ,;/``--._        
 |    |-. _///     ,'`\      
 |    |`-Y;'/     /  ,-'\    
 |    | // <_    / ,'  ,-'\  
 '----'// -- `-./,' ,-'  \\/  
  |   //[==]     \,' \_.,-\\  
  |  //      `  -- | \__.,-' 
    // -[==]_      |   ____\\ 
   //          `-- |--' |   \\
        [==__,,,,--'    |-'" 
    ---""''             |    
             ___...____/     
        --------------------.
''')
        animeImg = ('''
                     ._                                 
                  ,-'_ `-.                              
                  ::".^-. `.                            
                  ||<    >. \\                           
                  |: _, _| \\ \\                          
                  : .'| '|  ;\\`.                        
                  _\\ .`  '  | \\ \\                       
                .' `\\ *-'   ;  . \\                      
               '\\ `. `.    /\\   . \\                     
             _/  `. \\  \\  :  `.  `.;                    
           _/ \\  \\ `-._  /|  `  ._/                     
          / `. `. `.   /  :    ) \\                      
          `;._.  \\  _.'/   \\ .' .';                     
          /     .'`._.* /    .-' (                      
        .'`._  /    ; .' .-'     ;                      
        ; `._.:     |(    ._   _.'|                     
        `._   ;     ; `.-'        |                     
         |   / .-'./ .'  \\ .     /:                     
         |  +.'  \\ `-.   .\\ *--*' ;\\                    
         ;.' `. \\ `.    /` `.    /  .                   
        /.L-'\\_: L__..-*     \\   ".  \\                  
      :/ / .' `' ;   `-.     `.   \\  .                 
      / /_/     /              \\   ;  \\                
    _/ /       /          \\     `./    .               
   .  ;       /    .'      `-.   ;      \\              
  /  /       ,    /           `"' \\      .             
 .  '       /   .'                 `.     \\            
/  /       /   /                  |  `-.   .           
''')
        while fighting:
            knightTurn = True
            os.system('cls')
            playerStatsUI = player.playerBattleStatsUI(player.inventory)
            knightStatsUI = knight.battleStatsUI()
            self.display(playerStatsUI, knightStatsUI)
            if playerClass == "Adult":
                print(adultImg)
            elif playerClass == "Child":
                print(childImg)
            elif playerClass == "LARPer":
                print(larperImg)
            elif playerClass == "Anime Fan":
                print(animeImg)
            choice = input('''
╔══════════════════════════════════╗
║What would you like to do?        ║
╠══════════════════════════════════╣
║1 - Regular Attack                ║
║2 - Special Attack                ║
║3 - Use Item                      ║
╚══════════════════════════════════╝
''')
            if choice == "1":
                toHit = player.regAttack()
                if toHit >= knight.getDex():
                    weapon = inventory.get("Weapon")
                    toDmg = weapon.get_damage()
                    dmg = random.randint(1, toDmg)
                    knightHP = knight.getHP()
                    print("You deal " + str(dmg) + " points of damage to the knight.")
                    knight.setHP((knightHP - dmg))
                    input()
                else:
                    print("You missed.")
                    input()
            elif choice == "2":
                if playerClass == "Adult":
                    toHit, drunkRage = player.specialAttack(playerClass)
                    if toHit >= knight.getDex():
                        weapon = inventory.get("Weapon")
                        toDmg = weapon.get_damage()
                        dmg = random.randint(1, toDmg)
                        knightHP = knight.getHP()
                        print("The alcohol in your blood strengthens you and you strike a mightty blow of " + str(dmg +drunkRage) + " points of damage to the knight.")
                        knight.setHP((knightHP - dmg - drunkRage))
                        input()
                    else:
                        print("You missed.")
                        input()
                #Add child
                if playerClass == "Child":
                    knightTurn = player.specialAttack(playerClass)
                    print("You begin crying tears of entitlement that this isn't fair and the world is too hard. The knight seems confused.")
                #Add LARPer
                if playerClass == "LARPer":
                    toHit = player.specialAttack(playerClass)
                    if toHit >= knight.getDex():
                        weapon = inventory.get("Weapon")
                        toDmg = weapon.get_damage()
                        dmg1 = random.randint(1, toDmg)
                        dmg2 = random.randint(1, toDmg)
                        knightHP = knight.getHP()
                        print("All those weekend LARP events have prepared you well for this very moment. \nYou've been practicing thos move for some time. You swing once and hit for " + str(dmg1) + " \npoints of damage and before the knight knows what is happening, you swing back for another \n" + str(dmg2) + "points of damage!")
                        knight.setHP((knightHP - dmg1 - dmg2))
                        input()
                    else:
                        print("You missed.")
                        input()
                #Add Anime Fan
                if playerClass == "Anime Fan":
                    heal = player.specialAttack(playerClass)
                    inventory["Hit Points"] = inventory.get("Hit Points") + heal
                    print("You heal for " + str(heal) + " points of damage.")
                    input()
            elif choice == "3":
                if len(consumables) > 0:
                    os.system('cls')
                    playerStatsUI = player.playerBattleStatsUI(player.inventory)
                    knightStatsUI = knight.battleStatsUI()
                    self.display(playerStatsUI, knightStatsUI)
                    print(playerImg)
                    for x in consumables:
                        print(str(x))
                    itemChoice = input("Which item would you like to use?")
                    if itemChoice == "water":
                        heal = water.get_heal()
                        inventory["Hit Points"] = inventory.get("Hit Points") + heal
                        print("You heal for " + str(heal) + " points of damage.")
                        input()
                    elif itemChoice == "mutton":
                        heal = mutton.get_heal()
                        inventory["Hit Points"] = inventory.get("Hit Points") + heal
                        print("You heal for " + str(heal) + " points of damage.")
                        input()
                    elif itemChoice == "mead":
                        heal = mead.get_heal()
                        inventory["Hit Points"] = inventory.get("Hit Points") + heal
                        print("You heal for " + str(heal) + " points of damage.")
                        input()
                    elif itemChoice == "liquor":
                        heal = liquor.get_heal()
                        inventory["Hit Points"] = inventory.get("Hit Points") + heal
                        print("You heal for " + str(heal) + " points of damage.")
                        input()
                    elif itemChoice == "turkey":
                        heal = turkey.get_heal()
                        inventory["Hit Points"] = inventory.get("Hit Points") + heal
                        print("You heal for " + str(heal) + " points of damage.")
                        input()
                    elif itemChoice == "soda":
                        heal = soda.get_heal()
                        inventory["Hit Points"] = inventory.get("Hit Points") + heal
                        print("You heal for " + str(heal) + " points of damage.")
                        input()
                    elif itemChoice == "Full Health":
                        maxHP = player.getHP()
                        inventory["Hit Points"] = maxHP
                        print("You heal for to full hit points.")
                        input()
                    else:
                        print("You waste time looking for an item that you don't have.")
                else:
                    print("You waste time looking for an item that you don't have.")
            elif choice == "4":
                dmg = 100
                knightHP = knight.getHP()
                print("You hit really hard and nearly kill the poor guy.")
                knight.setHP((knightHP - dmg))
                input()
            knightHP = knight.getHP()
            if knightHP <= 0:
                os.system('cls')
                file = open("RenQuestWinText.txt", "r")
                for x in file:
                    renquestIntro.slowPrint(x, .025)
                input()
                file.close()
            os.system('cls')
            playerStatsUI = player.playerBattleStatsUI(player.inventory)
            knightStatsUI = knight.battleStatsUI()
            self.display(playerStatsUI, knightStatsUI)
            playerAC = inventory.get("Dexterity")
            print(knightImg)
            if knightTurn == "False":
                print("Still confused from your earlier rant, the knight stands there just \ntrying to figure out what to do next.")
            else:
                if knightHP < 10:
                    if knight.healed < 1:
                        print("The knight seems weak from your battle. He draws himself up to his full \nheight and begins chanting \"Fight. The. Knight.\" Soon everyone \nis chanting and it's almost as if that chant has healed him!")
                        heal = knight.specialAttack()
                        knight.setHP(knightHP + heal)
                    else:
                        healChance = random.randint(1, 100)
                        if healChance <= 25:
                            print("The knight seems weak from your battle. He draws himself up to his full \nheight and begins chanting \"Fight. The. Knight.\" Soon everyone \nis chanting and it's almost as if that chant has healed him!")
                            heal = knight.specialAttack()
                            knight.setHP(knightHP + heal)
                        else:
                            toHit = player.knightAttack()
                            if toHit >= playerAC:
                                toDmg = knightWeapon.get_damage()
                                dmg = random.randint(1, toDmg)
                                inventory["Hit Points"] = inventory.get("Hit Points") - dmg
                                print("The knight strikes a mighty blow and does " + str(dmg) + " points of damage to you.")
                                input()
                            else:
                                print("The Knight missed.")
                                input()
                else:
                    toHit = player.knightAttack()
                    if toHit >= playerAC:
                        toDmg = knightWeapon.get_damage()
                        dmg = random.randint(1, toDmg)
                        inventory["Hit Points"] = inventory.get("Hit Points") - dmg
                        print("The knight strikes a mighty blow and does " + str(dmg) + " points of damage to you.")
                        input()
                    else:
                        print("The Knight missed.")
                        input()
                if inventory.get("Hit Points") <= 0:
                    os.system('cls')
                    file = open("RenQuestLoseText.txt", "r")
                    for x in file:
                        renquestIntro.slowPrint(x, .025)
                    input()
                    file.close()
    
'''
	Battle options for knight
		If knight’s turn != False
		Use knight’s battle method to complete
	If knight’s damage would reduce player <0
		Don’t do damage, knight faints/falls over instead
		Go to ending ‘loss’ condition (print from txt file)
	If knight’s damage won’t reduce player <0
		Apply damage
		Loop battle
'''	
	
		
def main():

#create map
    mapList = MapFile.makeMap()
    faireMap = Map.TheMap(mapList)
#intro
    theGame, loaded = renquestIntro.intro()
    playerStats = renquestIntro.chooseChar()
    os.system('cls')
#create player character
    if loaded != True:
        inventory = {"Name":"", "Attack":0, "Dexterity":0, "Charisma":0, "Hit Points":0, "Weapon":"", "Player Class":"", "Money":0, "Consumables":[], "Spaces":["", "", "", "", "", "", "", ""]}
        consumable = inventory.get("Consumables")
        spaces = inventory.get("Spaces")
        dagger = Items.Weapon("Dagger", 0, 4, 0)
        armor = Items.Armor("", 0, 0)
        necklace = Items.Armor("", 0, 0)
        inventory["Weapon"] = dagger
        inventory["Armor"] = armor
        inventory["Accessory"] = necklace
        inventory["Name"] = playerStats.get("name")
        inventory["Player Class"] = playerStats.get("playerClass")
        inventory["Attack"] = playerStats.get("ATK")
        inventory["Dexterity"] = playerStats.get("DEX")
        inventory["Charisma"] = playerStats.get("CHA")
        inventory["Hit Points"] = playerStats.get("HP")
        inventory["Money"] = playerStats.get("money")
        player = character.Player(inventory.get("Name"), inventory.get("Attack"), inventory.get("Dexterity"), inventory.get("Charisma"), inventory.get("Hit Points"), inventory.get("Weapon"), inventory.get("Money"),inventory, consumable, spaces, inventory.get("Player Class"))
        playerClass = inventory.get("Player Class")
        maxHP = player.getHP()

#create the knight
        knightWeapon = Items.Weapon("Two-Handed Sword", 3, 6, 0)
        knight = character.Character("The Knight", 7, 7, 8, 50, knightWeapon) 
#create the game
        theGame = TheGame(inventory.get("Name"), knight, player)
#set fill character
    oldPos = "·"
#create display
    print("Use arrow keys to move around the map")
    gameMapUI = faireMap.mapUI()
    gameStatsUI = player.statsUI(player.inventory)
    theGame.display(gameMapUI, gameStatsUI)
#set current player variables 
    curPosX = 2
    curPosY = 10
    newPos = "·"
    
#loop to allow movement to continue
#    curPosX = 6
#    curPosY = 18
    newPos = "§"
    if newPos == "§":
        theGame.theInfoDragon(theGame)
    while True:
        uIn = ord(msvcrt.getch())
        playerChar = "☻"
        if uIn == 224: #special character
            uIn = ord(msvcrt.getch())
            os.system('cls')
            message, dead, level = player.healthValidation(inventory)
            if level != 1:
                os.system('cls')
                print(message)
                if dead == True:
                    print("\nYou lose the game")
                    input()
                    sys.exit()
            if uIn == 72: #UP
                newPosX = (curPosX - 1)
                newPos = faireMap.getFillChar(newPosX, curPosY)
                print("Your current position: " + newPos)
                if newPos == "▲":
                    theGame.display(gameMapUI, gameStatsUI)
                    print("The trees are too dense to go through. Choose another direction.")
                else:
                    faireMap.setFillChar(curPosX, curPosY, oldPos)
                    faireMap.setFillChar(newPosX, curPosY, playerChar)
                    oldPos = newPos
                    curPosX = newPosX
                    gameMapUI = faireMap.mapUI()
                    gameStatsUI = player.statsUI(player.inventory)
                    theGame.display(gameMapUI, gameStatsUI)
                    if newPos == "█":
                        theGame.vendors(curPosX, curPosY, playerClass, player.inventory, faireMap, player)
                    elif newPos == "♥":
                        theGame.waterTent(player, faireMap, inventory, maxHP)
                    elif newPos == "╔" or newPos == "╗" or newPos == "╚" or newPos == "╝":
                        theGame.battle(player, inventory, knight, knightWeapon)
                    elif newPos == "§":
                        theGame.theInfoDragon(theGame)
            if uIn == 80: #DOWN
                newPosX = (curPosX+1)
                newPos = faireMap.getFillChar(newPosX, curPosY)
                print("Your current position: " + newPos)
                if newPos == "▲":
                    theGame.display(gameMapUI, gameStatsUI)
                    print("The trees are too dense to go through. Choose another direction.")
                else:
                    faireMap.setFillChar(curPosX, curPosY, oldPos)
                    faireMap.setFillChar(newPosX, curPosY, playerChar)
                    oldPos = newPos
                    curPosX = newPosX
                    gameMapUI = faireMap.mapUI()
                    gameStatsUI = player.statsUI(player.inventory)
                    theGame.display(gameMapUI, gameStatsUI)
                    if newPos == "█":
                        theGame.vendors(curPosX, curPosY, playerClass, player.inventory, faireMap, player)
                    elif newPos == "♥":
                        theGame.waterTent(player, faireMap, inventory, maxHP)
                    elif newPos == "╔" or newPos == "╗" or newPos == "╚" or newPos == "╝":
                        theGame.battle(player, inventory, knight, knightWeapon)
                    elif newPos == "§":
                        theGame.theInfoDragon(theGame)
            if uIn == 75: #LEFT
                newPosY = (curPosY-1)
                newPos = faireMap.getFillChar(curPosX, newPosY)
                print("Your current position: " + newPos)
                if newPos == "▲":
                    theGame.display(gameMapUI, gameStatsUI)
                    print("The trees are too dense to go through. Choose another direction.")
                else:
                    faireMap.setFillChar(curPosX, curPosY, oldPos)
                    faireMap.setFillChar(curPosX, newPosY, playerChar)
                    oldPos = newPos
                    curPosY = newPosY
                    gameMapUI = faireMap.mapUI()
                    gameStatsUI = player.statsUI(player.inventory)
                    theGame.display(gameMapUI, gameStatsUI)
                    if newPos == "█":
                        theGame.vendors(curPosX, curPosY, playerClass, player.inventory, faireMap, player)
                    elif newPos == "♥":
                        theGame.waterTent(player, faireMap, inventory, maxHP)
                    elif newPos == "╔" or newPos == "╗" or newPos == "╚" or newPos == "╝":
                        theGame.battle(player, inventory, knight, knightWeapon)
                    elif newPos == "§":
                        theGame.theInfoDragon(theGame)
            if uIn == 77: #RIGHT
                newPosY = (curPosY+1)
                newPos = faireMap.getFillChar(curPosX, newPosY)
                print("Your current position: " + newPos)
                if newPos == "▲":
                    theGame.display(gameMapUI, gameStatsUI)
                    print("The trees are too dense to go through. Choose another direction.")
                else:
                    faireMap.setFillChar(curPosX, curPosY, oldPos)
                    faireMap.setFillChar(curPosX, newPosY, playerChar)
                    oldPos = newPos
                    curPosY = newPosY
                    gameMapUI = faireMap.mapUI()
                    gameStatsUI = player.statsUI(player.inventory)
                    theGame.display(gameMapUI, gameStatsUI)
                    if newPos == "█":
                        theGame.vendors(curPosX, curPosY, playerClass, player.inventory, faireMap, player)
                    elif newPos == "♥":
                        theGame.waterTent(player, faireMap, inventory, maxHP)
                    elif newPos == "╔" or newPos == "╗" or newPos == "╚" or newPos == "╝":
                        theGame.battle(player, inventory, knight, knightWeapon)
                    elif newPos == "§":
                        theGame.theInfoDragon(theGame)
        

main()
input()
        

    
'''Call intro function(which creates character object)
	Name = character.name
	curPos = character.curPos
	Instantiate knight character
	Call map/stats to string function
	map/stats = map/stats string
	Call The Game class (Name, knightCharacter, playerCharacter, curPos, map/stats string)
	Use move method to traverse the map
	Use random encounter method for random encounters
	Use vendor method for vendor encounters
	Use battle method when player goes to Fight the Knight
	
	Would you like to play again? Y/N
	If yes, loop'''
