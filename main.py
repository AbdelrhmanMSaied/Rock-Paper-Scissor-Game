import random



print("Welcome to Rock-Paper-Scissors!\n")
print("Play game roles: ") 
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

choices = ["Rock", "Paper", "Scissors"  ]

while True:

    print("Choose an option:")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    
    try:
        playerChoice = int(input("Do ur move: "))
    except ValueError:
            print("Please enter a valid number.\n")
            continue

    if (playerChoice <1 or playerChoice >3):
         playerChoice = int(input("Please Enter a number between 1 - 3"))

    playerChoice= choices[playerChoice - 1]
    print("\nUser choice is:", playerChoice)


    print("Now it's Computer's Turn...")
    computerChoice= random.randint(1, 3)
    computerChoice = choices[computerChoice - 1]
    print("Computer choice is:", computerChoice)

    if playerChoice == computerChoice:
        print("<== It's a Tie! ==>")

    elif (
        (playerChoice == "Rock" and computerChoice == "Scissors") or
        (playerChoice == "Paper" and computerChoice == "Rock") or
        (playerChoice == "Scissors" and computerChoice == "Paper")
    ):
        print("<== User Wins! ==>")

    else:
        print("<== Computer Wins! ==>")

    playAgain = input("\nDo you want to play again? (y/n): ")
    if playAgain.lower() != "y":
        print("Thanks for playing! Goodbye.")
        break
    

    



    
    