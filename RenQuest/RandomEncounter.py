import random
import os
import Items


def randomEncounter(aList, pInventory):
    encounterList = aList
    inventory = pInventory
    listRange = len(encounterList)
    selection = random.randrange(listRange)
    encounter = encounterList[selection]
    if encounter == "Faire Manager":
        inventory["Attack"] = inventory.get("Attack") + 5
        print('''
        As you are walking along, you see a harried-looking woman on her phone.
        When you approach, you catch a bit of her conversation.
        "The guy playing the knight hurt his leg yesterday during the event, so
        make sure that he's taking it easy so that he doesn't make it worse."
        Maybe this information will come in handy...''')
        input()
    elif encounter == "Water":
        inventory["Hit Points"] = inventory.get("Hit Points") + 5
        print('''
        You came across a tent offering free water! You drink some, and the metallic,
        chlorinated taste of the municipal water supply leaves you feeling refreshed.''')
        input()
    elif encounter == "Money":
        moneyValues= [1, 5, 10]
        dollarAmt = random.choice(moneyValues)
        inventory["Money"] = (inventory.get("Money") + dollarAmt)
        print("You found $" + str(dollarAmt) + " lying on the ground! Neat.")
        input()
    elif encounter == "Raccoon":
        inventory["Charisma"] = inventory.get("Charisma") - 2
        inventory["Attack"] = inventory.get("Attack") + 2
        print('''
        From behind an overflowing trashcan, an enormous, vicious looking raccoon is 
        peering at you. Without warning, it darts out, bites you on the ankle, and
        vanishes amongst the crowd.
        You feel nauseous, and you notice foam forming around your mouth.
        However, you also feel suddenly stronger, angrier, and bitier''')
        input()
    elif encounter == "Uber Nerd":
        print('''
        You are approached by the smell of stale Cheetohs, Red Bull, and poor hygiene.
        The person this odor is attached to is making their way towards you wih intent
        They level a finger at you, and loudly declare, 'I challenge you to an duel of honor!
        You must accept, or be labeled a coward!''')
        response = input("Do you accept, y/n? ")
        if response == "y":
            print('''
            "I accept your challenge!" you respond, as you watch a small crowd gather. Your
            opponent charges forward, only to slip in some mud and fall onto his greasy face.
            Clearly humiliated, he shuffles off without a word.''')
            input()
            inventory["Charisma"] = inventory.get("Charisma") + 2
        elif response == "n":
            print('''
            "I don't have time for this," you mutter, eager to escape the staring eyes of the
            crowd. "Ha!" your greasy antagonizer shouts. "Just as I thought, you're too scared
            of my strength and power." The people in the crowd turn away, clearly disappointed
            at your lack of bravery.''')
            input()
            inventory["Charisma"] = inventory.get("Charisma") - 2

    elif encounter == "Firebreather":
        print('''
        You hear a loud 'Fwoosh!" coming from nearby. Peering through the gathering crowd,
        you see a burst of flame. A troupe of performers, dressed in what looks like the 
        stained remnants of your grandmother's old couch, are performing fire-breathing and
        juggling tricks for the crowd.''')
        input()
    elif encounter == "Faries 1":
        print('''
        "Move!" snarls a middle-aged woman in a cheap fairy costume that still has visible
        clearance labels from Party City. She pushes past you, leading a group of similarly 
        dressed women as she goes. As they pass, you catch a glimpse of one of the
        fairies clutching at a mostly empty, plastic bottle labeled 'McCormick'.''')
        input()
    elif encounter == "Drunk Monk":
        consumable = inventory.get("Consumables")
        print('''
        The crowd disperses rather suddenly. You see a dishevelled-looking gentleman wearing
        a robe, though you can't really tell if it's a costume or just what he was wearing
        when he left his trailer house in the morning. He is very obviously trashed; you can
        smell the alcohol from quite a distance. He looks up, and his gaze locks onto you.
        He stumbles over to you, mutters something unintelligible, and presses a bottle of 
        something into your hand, before stumbling a few more paces and falling flat onto the
        ground, where he stays.''')
        input()
        mysteryDrink = Items.Consumable("mystery drink", 10, 0)
        consumable.append(mysteryDrink)
        inventory["Consumables"] = consumable
    elif encounter == "Fortune":
        print('''
        As you're walking around, minding your own business a frantic looking woman wearing
        layers of silk and satin scarves, one wrapped around her head in the fashion of a turban,
        comes toward you with purpose. You look left, you look right, sadly there is no escape.
        You are forced to hear her empassioned words as she tries to pull you into her fortune
        telling tent...
        ''')
        fortunes = ["I have never seen aura like yours. You are exceptional!", "In your previous life, you were royalty, a movie star, or died in the war.",
                    "I sense a dead person is trying to contact you.", "Love and money are coming your way, but you need me to guide you and tell you what to do and when.",
                    "I saw you in a vision. Buying my magic crystals will help you later in life.", "Someone important to you has the initial 'R.'",
                    "You are surrounded by enemies; I am your only true friend."]
        choice = random.choice(fortunes)
        print(choice)
        print('''
        Luckily for you, there are many more people nearby, ones that look like better marks, I
        mean customers for the fortune teller. You continue on your way wondering if maybe she
        knows something you don't....
        ''')
        input()
    elif encounter == "Bracelet":
        print('''
        While perusing some merchandise of dubious quality, a glint of gold catches your eye.
        You walk over, and see a small bracelet in a clump of grass. Picking it up, you examine
        it. It has a slender chain, with delicate charms dangling from it. A heart, a musical
        note, and a silouette of a dancer glimmer in the sunlight. While meant for a small wrist,
        the bracelet looks well-crafted and expensive. You scan the crowd, trying to see who it
        could belong to. An aristocratically dressed woman is frantically searching through some
        nearby shrubs, with a small, morose little girl at her side. You walk up to them, with
        the bracelet in your outstreched hand. "Is this yours?" you ask. The woman turns around,
        and, upon catching sight of the bracelet, you see relief evident across her face.

        "Oh, yes, we lost that about twenty minutes ago! Where did you find it?" she asks, as you
        hand her the bracelet. "I just happened across it in some grass over there," you say, and
        gesture towards where you found it. The woman is putting the bracelet on the little girl's
        wrist, and her small face is lights up with joy. "Thank you so much!" the woman continues.

        "This bracelet was a gift from her grandmother, and just about all that she has to remember
        her by. Now," she says, turning back towards her daughter, "be sure to thank the brave
        warrior for finding your bracelet."

        "Thanks, brave warrior!" the little girl says, a huge smile on her face.

        "Not a problem!" you say, "It's all in a day's work!"

        With a last thank you and wave, the two head off. You watch them leave, with a warm glow
        from helping them out.
        ''')
        input()
    elif encounter == "Horror":
        print('''
        You're sitting on a bench, watching the crowd idly as you take a quick break. From the
        corner of your eye, you catch a glimpse of a small figure disappearing into the trees.
        Intrigued, you stand up and follow it. Pushing your way between two trees and some 
        undergrowth, you stumble into a dimly lit clearing with a small, solitary figure turned
        away from you. At first glance, it appears to be a little boy in a somewhat dingy,
        colorless Victorian outfit. You feel a vague sense of disquiet as you watch him; you can't 
        put your finget on it, but something about him seems... wrong. His skin seems a bit too
        pale, and his arms and legs are stick thin and jointed oddly. His hair is matted with
        dirt, and sits oddly on his head. He's squatting over the ground, playing with a tatty old 
        stuffed bear.

        As you approach, the little boy turns and looks at you, and your vague trepidation turns
        into outright terror and revulsion. The boy's face is covered with caked-on powder, in
        an attempt to cover up the grey, lesion-covered skin. His eyes are wide, and bloodshot. 
        He stares directly at you, with a look of cold fury that no true child's face could
        possiby convey. He opens his mouth, revealing the black stumps of teeth set in raw red
        gums, and an equally black, slug-like tongue crawling behind them. You expect to hear
        a bone-chilling screech come out, but what you hear instead is a trilling, almost
        birdsong-like sound. His wig falls off of his head, revealing a raw, scabbed, hairless,
        scalp. You hear more sounds coming from further in the trees, and your nerve fails you.
        You bolt, running as fast as you can the way you came. You hear some things crashing
        through the brush behind you, catching up, and you suddenly burst into searing daylight
        and the sounds of the faire. You look behind you, and there's no sound or movement.

        You hurriedly make your way back into the crowd, eager to put some distance between you
        and what you witnessed, followed by the fading sound of birds.
        ''')
        input()
    elif encounter == "Old Man":
        print('''
        While munching on an overfried corn dog, you see a hunched-over figure sitting in the
        shade under a tree. You head over, thinking a rest in the shade sounds like a nice
        reprieve from the brutal sunlight and oppressive heat. You sit next to the hunched
        figure, who turns out to be an elderly gentleman wearing nondescript clothes. He looks
        tired, and his clothes are drenched in sweat. You offer him the drink that came with
        your corndog, which he gratefully accepts with a nod of thanks.

        He drinks half of it in one swig, wipes his mouth, and says, "Thanks, kid, I really
        needed that. I'm way too old to be out here in this heat, but my grandkids love it,
        and I could never say no to them. Speaking of, they're probably wondering where I'm at,
        so I'd best be off."
        
        He stands up, looking much better than he had before, and disappears into the crowd.
        You finish your corndog, get up, and do the same. 
        ''')
        input()
    del encounterList[selection]
    inventory["Hit Points"] = inventory.get("Hit Points") - 1

             

                

                                
