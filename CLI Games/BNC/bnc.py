from random import randint
roles = ["Bear", "Ninja", "Cowboy"]

computer = roles[randint(0, 2)]

#stretch challenge - game intro
print(f"Get ready to play Bear, Ninja, Cowboy!")
#stretch challenge - print instructions
instruction = input("Would you like instructions? (yes/no) ")
if instruction == "yes":
    print("""Bear, Ninja, Cowboy is an exciting game of strategy and skill! 
Pit your wit against the computer! Choose a player: Bear, Ninja, or Cowboy. 
The computer chooses a player. Bear eats Ninja, Ninja defeats Cowboy and cowboy shoots bear.""")


player = False

while player == False:
    
    #stretch challenge - inputting an unrecognized name. The while loop keeps asking/printing message until player enters a recognized name allowing the loop to break.
    while True:
        player = input("Bear, Ninja, or Cowboy? > ")
        if player not in ["Bear", "Ninja", "Cowboy"]:
            print(f"{player} is not Bear, Cowboy, or Ninja and Bear, Cowboy, and Ninja are the only allowed names.")
        else:
            break
    
    #player = input("Bear, Ninja, or Cowboy? > ")


    if computer == player:
        print("DRAW!")
    elif computer == "Cowboy":
        if player == "Bear":
            print("You lose!", computer, "shoots", player)
        else:  # computer is cowboy, player is ninja
            print("You win!", player, "defeats", computer)
    elif computer == "Bear":
        if player == "Cowboy":
            print("You win!", player, "shoots", computer)
        else:  # computer is bear, player is ninja
            print("You lose!", computer, "eats", player)
    elif computer == "Ninja":
        if player == "Cowboy":
            print("You lose!", computer, "defeats", player)
        else:  # computer is ninja, player is bear
            print("You win!", player, "eats", computer)


    play_again = input("Would you like to play again? (yes/no) > ")
    if play_again == 'yes':
        player = False
        computer = roles[randint(0, 2)]
    else:
        break
