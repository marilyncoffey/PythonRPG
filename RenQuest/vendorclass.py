import Items
import random


class vendor:
    def __init__(self, vendorType, charmChance, stealChance, charmed = False):
        
        self.vendorType = vendorType
        self.charmChance = charmChance
        self.stealChance = stealChance
        self.charmed = charmed

    def __string__(self):
        result = ""
        result += "This vendor sells " + self.vendorType
        result += "This is the vendor's chance to be charmed: " + self.charmChance
        result += "This is the vendor's chance to be stolen from: " + self.stealChance
        return result

    def getCharmed(self, charmed):
        print(self.charmed)

    def sell(self, playerClass, pInventory):
        player = playerClass
        inventory = pInventory
        if self.vendorType == "weapon": 
            if player == "Child":
                print("You stare in awe at the wide assortment of weapons before you, but your eye keeps landing on that perfect, shiny sword that looks just your size...there is a price tag that says $10")
                if self.charmed == True:
                    print("I see that this fine sword fits perfectly in your hands. Since you are so charming, I'll only ask $5.")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        childWeapon = Items.Weapon("Sword", 2,6,5)
                        return childWeapon
                    if buy == "n":
                        print("Deals like this don't last!")
                else:
                    print("I see that this fine sword fits perfectly in your hands. It can be yours for a mere $10")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        childWeapon = Items.Weapon("Sword",2,6,10)
                        return childWeapon
                    if buy == "n":
                        print("Deals like this don't last!")
            elif player == "Adult":
                print("As you down some mead from your drinking horn, you glance quickly at the wares inside the tent. There! It's size and shininess immediately attract your semi-drunken eyes. You know you need that giant foam sword. The price tag says $20.")
                if self.charmed == True:
                    print("Ahh, for such a fighter as you, this two-handed sword would be a fine fit. Your words are as honeyed as your mead, so for a mere $10 and this can be yours.")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        adultWeapon = Items.Weapon("Two-Handed Sword",3,12,10)
                        return adultWeapon
                    if buy == "n":
                        print("Deals like this don't last!")
                else:
                    print("Ahh, for such a fighter as you, this two-handed sword would be a fine fit. It can be yours for $20")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        adultWeapon = Items.Weapon("Two-Handed Sword",3,12,20)
                        return adultWeapon
                    if buy == "n":
                        print("Deals like this don't last!")
            elif player == "Anime Fan":
                print("You came because your friends told you it was a costume friendly event, and you stayed because there's food and alcohol. But wait, what is this? A ridiculously large blade with a barrel attached to the top, and a trigger fixed in the handle! You must have it! The price tag on it says $20")
                if self.charmed == True:
                    print("I honestly don't know why I brought this gunblade, but it seems you can't take your eyes off it. I can appreciate some good anime as much as the next guy, so how about just $10 for it?")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        animeWeapon = Items.Weapon("Gunblade",4,8,10)
                        return animeWeapon
                    if buy == "n":
                        print("Deals like this don't last!")
                else:
                    print("I honestly don't know why I brought this gunblade, but it seems you can't take your eyes off it. It matches your costume quite well, how about $20")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        animeWeapon = Items.Weapon("Gunblade",4,8,20)
                        return animeWeapon
                    if buy == "n":
                        print("Deals like this don't last!")
            elif player == "LARPer":
                print("You live for these events, and the chance to show off your gear. You also never turn down the chance for more gear, and that battle hammer would be a nice addition to your collection, and it says it's only $10.")
                if self.charmed == True:
                    print("You look like you could bash a few heads in with just your bare hands, but this battle hammer would work even better! This can be yours for the discounted price of $5")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        larperWeapon = Items.Weapon("Battle Hammer",5,10,5)
                        return larperWeapon
                    if buy == "n":
                        print("Deals like this don't last!")
                else:
                    print("You look like you could bash a few heads in with just your bare hands, but this battle hammer would work even better! This can be yours for only $10.")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        larperWeapon = Items.Weapon("Battle Hammer",5,10,10)
                        return larperWeapon
                    if buy == "n":
                        print("Deals like this don't last.")
            elif player == "King Arthur":
                print("As a King you must always be prepared, and that means a sword. Approaching the tent, you see a familiar rock on display.")
                if self.charmed == True:
                    print("A fine day to you, my King. I have this special sword over here. Some damp tart chucked it at me from out of a lake as I was walking by")
                    kingWeapon = Items.Weapon("Excalibur", 20, 1000000, 0)
                else:
                    print("A fine day to you, my King. I have this special sword over here. Some damp tart chucked it at me from out of a lake as I was walking by")
                    kingWeapon = Items.Weapon("Excalibur", 20, 1000000, 0)
                return kingWeapon

        if self.vendorType == "armor":
            if player == "Child":
                print("As you step through the flaps, your eyes behold an assortment of protective gear. Most of it looks much too big for you, but then you see a shield that looks just your size! As you grab hold of it, you faintly hear the words 'Hey! Listen!' ringing in your ears... The tag on the shield says it's $10.")
                if self.charmed == True:
                    print("Your knowledge of this shield has made my day! How about you take it for just $5, today. It goes with that green costume really well!")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        childArmor = Items.Armor("Shield", 5 ,5)
                        inventory["Dexterity"] = inventory.get("Dexterity") + childArmor.get_ac()
                        print("You have an incredible urge to start smashing clay pots...")
                        return childArmor
                    if buy == "n":
                        print("Deals like this don't last!")
                else:
                    print("This shield has been used to save many princesses! Or actually, just one... many times. It goes for $10.")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        childArmor = Items.Armor("Shield", 5, 10)
                        inventory["Dexterity"] = inventory.get("Dexterity") + childArmor.get_ac()
                        return childArmor
                    if buy == "n":
                        print("Deals like this don't last!")
            elif player == "Adult":
                print("The breastplate is $30.")
                if self.charmed == True:
                    print("You seem quite the talker. I'll give you this breastplate for $15 if you'll just go away.")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        adultArmor = Items.Armor("Breastplate", 2, 15)
                        inventory["Dexterity"] = inventory.get("Dexterity") + adultArmor.get_ac()
                        return adultArmor
                    if buy == "n":
                        print("Deals like this don't last!")
                else:
                    print("That's a great piece of armor there; it got me through some tough battles. How about $30 and it's yours?")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        adultArmor = Items.Armor("Breastplate", 2, 30)
                        inventory["Dexterity"] = inventory.get("Dexterity") + adultArmor.get_ac()
                        return adultArmor
                    if buy == "n":
                        print("Deals like this don't last!")
            elif player == "Anime Fan":
                print("You're not sure why you are bothering to come here; none of the stuff on display matches your costume. Oh, what's this? You just happen to catch a glimpse of the end of a dangling belt, one of many(almost 100 it seems!), attached to a long coat with an enormous hood. You search frantically for the price tag, there...it says $30.")
                if self.charmed == True:
                    print("You actually want to buy this? I didn't think I'd ever get rid of it. I'll let you have it for just $15")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        animeArmor = Items.Armor("Trenchcoat",1,15)
                        inventory["Dexterity"] = inventory.get("Dexterity") + animeArmor.get_ac()
                        return animeArmor
                    if buy == "n":
                        print("Deals like this don't last!")
                else:
                    print("I didn't actually mean to pack that for today, but now I'm glad I did. It suits you! Let's call it $30")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        animeArmor = Items.Armor("Trenchcoat", 1, 30)
                        inventory["Dexterity"] = inventory.get("Dexterity") + animeArmor.get_ac()
                        return animeArmor
                    if buy == "n":
                        print("Deals like this don't last!")
            elif player == "LARPer":
                print("From across the walkway you are blinded by the shining metal reflecting off of a chainmail shirt. As you look closer, you realize it's actually just soda can tabs strung together. But hey, people don't get that close to you anyway. With a price of $20 on the tag, you might need to add this to your collection.")
                if self.charmed == True:
                    print("This set of chainmail seems it was made just for you. It's a perfect fit! It also matches the rest of your gear. I'll take $10 and it's yours.")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        larperArmor = Items.Armor("Chainmail",3, 10)
                        inventory["Dexterity"] = inventory.get("Dexterity") + larperArmor.get_ac()
                    if buy == "n":
                        print("Deals like this don't last!")
                else:
                    print("Each tab was carefully collected from the leftover cans of long hours at the keyboard, grinding and completing raids with my guild. It's only $20.")
                    buy = input("Would you like to complete this purchase? y/n")
                    if buy == "y":
                        larperArmor = Items.Armor("Chainmail", 3, 20)
                        inventory["Dexterity"] = inventory.get("Dexterity") + larperArmor.get_ac()
                        return larperArmor
                    if buy == "n":
                        print("Deals like this don't last!")
            elif player == "King Arthur":
                print("Even a magnificent king such as yourself needs some fantastic armor. Hold on I have just the thing. The man walks away and comes back with a set of full plate mail.")
                if self.charmed == True:
                    print("A fitting set of plate mail for a fitting king! Hurrah!")
                    kingArmor = Items.Armor("Excalibur", 20, 0)
                else:
                    print("You're used to people fawning over you but this guy seems less than impressed as he tells you the armor will be $100")
                    kingArmor = Items.Armor("Excalibur", 20, 100)
                return kingArmor

        if self.vendorType == "consumable":
            water = Items.Consumable("water", 5, 2)
            mutton = Items.Consumable("mutton", 4, 6)
            mead = Items.Consumable("mead", 3, 4)
            liquor = Items.Consumable("liquor", 4, 5)
            turkey = Items.Consumable("turkey leg", 3, 5)
            shopping = True
            consumable = inventory.get("Consumables")
            while shopping:
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
                elif choice == "2":
                    if player == "Child":
                        print("I don't believe you're old enough to purchase that.")
                    else:
                        consumable.append(mead)
                elif choice == "3":
                    if player == "Child":
                        print("I don't believe you're old enough to purchase that.")
                    else:
                        consumable.append(liquor)
                elif choice == "4":
                    consumable.append(mutton)
                elif choice == "5":
                    consumable.append(turkey)
                elif choice == "6":
                    inventory["Consumables"] = consumable
                    shopping = False
            

    def charm(self, pCHA):
        playerCHA = pCHA
        charmDC = 15
        charmChance = random.randint(1, 20) + playerCHA
        if self.charmed != True:
            if charmChance >= charmDC:
                self.charmed = True
                print("Your charismatic ways and good bargaining skills are incredible.")
                print("You have talked the vendor down on the price by 50%!")
            else:
                print("The vendor tells you that prices are non-negotiable.")

    def steal(self, pDEX, pClass):
        playerDEX = pDEX
        player = pClass
        stealDC = 20
        stealChance = random.randint(1, 20) + playerDEX
        if stealChance >= stealDC:
            if player == "Child":
                weapon = Items.Weapon("Sword", 2,6,0)
            elif player == "Adult":
                weapon = Items.Weapon("Two-Handed Sword",3,12,0)
            elif player == "Anime Fan":
                weapon = Items.Weapon("Gunblade",4,8,0)
            elif player == "LARPer":
                weapon = Items.Weapon("Battle Hammer",5,10,0)
            elif player == "King Arthur":
                weapon = Items.Weapon("Excalibur", 20, 1000000, 0)
            print('''
You have successfully stolen the time, effort, and skill
that was put into this item! I hope it's worth it.
.......you monster.''')
            caught = False
        else:
            print('''
You were caught stealing! They don't take very well to that here.
You have forever lost the love of your family and friends,
and also you get kicked out of the faire.''')
            weapon = None
            caught = True
        return weapon, caught

    def printMenu(self):
        '''if self.vendorType == "weapon":
        elif self.vendorType == "armor":
            print("Welcome to Amanda's Armory! We have all kinds of sizes and types of armor, I'm sure we have just what you're looking for.")'''
        choice = input('''
╔═════════════════════════════════╗
║What would you like to do?       ║
╠═════════════════════════════════╣
║1 - Buy Item                     ║
║2 - Attempt to charm the vendor  ║
║3 - Attempt to steal the item    ║
║4 - leave this area              ║
╚═════════════════════════════════╝
''')
        return choice         
        
        

    def theTrickster(self, player, pInventory):
        inventory = pInventory
        thePlayer = player
        necklace = Items.Armor("Amulet", 5, 0)
        print("The tent looks dark from the outside, but not one to be easily scared you step through. Inside it looks like a magical faerie forest. On a log to the right you see a creature with the legs of a goat and body of a human. It's curled horns sit atop it's head right next to it's fawn-like ears.")
        choice = input("Do you approach? y/n: ")
        if choice == "n":
            print("well, that was just too much, you back right out of there.")
        elif choice == "y":
            print('''
.. ........... .............  ........... . ..... ........ .......
         .          ..       %                .    .   %      .    .
 .@@@        . @@     @@@@  .          .            .       *     . 
     @@   .   @      @             .       .     .      .  ***  .  .
   .  \\@\\   .@ .    @          .              .     #     *****     
  @@@   @@@@@  @@@@@@___ .   .       .%      .    {###}  *******
 .   @-@  @  .@.    .@@@\\  .    %       .       <## ####>********
   @@@@\\   @ @     .   \\@@@@         .       .    {###}***********
   . %  @  @@ /@@@@@ .         .       .      <###########> *******
         @-@@@@    V    .  ,~,      %     .     {#######}******* ***
           @@      v       )))======        <###############>*******
     .     @@             .-``-' /             {## ######}***** ****
   %      @@     %        (\\  /\\/         <###################> ****
          @@               |#(               {#############}********
          @@              /###)         <################  #####>***
          @@@            /#  \\|`._#        {##################}*****
           @@@           \\)  |)       <##########################>**
  @@@@     @@@           |`  |`          {###   ##############}*****
 @@@@@@@  @@@@@    / /@@ W   W      <##############################>
 @@@@@@@ @@@@@@@ @@@@@@@@@@@@@@@@@@@ ..... @@@@@@  @@@@@@@  @@@@
 @@@@@@###@@@@@### @@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@###@##@@ @@@@@@@@@@@@@@@@@@@@@ @@@@@   @@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@### @@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@
 -@@@@@@@@@#####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
''')
            print("The fawn-like creature looks up at you and smiles. \"My name is Puck, do you like riddles? If you can answer correctly I have a prize for you! If you answer incorrectly, well, we'll see what happens.")
            riddles = ["candle", "shadow", "wind"]
            pick = random.choice(riddles)
            if pick == "candle":
                riddle1 = input('''
╔══════════════════════════════════════════════════════════════╗
║What is the sister of the sun, though made for the night?     ║
║The fire causes her tears to fall, and when she is near dying ║
║they cut off her head.                                        ║
╠══════════════════════════════════════════════════════════════╣
║1 - Moon                                                      ║
║2 - Mirror                                                    ║
║3 - Candle                                                    ║
║4 - Telescope                                                 ║
╚══════════════════════════════════════════════════════════════╝
''')
                if riddle1 == "1":
                    print("that is incorrect")
                if riddle1 == "2":
                    print("not even close")
                if riddle1 == "3":
                    print("wow! you're a genious. have a cool necklace that makes you healthier!")
                    inventory["Accessory"] = necklace
                    #player.setHP()  = player.getHP() + 5
                    inventory["Hit Points"] = inventory.get("Hit Points") +5
                if riddle1 == "4":
                    print("I don't even know what that is...are you even trying?")
                input("Press any key to continue")
            elif pick == "shadow":
                riddle2 = input('''
╔══════════════════════════════════════════════════════════════╗
║I have one and you have one. So do the woods, fields, streams ║
║and seas, fish, beasts and crops and everything else in this  ║
║revolving world.                                              ║
╠══════════════════════════════════════════════════════════════╣
║1 - Sleep                                                     ║
║2 - Hunger                                                    ║
║3 - Soul                                                      ║
║4 - Shadow                                                    ║
╚══════════════════════════════════════════════════════════════╝
''')
                if riddle2 == "1":
                    print("the stream never sleeps")
                if riddle2 == "2":
                    print("I could go for some mutton....")
                if riddle2 == "3":
                    print("I certainly doubt that")
                if riddle2 == "4":
                    print("why yes!")
                    inventory["Accessory"] = necklace
                    #player.setHP()  = player.getHP() + 5
                    inventory["Hit Points"] = inventory.get("Hit Points") +5
                input("Press any key to continue")
            elif pick == "wind":
                riddle3 = input('''
╔══════════════════════════════════════════════════════════════╗
║Tell me, what is it that fills the sky and the whole earth    ║
║and tears up new shoots, and shakes all foundations, but      ║
║cannot be seen by eyes or touched by hands?                   ║
╠══════════════════════════════════════════════════════════════╣
║1 - Trees                                                     ║
║2 - Lightning                                                 ║
║3 - Fire                                                      ║
║4 - Wind                                                      ║
╚══════════════════════════════════════════════════════════════╝
''')
                if riddle3 == "1":
                    print("whoever heard of an invisible tree?")
                if riddle3 == "2":
                    print("that's just silly")
                if riddle3 == "3":
                    print("are you even trying?")
                if riddle3 == "4":
                    print("I can't trick you!")
                    inventory["Accessory"] = necklace
                    #player.setHP()  = player.getHP() + 5
                    inventory["Hit Points"] = inventory.get("Hit Points") +5
                input("Press any key to continue")
                    
        


        
            

            
        
    

