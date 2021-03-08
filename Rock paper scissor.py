from random import randint
#list of play options
n = ["rock", "paper", "scissor"]
#assign a random play for computer
computer = n[randint(0, 1)]
#set player to False
player = False

while player == False:
#player set to True
    player = input("Choose (rock, paper, scissor):\n")
    if player == computer:
        print("You tied.")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "defeats", player)
        else:
            print("You win!", player, "defeats", computer)
    elif player == "paper":
        if computer == "scissor":
            print("You lose!", computer, "defeats", player)
        else:
            print("You win!", player, "defeats", computer)
    elif player == "scissor":
        if computer == "rock":
            print("You lose!", computer, "defeats", player)
        else:
            print("You win!", player, "defeats", computer)
    else:
        print("You lose..............................CHEATER!!")
    #player set to False so the loop continues
    player = False
    computer = n[randint(0, 2)]
