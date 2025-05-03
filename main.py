import random
print("Let's play Rock, Paper & Scissors !")


def get_user_input():
    # Function to get user input 
    while(True):    
        user_choice = str(input("Enter your choice(rock,paper,scissors):")).strip().lower()

        if user_choice in ['rock','paper','scissors']:
            return user_choice
        else:
            print("Please enter a valid input!")

def get_computer_choice():
    # Funtion to get computer input 
    com_choice = random.choice(['rock','paper','scissors'])
    return com_choice   


def play(hum_score,com_score,choice,com_choice): 
     
    if choice == com_choice:
        print("\tIt's a tie.")        
    elif choice == "rock" and com_choice == "paper" or choice == "paper" and com_choice == "scissors" or choice == "scissors" and com_choice == "rock":
        com_score += 1
        print("\tComputer win!")
    else:
        hum_score += 1
        print("\tYou won!")

    return hum_score,com_score      

def determine_winner(hum_score,com_score):
    if hum_score == com_score:
        return"\tThis game is a tie!"
    elif hum_score>com_score:
        return("\tYeh! you won this game.")
    else:
        return("\tComputer won this game!")

def game():    
    if __name__ == "__main__":
        com_score = 0
        hum_score = 0 
        # defining rounds of this game      
        for _ in range(1,4):
            print("\tRound ",_)
            usr_choice = get_user_input()
            print(f"Your Choice is: {usr_choice}")

            com_choice = get_computer_choice()
            print(f"Computer Choice is: {com_choice}")

            hum_score,com_score=play(hum_score,com_score,usr_choice,com_choice)

        print("Final score:\tYou:{0}\tComputer:{1}".format(hum_score,com_score))
        print(determine_winner(hum_score,com_score))

        choice = str(input("Do you want to play again(yes/no):")).strip().lower()

        while True:
            if choice in ['yes','y']:
                game()
            elif choice in ['no','n']:
                print("See you later!")
            else:
                print("Please enter a valid input!")

game()   #Start the game
