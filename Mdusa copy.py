######################
### RANDOM GAME ###
######################

################
### IMPORTS ###
################
import os, time, random


######################
### PLAYER VALUES###
######################

def changestartvals():
    for change in range(1, 15):
        change1val = random.randint(1,4)
        change2val = random.randint(1,4)
        while change2val == change1val:
            change2val = random.randint(1, 4)
        Vals[change1val-1] += 1
        Vals[change2val-1] -= 1
    for prevals in range(0,len(Vals)):
        if Vals[prevals] < 5 or Vals[prevals] > 20:
            changestartvals()
            break

## Names ##
# Male Names#
FnamesM = "Jamie".split(" ")

# Female Names #
FnamesF = "Eleanor".split(" ")

# Last Names
Lnames = "Liz".split(" ")

gender = random.choice(list("MF"))
if gender == "M":
    firstname = random.choice(FnamesM)
    lastname = random.choice(Lnames)
else:
    firstname = random.choice(FnamesF)
    lastname = random.choice(Lnames)
name = firstname + " " + lastname
Vals = [16, 16, 16, 16]
changestartvals()   

Life = Vals[0]
Wis = Vals[1]
Str = Vals[2]
Dex = Vals[3]


HP = int((Life - Life%3)/3)
MaxHP = int((Life - Life%3)/3)
MaxSP = int((Wis - Wis%3)/3)
SP = int((Wis - Wis%3)/3)

##################
### VARIABLES ###
##################

# Origins   
O1 = "In a land far away, there was an explorer named Arthur. Arthur had always been fascinated by tales of adventure, and he was determined to have his own adventures one day. When he was old enough, Arthur set out on his first expedition. He traveled for many miles, encountering all sorts of danger along the way. But eventually he made it to his destination: a lost city that nobody had ever found before! It was a great achievement, and Arthur continued to explore more lands in the years that followed. Hence, he was your role model and you aspire to be a great adventurer just like him."
O2 = """Last year, a man known as Erik the Red discovered Greenland and decided to settle there. Erik was a brave and bold explorer, and he [False]uickly became famous for his exploits. However, one day he vanished while on an expedition to explore new lands. His ship was found abandoned off the coast of Greenland, but no trace of Erik or any of his crew was found. You want to be an adventurer to find him and bring him back to the world of the living."""
Origins = [O1, O2]

# Scenes

availscenes = [2, 3, 4, 5, 6, 7, 8, 9, 14, 15, 16, 17, 18]
### DICT ###
# Scene no. : [story, only enter, choice1, choice2, choice1 past, choice2 past, choice1fail past, choice2fail past, choice1r, choice2r, scenenext1, scenenext2, make availscene1, make availscene2]

scenes = {
    2: ["While walking you come across an old tent and a camp. Should you rest?", False,"Yes", "No", ["H+1", "You wake up the next day feeling refreshed and rejuvenated\nHP + 1"], ["H-1", "You continue walking, but tired, you trip over a rock and fall on your face. Ouch!\nHP - 1"], [False], [False], [False], [False], [False], [False]],
    3: ["While walking through the eternal desert you come across a goblin. Seeing you, it immediately turns to you and charges!", False, "Brace for impact", "RUN!!!!", ["", "You grab the Goblin as it runs at you and throws it to the side.  Defeated, it slunks away from you"], ["", "You immediately turn tail and run. Due to your incredible speed, the Goblin [False]uickly falls behind."], ["H-1", "The Goblin slams into you and drives you into a large rock. You get up to fight, with your back aching. HP-1"], ["H-1", "The Goblin catches up to you swiftly and drives you into a large rock. You get up to fight, with your back aching. HP-1"], [True, Str, 30], [True, Dex, 60], [False], [False], [True, "Goblin", [0.75, 1]], [True, "Goblin", [0.75, 1]], [False], [False]],
    4: ["Walking through a forest, you encounter a tran[False]uil river with clear water.", True, "", "", ["S+1", "The sounds of the river gives you a peaceful feeling. Sanity + 1, Wis + 1"],["W+1", ""],[False],[False],[False],[False],[False],[False],[False], [False], [False]],
    5: ["While walking through a forest, you encounter a luminescent butterfly flying around you, as if trying to lead you somewhere.", False, "Follow it", "Don't follow it", ["L+1", "The butterfly leads you to a magically clean pond from which you drink. Life + 1"],["[False]", "You continue with your travels"], [False], [False], [False], [False], [False], [False], [False]],
    6: ["While walking through a forest, you encounter a luminescent butterfly flying around you, as if trying to lead you somewhere.", False, "Follow it", "Don't follow it", ["H-1", "You trip over a tree root while trying to follow it. HP - 1"],["", "You continue with your travels"], [False], [False], [False], [False], [False], [False], [False]],
    7: ["A frost giant blocks your way through the mountain pass", False, "ATTACK!", "Sneak past it", ["", "You charge the frost giant! Not expecting you, you have the upper hand."], ["", "You successfully sneak past the frost giant! "], ["", ""], ["H-1", "The frost giant spots you, grabs you by the ankle and throws you to the floor. HP-1"], [False], [True, Dex, 70], [True, "Frost Giant", [1.25, 1]], [True, "Frost Giant", [1.25, 1]], [False], [True, "Frost Giant", [0.75, 1]], [False]],
    8: ["While walking through an elven town, you spot a shrine in the middle of it. A local tells you, 'it is the shrine to Shak al Shabud, the all mother.' You walk up to it.", [False], "Destroy it", "Steal some of the offerings", ["St+1", "You destroy the shrine and feel it's magic flow into you. Then you hurry away from the town."], ["D+1", "You [False]uickly take some of the food and leave. After consuming the food you stole, you feel faster."], ["", "You hurry away from the town in embarrassment as you were unable to break it."], ["", "You try to steal some loot, but there was no opening to do so"], [True, Str, 30], [True, Dex, 30], [False], [False], [False], [False], [False]],
    9: ["While walking through a path in the woods, you find an overturned cart. next to it were human footprints and monster footprints.", False, "Track the Monster", "Track the human", ["", "You track the Monster's footprints, but it suddenly disappears."], ["", "You track the human footprints to see a woman, chained to a rock."], [False], [False], [False], [False], [False], [False], [False], [False], [False], [True, 10, True, 10]],
    10: ["A woman was chained to the rock. When you ask her what happened she simply said, she was arrested for hunting in the territory of Ogres, and was charged with Espionage. She also said that her guards left to find the nearest human town, and were going to be back", False, "Release her", "Let her be and wait for the guards to come back", ["", "You quickly untie her. Follow me! She said, and quickly disappeared. You chase after her"], ["", "You leave her and continue with your travels"], [False], [False], [False], [False], [False], [False], [False], [False], [True, 12, True, 12], [True, 11]],
    11: ["While walking through a town you see the woman who you spotted before in the town centre. She was about to be hung", False, "Save her", "Let her be", ["", "You jump onto the gallows and draw a knife across the ropes binding her. The guards immediately start to attack."], ["", "Leia. Espionage. Someone announced as the executioner tied the rope around her neck and removed the stool she was on. She died quick."], ["", "You jump onto the platform, but it was too late. She -- Leia was already dead."], [False], [True, Dex, 20], [False], [True, "Guards", [1.25, 0.8]], [True, "Guards", [1.1, 1]], [True, 12, True, 12], [True], [True], [True]],
    12: ["You follow the woman, who introduced herself as Leia, back to her house. Or - what remained of it. Above the house sat a Drake, a Dragon-like animal that couldn't fly. You took out your sword and prepared to fight", False, "Fight", "Hang back", ["", "You charge the Drake"], ["", "The Drake charges you"], ["", ""], ["", ""], [False], [False], [True, "Drake", [1.5, 1.25]], [True, "Drake", [0.8, 1]], [True, 13, True, 13], [True, 13, True, 13]],
    13: ["Filler", True, "", "", ["H+1", "Congrats"], ["S+1", ""], ["", ""], ["", ""], [False], [False], [False], [False], [False], [False], [False], [False]],
    14: ["While walking through a dark cave, you hear strange noises coming from deep within the cave.", False, "Investigate the noises", "Turn back", ["", "You venture deeper into the cave and find a hidden treasure trove filled with gold and gems!"], ["", "You decide to turn back, not wanting to risk your safety."], [False], [False], [False], [False], [False], [False], [False], [False], [False], [True, 50, True, 50]],
    15: ["You come across a village being attacked by a group of orcs.", False, "Join the fight", "Stay out of it", ["", "You grab your weapon and join the fight, helping the village defeat the orcs and protect their people."], ["", "You decide to stay out of the fight, not wanting to get involved in a dangerous situation."], [False], [False], [False], [False], [False], [False], [False], [False], [True, Str, 50], [True, "Orc", [1.25, 1]]],
    16: ["While walking through a dense jungle, you come across a ancient temple.", False, "Explore the temple", "Bypass it", ["", "You explore the temple and find a hidden room filled with mysterious artifacts."], ["", "You bypass the temple, not wanting to risk getting lost in its maze-like interior."], [False], [False], [False], [False], [False], [False], [False], [False], [False], [False], [True, Dex, 30]],
    17: ["You find yourself in a sea of sand dunes, with no sign of water in sight.", False, "Climb the dunes", "Stay at the base", ["H-1", "You climb the dunes and spot an oasis in the distance, but by the time you reach it, you are exhausted and dehydrated. HP -1"], ["", "You stay at the base of the dunes, conserving your energy and waiting for a sign of water."], [False], [False], [False], [False], [False], [False], [False], [False], [False], [False], [True, Wis, 20]],
    18: ["You come across a group of travelers being ambushed by bandits.", False, "Help the travelers", "Stay out of it", ["", "You grab your weapon and help the travelers defeat the bandits and protect their goods."], ["", "You decide to stay out of the fight, not wanting to risk your safety."], [False], [False], [False], [False], [False], [False], [False], [False], [True, Str, 40], [True, "Bandit", [1.25, 1]], [True, 20, True, 20]],
    }

##################
### FUNCTIONS ###
##################

def drawheader(p2, ms, pHP, eHP, eATK):
    enemyatk = eATK
    differenceinplayerletter = len(p2)-len("Player")
    print("\n\n\n\n\n\n\n\n\n\n")
    if differenceinplayerletter >= 0:
        print(f"Player: {' '*differenceinplayerletter}{'█'*pHP}")
        print(f"{p2}: {'█'*eHP}")
    else:
        print(f"Player: {'█'*playerhealth}")
        print(f"{p2}: {' '*differenceinplayerletter}{'█'*eHP}")
    print("\n")
    if ms[0] != 1:
        print(f"Player atk: {int((Dex + Str*2) * 0.5 * ms[0])} ({((Dex + Str) * 0.5 * ms[0])-(Dex+Str)*0.5})")
    else:
        print(f"Player atk: {int((Dex + Str*2) * 0.5)}")
    if ms[1] != 1:
        print(f"Enemy atk: {int((enemyatk) * 0.5 * ms[1])} ({(enemyatk * 0.5 * ms[1])-enemyatk})")
    else:
        print(f"Enemy atk: {int(enemyatk * 0.5)}")
    

def callatk(who, atk):
    print(f"{who} attacked for {atk} damage!")
    
def fight(enemy, modifiers):
    global HP, SP, Life, Wis, Dex, Str
    enemyatk = int(random.randint(int((Dex+Str*2)*0.5), int(Dex+Str*2)) * modifiers[1])
    playeratk = (int((Dex + Str*2) * 0.5 * modifiers[0]))
    pHP = 100
    eHP = 100
    pSP = int(Dex/3)
    eSP = int((random.randint(int(Dex*0.5), int(Dex * 1.5)))/2)
    dispvals()
    drawheader(enemy, modifiers, pHP, eHP, enemyatk)
    input("Press enter to start fight")
    timeslept = 0
    while pHP > 0 or eHP > 0:
        time.sleep(0.5)
        timeslept += 1
        if timeslept % pSP == 0:
            eHP -= playeratk
            drawheader(enemy, modifiers, pHP, eHP, enemyatk)
            callatk("You", playeratk)            
        elif timeslept % eSP == 0:
            pHP -= enemyatk
            drawheader(enemy, modifiers, pHP, eHP, enemyatk)
            callatk(enemy, enemyatk)
        if pHP <= 0:
            break
        elif eHP <= 0:
            break
    if pHP <= 0:
        print(f"You lost to the {enemy}. It leaves you on the floor HP - 1")
        HP -= 1
        if HP == 0:
            end(1)
            return
    elif eHP <= 0:
        increasedval = random.randint(1, 4)
        if increasedval == 1:
            Str += 1
            dispvals()
            print(f"You sent the {enemy} back to where it belonged - in the underworld. STR + 1")
        elif increasedval == 2:
            Dex += 1
            dispvals()
            print(f"You sent the {enemy} back to where it belonged - in the underworld. DEX + 1")
        elif increasedval == 3:
            Life += 1
            dispvals()
            print(f"You sent the {enemy} back to where it belonged - in the underworld. Life + 1")
        else:
            Wis += 1
            dispvals()
            print(f"You sent the {enemy} back to where it belonged - in the underworld. Wis + 1")
            
            
def end(end):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    if end == 1:
        print("You died after you lost all your health. You were found by adventurers and was diggen a shallow grave")
        return
    elif end == 2:
        print("You went insane and died of thrist after wandering around for days. Your body was never recovered")
        return

def successfulscene(s, scene):
    global HP, SP, Life, Wis, Dex, Str
    scenelib = scenes[scene]
    if scenelib[s][0] == "H+1":
        if HP < MaxHP:
            HP += 1
        else:
            pass
    elif scenelib[s][0] == "H-1":
        HP -=1
        if HP == 0:
            end(1)
            return
    elif scenelib[s][0] == "S+1":
        if SP < MaxSP:
            SP += 1  
        else:
            pass
    elif scenelib[s][0] == "S-1":
        SP -= 1
        if SP == 0:
            end(2)
            return
    elif scenelib[s][0] == "L+1":
        Life += 1
    elif scenelib[s][0] == "L-1":
        Life -= 1
    elif scenelib[s][0] == "W+1":
        Wis += 1
    elif scenelib[s][0] == "W-1":
        Wis -= 1
    elif scenelib[s][0] == "St+1":
        Str += 1
    elif scenelib[s][0] == "St-1":
        Str -= 1
    elif scenelib[s][0] == "D+1":
        Dex += 1
    elif scenelib[s][0] == "D-1":
        Dex -= 1
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    dispvals()
    print("\n")
    print("\n\n")
    print(scenelib[s][1])

def scene(scene):
    global HP, SP, Life, Wis, Dex, Str, availscene
    scenelib = scenes[scene]
    print(scenelib[0])
    choice = 0
    if scenelib[1]:
        input("Press enter to continue")
        successfulscene(4, scene)
        successfulscene(5, scene)
    else:
        if scenelib[8][0]:
            print(f"Option 1: {scenelib[2]} Chance of success: {scenelib[8][1]/scenelib[8][2]*100}%")
        else:
            print(f"Option 1: {scenelib[2]}")
        if scenelib[9][0]:
            print(f"Option 2: {scenelib[3]} Chance of success: {scenelib[9][1]/scenelib[9][2]*100}%")
        else:
            print(f"Option 2: {scenelib[3]}")
        print("\n\n")
        
        while choice != 1 and choice != 2:
            choice = int(input("For Option 1, press 1, for 2, press 2. Then, press enter. : "))
        if choice == 1 and scenelib[8][0]: # Option 1, there is a requirement
            diceroll = random.randint(1, scenelib[8][2])
            if diceroll <= scenelib[8][1]:
                successfulscene(4, scene)
                if scenelib[-6][0]:
                    input("Press enter to continue")
                    fight(scenelib[-6][1], scenelib[-6][2])
            else:
                successfulscene(6, scene)
                if scenelib[-4][0]:
                    input("Press enter to continue")
                    fight(scenelib[-4][1], scenelib[-4][2])
        elif choice == 1 and scenelib[8][0] != True: # Option 1
            successfulscene(4, scene)
            if scenelib[-6][0]:
                    input("Press enter to continue")
                    fight(scenelib[-6][1], scenelib[-6][2])
        elif choice == 2 and scenelib[9][0]: # Option 2, there is a requirement
            diceroll = random.randint(1, scenelib[9][2])
            if diceroll <= scenelib[9][1]:
                successfulscene(5, scene)
                if scenelib[-5][0]:
                    input("Press enter to continue")
                    fight(scenelib[-5][1], scenelib[-5][2])
            else:
                successfulscene(7, scene)
                if scenelib[-3][0]:
                    input("Press enter to continue")
                    fight(scenelib[-3][1], scenelib[-3][2])
        else: # Option 2
            successfulscene(5, scene)
            if scenelib[-5][0]:
                    input("Press enter to continue")
                    fight(scenelib[-5][1], scenelib[-5][2])
    if choice == 2 and scenelib[-1][0]:
        if scene in availscenes:
            availscenes.pop(availscenes.index(scene))
        if len(scenelib[-1]) > 3:
            if scenelib[-1][2]:
                newpart(scenelib[-1][3])
            else:
                availscenes.append(scenelib[-1][1])
    if choice == 1 and scenelib[-2][0]:
        if scene in availscenes:
            availscenes.pop(availscenes.index(scene))
        if len(scenelib[-2]) > 3:
            if scenelib[-2][2]:
                newpart(scenelib[-2][3])
            else:
                availscenes.append(scenelib[-2][1])
    input("Press enter to continue")
    newpart(random.choice(availscenes))
    
# DISPLAY PLAYER VALS #

def dispvals():
    global MaxHP, MaxSP
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(f"{name}  ({gender})")
    MaxHP = int((Life - Life%3)/3)
    MaxSP = int((Wis - Wis%3)/3)
    print(f"Health: {'●' * HP}{'◌' * (MaxHP-HP)}{' '*(10-HP)}Life: {Life}\nSanity: {'●'*SP}{'◌' * (MaxSP-SP)}{' '*(10-SP)}Wisdom: {Wis}\nStrength: {Str}\nDexterity: {Dex}")
    print("\n")

def newpart(s):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    dispvals()
    print("\n")
    if s == 1:
        origin()
        print("\n")
        print("If you Health or Sanity goes to 0, you lose. 3 Life points increases Max health by 1, and 3 Wisdom points increases Max Sanity by 1. Strength and Dexterity \naffects the outcome of certain choices. The higher your Dexterity, the faster you attack in a fight. These two stats also directly affects the damage you deal in a \nfight. \n")
        input("Press enter to continue")
        newpart(random.choice(availscenes))
    else:
        scene(s)
    
    
# ORIGIN #

def origin():
    print(random.choice(Origins), end = "\n")
  

#####################
### INITIALIZATION ###
#####################

newpart(1)
print("\n\n")



