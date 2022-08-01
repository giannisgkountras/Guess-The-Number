import random
import time
import os


pc_number = random.randrange(1,100)
player_tries = 1
pc_tries = 1
pc_guess = 50
start = 1
end = 100
choice = -1

print("Welcome to guess the number!")
time.sleep(1)
while not choice == 3: 
    choice = int(input("If you want to guess the computer's number type 1.\nIf you want to have the computer guess your number type 2.\nTo exit press 3.\nYour choice: "))
    os.system("cls")
    while not (choice == 1 or choice ==2 or choice ==3):
        os.system("cls")
        choice = int(input("If you want to guess the computer's number type 1.\nIf you want to have the computer guess your number type 2.\nTo exit press 3.\nYour choice: "))
    
    if choice == 1:
        print("The computer picked a number between 1 and 100. Try to find it as quickly as possible!")
        time.sleep(1)



        player_guess = int(input("Type in your guess: "))
        while player_guess != pc_number:
            if player_guess> pc_number:
                player_tries +=1
                print("Your guess was too high.",end=" ")
                player_guess = int(input("Type in your guess: "))
            if player_guess< pc_number:
                player_tries +=1
                print("Your guess was too low.",end=" ")
                player_guess = int(input("Type in your guess: "))
        time.sleep(1)
        os.system("cls")
        print("Y",end="")
        time.sleep(0.1)
        print("O",end="")
        time.sleep(0.1)
        print("U",end="")
        time.sleep(0.1)
        print(" ",end="")
        time.sleep(0.1)
        print("A",end="")
        time.sleep(0.1)
        print("R",end="")
        time.sleep(0.1)
        print("E",end="")
        time.sleep(0.1)
        print(" ",end="")
        time.sleep(0.1)
        print("C",end="")
        time.sleep(0.1)
        print("O",end="")
        time.sleep(0.1)
        print("R",end="")
        time.sleep(0.1)
        print("R",end="")
        time.sleep(0.1)
        print("E",end="")
        time.sleep(0.1)
        print("C",end="")
        time.sleep(0.1)
        print("T",end="")
        time.sleep(0.1)
        print("!")
        time.sleep(1)

        print("It took you", player_tries, "tries to guess it.")
        time.sleep(2)
        os.system("cls")
    if choice == 2:
        print("Pick a number from 1 to 100 and the computer will try to guess it")
        player_number = int(input("Type in your number: "))
        while player_number <1 or player_number>100:
            print("Type a number between 1 and 100.")
            player_number = int(input("Type in your number: "))

        while pc_guess != player_number:
            print("Is your number higher or lower than", pc_guess, "? (type 'l' for lower or 'h' for higher): " , end="")
            h_or_l = input()
            if h_or_l == 'h':
                start = pc_guess
                pc_guess = (end + pc_guess)//2
                

            if h_or_l == 'l':
                end = pc_guess
                pc_guess = (start + pc_guess)//2
            pc_tries += 1
        os.system("cls")
        print("Your number is: " +str(pc_guess)+"!")
        time.sleep(1)
        print("It took the computer", pc_tries, "tries")
        time.sleep(3)
        os.system("cls")
os.system("cls")

print("G",end="")
time.sleep(0.1)
print("o",end="")
time.sleep(0.1)
print("o",end="")
time.sleep(0.1)
print("d",end="")
time.sleep(0.1)
print("b",end="")
time.sleep(0.1)
print("y",end="")
time.sleep(0.1)
print("e",end="")
time.sleep(0.1)
print("!",end="")
time.sleep(2)
   