import pickle, os

def clearScreen():
    os.system('cls')
    os.system('clear')

def slowPrint(s,delay):
    import time
    for letter in s:
        print(letter,end="")
        time.sleep(delay)

def playIntro():
    print("""\n\n\n\n\n\n
           ,   ,
         ,-`{-`/
      ,-~ , \ {-~~-,
    ,~  ,   ,`,-~~-,`,
  ,`   ,   { {      } }                                             }/
 ;     ,--/`\ \    / /                                     }/      /,/
;  ,-./      \ \  { {  (                                  /,;    ,/ ,/
; /   `       } } `, `-`-.___                            / `,  ,/  `,/
 \|         ,`,`    `~.___,---}                         / ,`,,/  ,`,;
  `        { {                                     __  /  ,`/   ,`,;
        /   \ \                                 _,`, `{  `,{   `,`;`
       {     } }       /~\         .-:::-.     (--,   ;\ `,}  `,`;
       \\._./ /       /` , \      ,:::::::::,     `~;   \},/  `,`;     ,-=-
        `-..-`      /. `  .\_   ;:::::::::::;  __,{     `/  `,`;     {
                   / , ~ . ^ `~`\:::::::::::<<~>-,,`,    `-,  ``,_    }
                /~~ . `  . ~  , .`~~\:::::::;    _-~  ;__,        `,-`
       /`\    /~,  . ~ , '  `  ,  .` \::::;`   <<<~```   ``-,,__   ;
      /` .`\ /` .  ^  ,  ~  ,  . ` . ~\~                       \\, `,__
     / ` , ,`\.  ` ~  ,  ^ ,  `  ~ . . ``~~~`,                   `-`--,,\\
    / , ~ . ~ \ , ` .  ^  `  , . ^   .   , ` .`-,___,---,__            
  /` ` . ~ . ` `\ `  ~  ,  .  ,  `  ,  . ~  ^  ,  .  ~  , .`~---,___
/` . `  ,  . ~ , \  `  ~  ,  .  ^  ,  ~  .  `  ,  ~  .  ^  ,  ~  .  `-,
""")
    print("""
------------------------------------------------------------------------
                            INTRODUCTION
------------------------------------------------------------------------
""")
    file=open("renquestIntroStory.txt","r", encoding="UTF-8")
    introFile = file.readlines()
    file.close()
    slowPrint(introFile, .5)
    input("Press any key to continue.")

def chooseChar():
    name=input("What is your name, fairegoer?:")
    print("""
------------------------------------------------------------------------
                        CHOOSE YOUR CHARACTER
------------------------------------------------------------------------
╔═══╤══════════════════════════════════════════════════════════════════╗
║   │ Character   Attack   Dexterity   Charisma   Health Points   Cash ║
╟───┼──────────────────────────────────────────────────────────────────╢
║ 1 │ Adult       5        1           2          18              $100 ║
║   │ Tavern barfly- love of mutton only rivaled by need for mead.     ║
║   │ Special attack - Drunken Rage                                    ║
║ 2 │ Child       1        8           8          10              $30  ║
║   │ They dream of one day being as cool as the jousting knights.     ║
║   │ Special attack - Tears of Entitlement			       ║
║ 3 │ LARPer      5        1           5          20              $50  ║
║   │ Mouth breathing medieval enthusiast, goes nowhere without his    ║
║   │ chainmail suit. Not even the grocery store.		       ║
║   │ Special attack - Double Attack			               ║
║ 4 │ Anime       8        3           1          15              $70  ║
║   │ Thinks that any excuse to dress in their costume is worthwhile,  ║
║   │ I mean, they spent a LOT of time creating it!		       ║
║   │ Special attack - Subs vs Dubs Lecture    			       ║
╚═══╧══════════════════════════════════════════════════════════════════╝
""")
    playerStats={}
    
    choice=input("Which character type are you?:")
    while(choice != "1" and choice != "2" and choice !="3" and choice !="4" and choice != "5"):
        print("Invalid choice.")
        playerClass = input("Which character type are you?:")

    if(choice == "1"):
        playerClass = "Adult"
        atk = 5
        dex = 1
        cha = 2
        HP = 18
        money = 100
        
    elif(choice == "2"):
        playerClass = "Child"
        atk = 1
        dex = 8
        cha = 8
        HP = 10
        money = 30

    elif(choice =="3"):
        playerClass = "LARPer"
        atk = 5
        dex = 1
        cha = 5
        HP = 20
        money = 50

    elif(choice =="4"):
        playerClass = "Anime Fan"
        atk = 8
        dex = 3
        cha = 1
        HP = 15
        money = 70
        
    elif(choice =="5"):
        playerClass = "King Arthur"
        atk = 20
        dex = 10
        cha = 10
        HP = 200
        money = 1000

    else:
        choice=input("Which character type are you?:")
    
    playerStats["name"]=name
    playerStats["playerClass"]=playerClass
    playerStats["ATK"]=atk
    playerStats["DEX"]=dex
    playerStats["CHA"]=cha
    playerStats["HP"]=HP
    playerStats["money"]=money

    return playerStats

def loadGame():
    saveFile = open("save.bin", "rb")
    theGame = pickle.load(saveFile)
    saveFile.close()
    return theGame
    
        
def intro():
    print("""
     ***** ***                             * ***                                                
  ******  * **                           *  ****                                          *     
 **   *  *  **                          *  *  ***                                        **     
*    *  *   **                         *  **   ***                                       **     
    *  *    *                         *  ***    *** **   ****                 ****     ******** 
   ** **   *       ***  ***  ****    **   **     **  **    ***  *   ***      * **** * ********  
   ** **  *       * ***  **** **** * **   **     **  **     ****   * ***    **  ****     **     
   ** ****       *   ***  **   ****  **   **     **  **      **   *   ***  ****          **     
   ** **  ***   **    *** **    **   **   **     **  **      **  **    ***   ***         **     
   ** **    **  ********  **    **   **   **     **  **      **  ********      ***       **     
   *  **    **  *******   **    **    **  ** *** **  **      **  *******         ***     **     
      *     **  **        **    **     ** *   ****   **      **  **         ****  **     **     
  ****      *** ****    * **    **      ***     ***   ******* ** ****    * * **** *      **     
 *  ****    **   *******  ***   ***      ******* **    *****   ** *******     ****        **    
*    **     *     *****    ***   ***       ***   **                *****                        
*                                                **                                             
 **                                              *                                              
                                                *                                               
                                               *                                                

  __     _____  _               ___      _                     _   ____      _____ _                 
 /_ |   |  __ \| |             |__ \    | |                   | | |___ \    / ____| |                
  | |   | |__) | | __ _ _   _     ) |   | |     ___   __ _  __| |   __) |  | |    | | ___  __ _ _ __ 
  | |   |  ___/| |/ _` | | | |   / /    | |    / _ \ / _` |/ _` |  |__ <   | |    | |/ _ \/ _` | '__|
  | |_  | |    | | (_| | |_| |  / /_ _  | |___| (_) | (_| | (_| |  ___) |  | |____| |  __/ (_| | |   
  |_(_) |_|    |_|\__,_|\__, | |____(_) |______\___/ \__,_|\__,_| |____(_)  \_____|_|\___|\__,_|_|   
                         __/ |                                                                       
                        |___/                                                                        
""")
    option=input(">>>")
    while(option != "1" and option != "2" and option !="3" and option != "4"):
        print("Invalid choice. Ho-hum.")
        option = input(">>>")
    if option == "1":
        playIntro()
    elif option == "2":
        theGame = loadGame()
        #loaded = True
        #return theGame, loaded
    elif option == "3":
        clearScreen()
    elif option == "4":
        print()
    else:
        intro()

'''def main():
    intro()

main()
    '''
