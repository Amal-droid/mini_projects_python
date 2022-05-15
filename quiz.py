score = 0
print("welcome to my quiz")
play = input("Do you wanna play quiz?   ")
if play.lower() != "yes":
    quit()
else:
    print("ok let's start")
    answer =input("what does CPU stands for? ")
    if answer.lower() == "central processing unit":
        print("correct... Welcome to next question")
        score += 1
    else:
        print("incorrect answer")

    answer = input("what does GPU stands for? ")
    if answer.lower() == "graphics processing unit":   
        print("correct... Welcome to next question")
        score += 1
    else:
        print("incorrect answer")    

    answer = input("what does PSU stands for? ")
    if answer.lower() == "power supply unit":   
        print("correct... Welcome to next question")
        score += 1 
    else:
        print("incorrect answer")
    
    answer = input("what does RAM stands for? ")
    if answer.lower() == "ramdom access memory":   
        print("correct... Welcome to next question")
        score += 1  
    else:
        print("incorrect answer")

    if score == 4:
        print("you have won the quiz")
    else:
        print("Better luck next time... you have"+ str(score)+" scores")    
