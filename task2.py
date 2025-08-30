import random

def rand():
    secret_number=random.randint(1,100)
    attempts=0
    while(True):
        print("start the number guessing game \n")
        player_number=int(input("enter the your guessing number 1 to 100: "))
        attempts+=1
        if player_number < secret_number:
            print("This number is lower!!!")
        elif player_number > secret_number:
            print("This number is higher!!!")
        else:
            print("congratulations!!! your got won...")
            print(attempts)
            exit()
rand()
    
