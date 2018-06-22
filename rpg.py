#the new and  improved version
#escape from the future
#project game
print("Welcome to Escape from the Future. This is the coding project of Huamin, Ria M, Ria S, and Aishani.")
print("It is the year 2025.")
print("You are a physicist.")
print("You have been experimenting with a particle accelerator, but you miscalculate which in turn causes an error.")
print("As a result of this, you are transported to an alternate reality of your earth.")

#start choice
start = raw_input("Are you up for the challenge? Yes or No  ")
if start == "No":
    print("Over the years you grow more and more isolated and lose sight of what is your reality. FAILED MISSION.")
else:    
#world choice
    #Particle Physics = experiment that caused you to be sent to the regular earth
    #Holographic Universe Theory = experiment that caused you to be sent to the dragon earth
    earth_choice = raw_input("Choose what you were experimenting before the accident: Particle Physics or Holographic Universe Theory: ")

#dragon earth
    from random import randint
import sys
if earth_choice == "Holographic Universe Theory":
    welcome1 = ("Welcome to Earth 72 otherwise known as the Draconic Earth.")
    name1 = raw_input("Please enter your Character's Name.")
    welcome1 = ("Welcome to the Dragonbound Gates, %s. Good luck on your mission.")
    characterhealth = 50
    characterenergy = 50
    healthstatement = ("You have %s Health.")
    energystatement = ("Your energy level is at %s.")
    print(healthstatement %(characterhealth))
    print(energystatement %(characterenergy))
    print(welcome1 %(name1))
    print("These gates lead to the world of the dragons. As you gaze beyond the towering gates, thick fog obscures whatever else this world may hold.")
    print("You look around the room you were put in. As you observe the intricate carvings that line the marble columns that reach towards the sky.")
    print("Looking out, a small shadow soon crosses your path. It's Kourovy Drak, the dragon of the smoke.")
    print("The small serpent slithers across the floor, gliding across the smooth surface as it tilts it's head to you, questioning.")
    print("The dragon opens it's mouth to speak, mist hissing out of it's pitless eyes.")
    smokespeech = ("'%s, dear friend. I see you're trying to escape... Perhaps you could do me a favor and I will swear myself to you...?'")
    print(smokespeech %(name1))
    print("As you look beyond Kourovy Drak, you see two newly foermed tunnels. Both are dark.")
    print("Drak follows your gaze, and flicks it's tail. The second cavern is blocked by large stones, and the dragon looks at you again.")
    choice1 = raw_input("Do you choose to: Take Corridor 1, or Talk to Kourovy Drak?")
    if choice1 == "Take Corridor 1":
        print("You run down the dark corridor on the left. Not long after you've taken this corridor, you hear a strange sound.")
        choice11 = raw_input("Do you choose to: Investigate, or Keep Going?")
        if choice11 == "Investigate":
            print("As you head towards the strange sound, a small shadow shoots out from behind you. It's a drake!")
        fight1 = raw_input("Do you choose to: Stay and Fight, or Back Off?")
        if fight1 == "Back Off":
            print("You travel down the long tunnel until you emerge into a new tunnel.")
            rightleft = raw_input("There are two branches: Right or Left?")
        if rightleft == "Right":
            print("You run down the tunnel, and it soon gets more and more slippery, as the water soon turns into slime.")
            print("You soon loose your footing, and slide at an uncontrollable pace towards the bottom.")
            slidetohell = randint(1, 3)
        if (slidetohell == 1):
            computer = "You reach out your hand to stop your fall, and you hand catches on a needle. Take 5 damage."
            characterhealth = characterhealth - 5
            print(computer)
            print("Unfortunately, you are too far down the slide to climb back up. Game over.")
            sys.exit("Game over.")
        elif (slidetohell == 2): 
            computer = "You are unable to catch yourself, and crash at the end. Game over."
            print("You are unable to catch yourself, and crash at the end. Game over.")
            sys.exit("You are unable to catch yourself, and crash at the end. Game over.");
        elif (slidetohell == 3):
            computer = "You manage to stop yourself, but the slime covers your head. Game over."
            sys.exit("Game over.")
            print(computer)
        elif fight1 == "Stay and Fight":
            Drakehealth = 10
            assasinhealth = 30
            while (characterhealth > 0 and Drakehealth > 0):
                currenthealth = ("%s has %s Health.")
                currentenergy = ("%s has %s Energy.")
                drakecurrent = ("Drake has %s Health.")
                print(currenthealth %(name1,characterhealth))
                print(currentenergy %(name1, characterenergy))
                print(drakecurrent %(Drakehealth))
                RNGesusbless = randint(1, 6)
                if (RNGesusbless == 1):
                    computer = "Attack"
                elif (RNGesusbless == 2):
                    computer = "Defend"
                elif (RNGesusbless == 3):
                    computer = "Dodge"
                elif (RNGesusbless == 4):
                    computer = "Stay Put"
                elif (RNGesusbless == 5):
                    computer = "Stay Put"
                elif (RNGesusbless == 6):
                    computer = "Stay Put"
                userchoice = raw_input("What would you like to do: Attack, Defend, Dodge, or Stay Put?")
                if computer == userchoice:
                    print("Neither the Drake nor you can land an attack.")
                elif computer == "Attack" and userchoice == "Defend":
                    print("The Drake tries to attack, but you expertly defend yourself.")
                elif computer == "Attack" and userchoice == "Stay Put":
                    print("The Drake attacks, and does 1 damage.")
                    characterhealth = characterhealth - 1 
                    characterenergy = characterenergy + 1
                elif computer == "Attack" and userchoice == "Dodge":
                    print("The Drake comes at you, but you are faster. You leap out of harms way just in time.")
                    characterenergy = characterenergy - 1
                elif computer == "Defend" and userchoice == "Dodge":
                    print("Neither you nor the Drake attack, instead both choosing to defend.")
                    characterenergy = characterenergy - 1
                elif computer == "Defend" and userchoice == "Attack":
                    print("You try and attack the Drake, but you cannot get through to land a blow.")
                    characterenergy = characterenergy - 1
                elif computer == "Defend" and userchoice == "Stay Put":
                    print("You don't do anything, and the Drake defends, expecting an attack.")
                    characterenergy = characterenergy + 1
                elif computer == "Dodge" and userchoice == "Defend":
                    print("You defend yourself, and the Drake dodges, expecting an attack.")
                elif computer == "Dodge" and userchoice == "Attack":
                    print("You try to attack the Drake, but the Drake dodges your incoming attack.")
                    characterenergy = characterenergy - 1
                elif computer == "Dodge" and userchoice == "Stay Put":
                    print("You stay where you are, and the Drake dodges, thinking that you will attack.")
                    characterenergy = characterenergy + 1
                elif computer == "Stay Put" and userchoice == "Attack":
                    print("The Drake makes no move as you attack. Drake takes 2 Damage.")
                    Drakehealth = Drakehealth - 2
                    characterenergy = characterenergy - 1
                elif computer == "Stay Put" and userchoice == "Dodge":
                    print("The Drake makes no move and you dodge, expecting an attack.")
                    characterenergy = characterenergy - 1
                elif computer == "Stay Put" and userchoice == "Defend":
                    print("The Drake does nothing as you defend, expecting an attack.")
                if (characterhealth > 0 & Drakehealth <= 0):
                    print("You defeat the Drake, and move on.")
                    randomevents = randint(1,3)
                    print(randomevents)
                    if (randomevents == 1):
                        print("As you move further down the ominous tunnel, a howl stops you in your track.")
                    elif (randomevents == 2):
                        print("An assassin jumps from behind a wall that you did not realize was there.")
                        fight3 = raw_input("Do you wish to: Turn Around, or Stand and Fight?")
                        if fight3 == "Stay and Fight":
                            print("The assasin draws his blades.")
                        while (characterhealth > 0 and assasinhealth> 0):
                            currenthealth = ("%s has %s Health.")
                            currentenergy = ("%s has %s Energy.")
                            assasincurrent = ("Assasin has %s Health.")
                            print(currenthealth %(name1,characterhealth))
                            print(currentenergy %(name1, characterenergy))
                            print(assasincurrent %(assasinhealth))
                            RNGesusbless = randint(1, 6)
                            if (RNGesusbless == 1):
                                   computer = "Attack"
                            elif (RNGesusbless == 2):
                                   computer = "Defend"
                            elif (RNGesusbless == 3):
                                   computer = "Dodge"
                            elif (RNGesusbless == 4):
                                   computer = "Stay Put"
                            elif (RNGesusbless == 5):
                                   computer = "Stay Put"
                            elif (RNGesusbless == 6):
                                   computer = "Stay Put"
                           
                            userchoice2 = raw_input("What would you like to do: Attack, Defend, Dodge, or Stay Put?")
                            if computer == userchoice2:
                                print("Neither the Assasin nor you can land an attack.")
                            elif computer == "Attack" and userchoice2 == "Defend":
                                print("The Assasin tries to attack, but you expertly defend yourself.")
                            elif computer == "Attack" and userchoice2 == "Stay Put":
                                print("The Assasin attacks, and does 1 damage.")
                                characterhealth = characterhealth - 1 
                                characterenergy = characterenergy + 1
                            elif computer == "Attack" and userchoice2 == "Dodge":
                                print("The Assasin comes at you, but you are faster. You leap out of harms way just in time.")
                                characterenergy = characterenergy - 1
                            elif computer == "Defend" and userchoice2 == "Dodge":
                                print("Neither you nor the Assasin attack, instead both choosing to defend.")
                                characterenergy = characterenergy - 1
                            elif computer == "Defend" and userchoice2 == "Attack":
                                print("You try and attack the Assasin, but you cannot get through to land a blow.")
                                characterenergy = characterenergy - 1
                            elif computer == "Defend" and userchoice2 == "Stay Put":
                                print("You don't do anything, and the Assasin defends, expecting an attack.")
                                characterenergy = characterenergy + 1
                            elif computer == "Dodge" and userchoice2 == "Defend":
                                print("You defend yourself, and the Assasin dodges, expecting an attack.")
                            elif computer == "Dodge" and userchoice2 == "Attack":
                                print("You try to attack the Assasin, but the Assasin dodges your incoming attack.")
                                characterenergy = characterenergy - 1
                            elif computer == "Dodge" and userchoice2 == "Stay Put":
                                print("You stay where you are, and the Assasin dodges, thinking that you will attack.")
                                characterenergy = characterenergy + 1
                            elif computer == "Stay Put" and userchoice2 == "Attack":
                                print("The Assasin makes no move as you attack. Assasin takes 2 Damage.")
                                assasinhealth = assasinhealth - 2
                                characterenergy = characterenergy - 1
                            elif computer == "Stay Put" and userchoice2 == "Dodge":
                                print("The Assasin makes no move and you dodge, expecting an attack.")
                                characterenergy = characterenergy - 1
                            elif computer == "Stay Put" and userchoice2 == "Defend":
                                print("The Assasin does nothing as you defend, expecting an attack.")
                        print("You defeat the Assasin, and move on.")
                        print("As you're running along the path, a light at the end grows brighter and brighter. You emerge from your world. Mission Successful.")
                    elif (randomevents == 3):
                        print("You travel down the long tunnel until you emerge into a new tunnel.")
                        rightleft = raw_input("There are two branches: Right or Left?")
                        if rightleft == "Right":
                            print("You run down the tunnel, and it soon gets more and more slippery, as the water soon turns into slime.")
                            print("You soon loose your footing, and slide at an uncontrollable pace towards the bottom.")
                            slidetohell = randint(1, 3)
                            if (slidetohell == 1):
                                computer = "You reach out your hand to stop your fall, and you hand catches on a needle. Take 5 damage."
                                characterhealth = characterhealth - 5
                                print(computer)
                                print("Unfortunately, you are too far down the slide to climb back up. Game over.")
                                sys.exit("Game over.")
                            elif (slidetohell == 2): 
                                computer = "You are unable to catch yourself, and crash at the end. Game over."
                                print("You are unable to catch yourself, and crash at the end. Game over.")
                                sys.exit("You are unable to catch yourself, and crash at the end. Game over.");
                            elif (slidetohell == 3):
                                computer = "You manage to stop yourself, but the slime covers your head. Game over."
                                sys.exit("Game over.")
                                print(computer)
                        elif rightleft == "Left":
                            print("You swerve left, and a weird shadow attacks you. Game over.")
                            sys.exit("Game over.")
        if choice11 == "Keep Going":
            print("You travel down the long tunnel until you emerge into a new tunnel.")
            rightleft = raw_input("There are two branches: Right or Left?")
            if rightleft == "Right":
                print("You run down the tunnel, and it soon gets more and more slippery, as the water soon turns into slime.")
                print("You soon loose your footing, and slide at an uncontrollable pace towards the bottom.")
                slidetohell = randint(1, 3)
                if (slidetohell == 1):
                    computer = "You reach out your hand to stop your fall, and you hand catches on a needle. Take 5 damage."
                    characterhealth = characterhealth - 5
                    print(computer)
                    print("Unfortunately, you are too far down the slide to climb back up. Game over.")
                    sys.exit("Game over.")
                elif (slidetohell == 2): 
                    computer = "You are unable to catch yourself, and crash at the end. Game over."
                    print("You are unable to catch yourself, and crash at the end. Game over.")
                    sys.exit("You are unable to catch yourself, and crash at the end. Game over.");
                elif (slidetohell == 3):
                    computer = "You manage to stop yourself, but the slime covers your head. Game over."
                    print(computer)
                    sys.exit("Game over.")

#regular earth                    
#earth_choice = raw_input("Choose what you were experimenting before the accident: Particle Physics or Holographic Universe Theory: ")
if earth_choice == "Particle Physics":
    name2 = raw_input("Please enter your Character's Name: ")
    welcome2 = ("Welcome to Earth 54")
    print(welcome2 , name2)
    print("""
       In this earth, the people have already learned about the multiverse.
       A team of scientists including your doppelganger are working to build a particle accelerator,
       similar to the one you developed on your earth to harness enough energy from the universe to
       create a portal between realities/earths.
       Once such a portal is created, Earth 54 will be able to travel to your Earth and conquer it.
       This could be fatal to the multiverse, as the current futures could be disrupted.
       It is up to you to figure out a solution to the problem without causing harm to your doppelganger
       or any other inhabitant of this Earth, because all versions of that person will be harmed.
       There is one solution to this problem. You could disable the particle accelerator.""")
choice2 = raw_input("Do you choose to: Disable the particle accelerator:Y/N ")
if choice2 == "Y":
    print("""You are going down the large corridor in the lab. You are walking in the empty corrider when 
    you hear a footstep. You are getting a little scared. You are feeling confused about what to do. You
    have two choices on what to do. Do you want to investigate or keep going? Choose below.""")
    choice22 = raw_input("Do you choose to: Investigate, or Keep Going? ")
    if choice22 == "Investigate":
        print("As you head towards the strange sound, a shadow appears behind you. It's the doppelganger of your colleague, Jaime Maddox!")
        fight2 = raw_input("Do you choose to: Knock him out, or Try to talk?")
        if fight2 == "Knock him out":
            jaimehealth = 10
            characterhealth = 10 
            while (characterhealth > 0 & jaimehealth > 0):
                userchoice = raw_input("What would you like to do: Attack, Defend, Dodge, or Stay Put?")
                from random import randint
                RNGesusbless1 = randint(1, 6)
                if (RNGesusbless1 == 1):
                    computer = "Attack"
                elif (RNGesusbless1 == 2):
                        computer = "Defend"
                elif (RNGesusbless1 == 3):
                        computer = "Dodge"
                elif (RNGesusbless1 == 4):
                        computer = "Stay Put"
                elif (RNGesusbless1 == 5):
                        computer = "Stay Put"
                elif (RNGesusbless1 == 6):
                        computer = "Stay Put" 
                if computer == userchoice:
                        print("You're having a hard time knocking this person out!")
                if computer == "Attack" and userchoice == "Defend":
                        print("Jaime tries to attack, but you expertly defend yourself.")
                if computer == "Attack" and userchoice == "Stay Put":
                        print("Jaime attacks, and does 1 damage.")
                        characterhealth = characterhealth - 1 
                if computer == "Attack" and userchoice == "Dodge":
                        print("Jaime comes at you, but you are faster. You leap out of harms way just in time.")
                        characterenergy = characterenergy - 1
                if computer == "Defend" and userchoice == "Dodge":
                        print("Neither you nor Jaime attack, instead both choosing to defend.")
                        characterenergy = characterenergy - 1
                if computer == "Defend" and userchoice == "Attack":
                        print("You try and attack Jaime, but you cannot get through to land a blow.")
                        characterenergy = characterenergy - 1
                if computer == "Defend" and userchoice == "Stay Put":
                        print("You don't do anything, and Jaime defends, expecting an attack.")
                        characterenergy = characterenergy + 1
                if computer == "Dodge" and userchoice == "Defend":
                        print("You defend yourself, and the Jaime dodges, expecting an attack.")
                if computer == "Dodge" and userchoice == "Attack":
                        print("You try to attack Jaime, but Jaime dodges your incoming attack.")
                        characterenergy = characterenergy - 1
                if computer == "Dodge" and userchoice == "Stay Put":
                        print("You stay where you are, and Jaime dodges, thinking that you will attack.")
                if computer == "Stay Put" and userchoice == "Attack":
                        print("Jaime makes no move as you attack. Jaime takes 2 Damage.")
                        jaimehealth = jaimehealth - 2
                if computer == "Stay Put" and userchoice == "Dodge":
                        print("Jaime makes no move and you dodge, expecting an attack.")
                if computer == "Stay Put" and userchoice == "Defend":
                        print("Jaime does nothing as you defend, expecting an attack.")
#someone test this part i debugged it but im not sure if it actually works
elif characterhealth <= 0 & jaimehealth > 0:
    print("Jaime triumphs, striking you down with a mighty blow. You are taken to prison. All hope is lost for the universe. Game Over.")        
else:
       print("Good Job! You hide Jaime's body and then continue on with your mission.")
       print("You get to the accelerator. Your task is to disable it.")
t = ["Screwdriver", "Electric Generator", "Pliers", "Wrench", "Drill"]
#player = False
#while player == False:
player = raw_input("Pick One: Screwdriver, Electric Generator, Pliers, Wrench, Drill ")
from random import randint
computer = randint(1,6)
if player == computer:
        print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
elif player == "Electric Generator":
        if computer == "Screwdriver":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Drill":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")    
elif player == "Screwdriver":
        if computer == "Pliers":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Wrench":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")    
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")
elif player == "Pliers":
        if computer == "Screwdriver":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Drill":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")    
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")
elif player == "Wrench":   
        if computer == "Screwdriver":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Pliers":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")  
elif player == "Drill":    
        if computer == "Electric Generator":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Wrench":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")        
else:
        print("Invalid Play! Please check your spelling.")
#player = False
computer =  t[randint(0,4)] 
if choice22 == "Keep Going":
    print("As you head towards the accelerator, a shadow appears behind you. It's the doppelganger of your colleague, Jaime Maddox!")
    fight2 = raw_input("Do you choose to: Knock him out, or Try to talk?")
    if fight2 == "Knock him out":
        jaimehealth = 10
        characterhealth = 10
        while (characterhealth > 0 & jaimehealth > 0):
            userchoice = raw_input("What would you like to do: Attack, Defend, Dodge, or Stay Put?")
            from random import randint
            RNGesusbless1 = randint(1, 6)
            if (RNGesusbless1 == 1):
                computer = "Attack"
            elif (RNGesusbless1 == 2):
                computer = "Defend"
            elif (RNGesusbless1 == 3):
                computer = "Dodge"
            elif (RNGesusbless1 == 4):
                computer = "Stay Put"
            elif (RNGesusbless1 == 5):
                computer = "Stay Put"
            elif (RNGesusbless1 == 6):
                computer = "Stay Put" 
        if computer == userchoice:
            print("You're having a hard time knocking this person out!")
        if computer == "Attack" and userchoice == "Defend":
            print("Jaime tries to attack, but you expertly defend yourself.")
        if computer == "Attack" and userchoice == "Stay Put":
            print("Jaime attacks, and does 1 damage.")
            characterhealth = characterhealth - 1 
        if computer == "Attack" and userchoice == "Dodge":
            print("Jaime comes at you, but you are faster. You leap out of harms way just in time.")
            characterenergy = characterenergy - 1
        if computer == "Defend" and userchoice == "Dodge":
            print("Neither you nor Jaime attack, instead both choosing to defend.")
            characterenergy = characterenergy - 1
        if computer == "Defend" and userchoice == "Attack":
            print("You try and attack Jaime, but you cannot get through to land a blow.")
            characterenergy = characterenergy - 1
        if computer == "Defend" and userchoice == "Stay Put":
            print("You don't do anything, and Jaime defends, expecting an attack.")
            characterenergy = characterenergy + 1
        if computer == "Dodge" and userchoice == "Defend":
            print("You defend yourself, and the Jaime dodges, expecting an attack.")
        if computer == "Dodge" and userchoice == "Attack":
            print("You try to attack Jaime, but Jaime dodges your incoming attack.")
            characterenergy = characterenergy - 1
        if computer == "Dodge" and userchoice == "Stay Put":
            print("You stay where you are, and Jaime dodges, thinking that you will attack.")
        if computer == "Stay Put" and userchoice == "Attack":
            print("Jaime makes no move as you attack. Jaime takes 2 Damage.")
            jaimehealth = jaimehealth - 2
        if computer == "Stay Put" and userchoice == "Dodge":
            print("Jaime makes no move and you dodge, expecting an attack.")
        if computer == "Stay Put" and userchoice == "Defend":
            print("Jaime does nothing as you defend, expecting an attack.")
#someone test this part i debugged it but im not sure if it actually works
jaimehealth = 10
characterhealth = 10
if characterhealth <= 0 & jaimehealth > 0:
    print("Jaime triumphs, striking you down with a mighty blow. You are taken to prison. All hope is lost for the universe. Game Over.")        
            
else:
    print("Good Job! You hide Jaime's body and then continue on with your mission.")
    print("You get to the accelerator. Your task is to disable it.")

from random import randint
t = ["Screwdriver", "Electric Generator", "Pliers", "Wrench", "Drill"]
computer = t[randint(0,4)]
#player = False
while player == False:
    player = raw_input("Pick One: Screwdriver, Electric Generator, Pliers, Wrench, Drill ")
    if player == computer:
        print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
    elif player == "Electric Generator":
        if computer == "Screwdriver":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Drill":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")    
    elif player == "Screwdriver":
        if computer == "Pliers":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Wrench":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")    
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")
    elif player == "Pliers":
        if computer == "Screwdriver":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Drill":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")    
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")
    elif player == "Wrench":   
        if computer == "Screwdriver":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Pliers":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")  
    elif player == "Drill":    
        if computer == "Electric Generator":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Wrench":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")        
    else:
        print("Invalid.")
#player = False
computer =  t[randint(0,4)]
if fight2 == "Try to talk":
    print("Jaime doesn't look that understanding. He tries to strangle you!")
    jaimehealth = 10
    characterhealth = 10
    while (characterhealth > 0 & jaimehealth > 0):
        userchoice = raw_input("What would you like to do: Attack, Defend, Dodge, or Stay Put?")
        from random import randint
        RNGesusbless1 = randint(1, 6)
        if (RNGesusbless1 == 1):
            computer = "Attack"
            if (RNGesusbless1 == 2):
                computer = "Defend"
            if (RNGesusbless1 == 3):
                computer = "Dodge"
            if (RNGesusbless1 == 4):
                computer = "Stay Put"
            if (RNGesusbless1 == 5):
                computer = "Stay Put"
            if (RNGesusbless1 == 6):
                computer = "Stay Put" 
            if computer == userchoice:
                print("You're having a hard time knocking this person out!")
            if computer == "Attack" and userchoice == "Defend":
                print("Jaime tries to attack, but you expertly defend yourself.")
            if computer == "Attack" and userchoice == "Stay Put":
                print("Jaime attacks, and does 1 damage.")
                characterhealth = characterhealth - 1 
            if computer == "Attack" and userchoice == "Dodge":
                print("Jaime comes at you, but you are faster. You leap out of harms way just in time.")
                characterenergy = characterenergy - 1
            if computer == "Defend" and userchoice == "Dodge":
                print("Neither you nor Jaime attack, instead both choosing to defend.")
                characterenergy = characterenergy - 1
            if computer == "Defend" and userchoice == "Attack":
                print("You try and attack Jaime, but you cannot get through to land a blow.")
                characterenergy = characterenergy - 1
            if computer == "Defend" and userchoice == "Stay Put":
                print("You don't do anything, and Jaime defends, expecting an attack.")
                characterenergy = characterenergy + 1
            if computer == "Dodge" and userchoice == "Defend":
                print("You defend yourself, and the Jaime dodges, expecting an attack.")
            if computer == "Dodge" and userchoice == "Attack":
                print("You try to attack Jaime, but Jaime dodges your incoming attack.")
                characterenergy = characterenergy - 1
            if computer == "Dodge" and userchoice == "Stay Put":
                print("You stay where you are, and Jaime dodges, thinking that you will attack.")
            if computer == "Stay Put" and userchoice == "Attack":
                print("Jaime makes no move as you attack. Jaime takes 2 Damage.")
                jaimehealth = jaimehealth - 2
            if computer == "Stay Put" and userchoice == "Dodge":
                print("Jaime makes no move and you dodge, expecting an attack.")
            if computer == "Stay Put" and userchoice == "Defend":
                print("Jaime does nothing as you defend, expecting an attack.")
#someone test this part i debugged it but im not sure if it actually works- aishani
characterhealth = 10
if characterhealth <= 0 & jaimehealth > 0:
    print("Jaime triumphs, striking you down with a mighty blow. You are taken to prison. All hope is lost for the universe. Game Over.")        
            
else:
       print("Good Job! You hide Jaime's body and then continue on with your mission.")
       print("You get to the accelerator. Your task is to disable it.")
       from random import randint
t = ["Screwdriver", "Electric Generator", "Pliers", "Wrench", "Drill"]
computer = t[randint(0,4)]
player = False
while player == False:
    player = raw_input("Pick One: Screwdriver, Electric Generator, Pliers, Wrench, Drill ")
if player == computer:
    print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
    if player == "Electric Generator":
        if computer == "Screwdriver":
           print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Drill":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")    
    elif player == "Screwdriver":
        if computer == "Pliers":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Wrench":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")    
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")
    elif player == "Pliers":
        if computer == "Screwdriver":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        if computer == "Drill":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")    
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")
    elif player == "Wrench":   
        if computer == "Screwdriver":
           print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Pliers":
           print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")  
    elif player == "Drill":    
        if computer == "Electric Generator":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        elif computer == "Wrench":
            print("You failed! You are caught and sent to prison. All hope is lost for the universe. Game Over!")
        else:
            print("You disabled the accelerator and saved the universe. The energy held in the accelerator opens up a portal and takes you home.")        
    else:
        print("Invalid Play! Please check your spelling.")
player = False
computer =  t[randint(0,4)]
    
if choice2 == "N":
        print("Over the years you grow more and more isolated and lose sight of what is your reality. FAILED MISSION.")
if start == "No":
        print("Over the years you grow more and more isolated and lose sight of what is your reality. FAILED MISSION.")
else:
    print("Over the years you grow more and more isolated and lose sight of what is your reality. FAILED MISSION.")
#The end FINALLY










    