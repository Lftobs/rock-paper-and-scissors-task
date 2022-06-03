
#rock paper or scissors game

import random
print("This is a rock, paper and  scissors game.")
print("R = rock")
print("P = paper")
print("S = scissors")
while True:
    choices = ["r","p","s"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Enter your choice : ").lower()
        print(f"\nYou chose {player}, computer chose {computer}.\n")


    if player == computer:
        print(f"Both player selected {player}. Hence it's a tie")
  

    elif player == "r":
        if computer == "p":
            print("Paper covers rock. You lose!")

        else:
            print("Rock smashes scissors. You win!")
       

    elif player == "s":
        if computer == "r":
            print("Rock smashes scissors. You lose!")
        else:
            print("Scissors cuts paper. You win!")
       

    elif player == "p":
        if computer == "s":
            print("Scissors cuts paper. You lose!")
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        else:
            print("Paper covers rock. You win!")
        

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Bye!")