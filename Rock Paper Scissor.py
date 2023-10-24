import random
  
user_score=0
computer_score=0
while(True):
    x=int(input('Press 1 to play , Press 2 to exit'))
    if (x==1):
        options = ["Rock", "Paper", "Scissors"]

        user_choice = input("Choose Rock, Paper, or Scissors: ")

        computer_choice = random.choice(options)

        print("You chose: ", user_choice)

        print("Computer chose: ", computer_choice)

        if user_choice == computer_choice:

            print("It's a tie!")

        elif user_choice == "Rock" and computer_choice == "Scissors":
            user_score=user_score+1
            print("You win!")

        elif user_choice == "Paper" and computer_choice == "Rock":
            user_score=user_score+1
            print("You win!")

        elif user_choice == "Scissors" and computer_choice == "Paper":
            user_score=user_score+1
            print("You win!")

        else:
            computer_score=computer_score+1
            print("Computer wins!")
    else:
        print('User score is',user_score)
        print('Computer score is',computer_score)
        break
