import random

while True:
    choices = ['r', 'p', 's']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("slect 'r' for rock, 'p' for paper and 's' for scissors :").lower()

    print("computer :", computer)

    #Tie Condition
    if player == computer:
        print("Both have selected the same so its a tie!")

    #Win condition
    if (player == 'r' and computer == 's') or (player == 's' and computer == 'p') or (player == 'p' and computer == 'r'):
        print("The player won the game!")

    #Lose condition
    if (player == 's' and computer == 'r') or (player == 'p' and computer == 's') or (player == 'r' and computer == 'p'):
        print("The player has lost the game")
    
    play_again = input("Would like to play again ? (y/n) :").lower()
    if play_again != 'y':
        break
print("Bye")