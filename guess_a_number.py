import random
top_range = input("type the top range")
if top_range.isdigit():
    top_range=int(top_range)

random_number =random.randint(0,top_range)

while True:
    guess = int(input("enter your guess"))
    if guess == random_number:
        print("you got it")
        break
    elif(guess >= random_number):
        print("you are above the number")
    else:
        print("YOU are below the number")

    print("please type the next number")