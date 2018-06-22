from random import randint
user = raw_input("Rock , Paper, Scissors, Lizard, Spock")
choice = randint(1,3)
if (choice == 1):
    computer = "Rock"
elif(choice == 2):
    computer = "Paper"
else: 
    computer = "Scissors"
if (computer == user):
    print("draw")
elif(computer == "Scissors" and user == "Paper"):
    print("Computer wins")
elif(computer == "Paper" and user == "Scissors"):
    print("User wins")
elif(computer == "Scissors" and user == "Rock"):
    print("User wins")
elif(computer == "Rock" and user == "Paper"):
    print("User wins")
elif(computer == "Rock" and user == "Scissors"):
    print("Computer wins")
elif(computer == "Paper" and user == "Rock"):
    print("Computer wins")
elif(computer == "Lizard" and user == "Rock"):
    print("User Wins")
elif(computer == "Lizard" and user == "Scissors"):
    print("User wins")
elif(computer == "Scissors" and user == "Lizard"):
    print("Computer wins")
elif(computer == "Rock" and user == "Lizard"):
    print("Computer wins")
elif(computer == "Spock" and user == "Paper" ):
    print("User wins")
elif(computer == "Spock" and user == "Lizard"):
    print("User wins")
elif(computer == "Spock" and user == "Paper"):
    print("User wins")
elif(computer == "Lizard" and user == "Spock"):
    print("Computer wins")
elif(computer == "Paper" and user == "Spock"):
    print("Computer wins0")