import random
user_score = 0
computer_score = 0
options = ["rock","paper","sissor"]
while True:
    user_input = input("enter your options,Rock,Paper,Sissors, enter q to Quit   ").lower()
    if user_input == "q":
        quit()
    if user_input not in options:
        continue

    computer_input = (options[random.randint(0,2)])
    if user_input == "rock" and computer_input == "sissors":
        print("you won")
        user_score += 1
        print("your score is",user_score,"computer score is",computer_score)
        continue
    elif user_input == "paper" and computer_input == "rock":  
        print("you won")
        user_score += 1
        print("your score is",user_score,"computer score is",computer_score)
        continue 
    elif user_input == "sissor" and computer_input == "paper":  
        print("you won")
        user_score += 1
        print("your score is",user_score,"computer score is",computer_score)
        continue 
    elif user_input == "sissor" and computer_input == "sissor":  
        print("rematch")
        print("your score is",user_score,"computer score is",computer_score)
        continue 
    elif user_input == "rock" and computer_input == "rock":  
        print("rematch")
        print("your score is",user_score,"computer score is",computer_score)
        continue 
    elif user_input == "paper" and computer_input == "":  
        print("rematch")
        print("your score is",user_score,"computer score is",computer_score)
        continue 
    else:
        print("you lost... computer choosed",computer_input)

        computer_score += 1
        print("computer score is",computer_score)

    print("thank you")
   