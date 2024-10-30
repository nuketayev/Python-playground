import random

while True:
    choices = ["Rock","Paper","Scissors"]
    computer = random.choice(choices)

    player = input("Please enter your choice 'Rock', 'Paper', or 'Scissors': ")

    if player == "Rock" or player == "Paper" or player == "Scissors":
        if player == "Rock":
            if computer == "Paper":
                print("Computer: "+computer)
                print("You lost!")
            elif computer == "Scissors":
                print("Computer: "+computer)
                print("You won!")
            else:
                print("Computer: "+computer)
                print("Draw!")
        elif player == "Paper":
            if computer == "Scissors":
                print("Computer: "+computer)
                print("You lost!") 
            elif computer == "Rock":
                print("Computer: "+computer)
                print("You won!")       
            else:
                print("Computer: "+computer)
                print("Draw!")
        elif player == "Scissors":
            if computer == "Rock":
                print("Computer: "+computer)
                print("You lost!") 
            elif computer == "Paper":
                print("Computer: "+computer)
                print("You won!")           
            else:
                print("Computer: "+computer)
                print("Draw!")
    else:
        print("\nPlease type as intructed above!")
    playAgain = input("Do you want to play again? (yes/no): ").lower()
    if playAgain != "yes":
        break
print("Bye!")
