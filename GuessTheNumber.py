import random
while(True):
    num = random.randint(1, 10)
    guess = 0
    while(guess!=num):
        guess = int(input("Guess an integral value between 1 to 10 - "))
        if(guess>num):
            print("Your guess is greater than the number")
        elif(guess<num):
            print("Your guess is less than the number")
    print("You got that right !")
    check = int(input("Do you want to play again?Enter 1 for yes and 0 for no - "))
    if(check==0):
        break
