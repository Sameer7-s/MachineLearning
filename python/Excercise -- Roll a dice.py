'''WAP a programm to simulate a roll of a die/dice 
A die has 6 faces with numbers 1 to 6 written on them 
the programm should randomly prints a number btw  1 and 6'''

import random
print("welcome to game of rolling a dice")

while True:
    choice = input("press 'Enter' to roll a dice or 'q' to quit" )
    choice = choice.strip()###this is use for using extra space of q for quit 
    if choice =='q':
        print("Thanks for playing the game ,bye!")
        break
    elif choice == '':
        number = random.randint(1,6)
        print(f"your number is {number}")
    else:
        print("Invalid input!!!")
      
print("GAME OVER!!!!!!")