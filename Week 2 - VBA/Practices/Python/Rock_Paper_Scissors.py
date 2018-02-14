# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

keep_playing = True

# Run Conditionals
while(keep_playing == True):
    # Computer Selection
    computer_choice = random.choice(options)

    # User Selection
    user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

    if(user_choice == "r" and computer_choice == "s"):
        print("User: " + user_choice + "\n")
        print("Computer: " + computer_choice + "\n")
        print("Rock Smashes Scissors! You Win")
    elif(user_choice == "p" and computer_choice == "r"):
        print("User: " + user_choice + "\n")
        print("Computer: " + computer_choice + "\n")
        print("Paper covers rock, you win!")
    elif(user_choice == "s" and computer_choice == "p"):
        print("User: " + user_choice + "\n")
        print("Computer: " + computer_choice + "\n")
        print("scissors cuts paper, you win!")
    elif(user_choice == "r" and computer_choice == "p"):
        print("User: " + user_choice + "\n")
        print("Computer: " + computer_choice + "\n")
        print("paper covers rock, you lose!")
    elif (user_choice == "p" and computer_choice == "s"):
        print("User: " + user_choice + "\n")
        print("Computer: " + computer_choice + "\n")
        print("scissors cuts paper, you lose!")
    elif (user_choice == "s" and computer_choice == "r"):
        print("User: " + user_choice + "\n")
        print("Computer: " + computer_choice + "\n")
        print("rock smashes scissors, you lose!")
    else:
        print("User: " + user_choice + "\n")
        print("Computer: " + computer_choice + "\n")
        print("It's a tie!")

    play_again = input("Play again? 'y' or 'n': ")
    while (play_again != "y" or play_again != "n"):

        if(play_again == "n"):
            print("Thanks for playing!")
            keep_playing = False
            break
        elif(play_again == "y"):
            keep_playing = True
        else:
            print("invalid input. try again\n")
            play_again = input("Play again? 'y' or 'n': ")

