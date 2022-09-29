print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 

firstChoice = input("A crossroads lies ahead, there are two paths, left and right, which one will you pick? Type LEFT or RIGHT \n")
firstChoice = str(firstChoice.lower())

if firstChoice == "right":
    print("You have chosen poorly, and have fallen into a whole, game over")
    exit()
else:
    print("Look at the mountains on the right side of the road! Lets continue \n")

secondChoice = input ("The tide is high right now, there are dangerous carnivorous trout in the river, we should be able to cross once the die goes down, your choice! Type WAIT or SWIM \n ")
secondChoice = str(secondChoice.lower())

if secondChoice == "swim":
    print("******* You were eaten by a trout *********** I warned you about the trouts, and you still chose to cross the river rather than wait. GAME OVER \n")
    exit()
else:
    print("The tide went down faster than I thought, lets keep exploring! \n")

thirdChoice = input("Three doors lie ahead, a red one, a yellow one and a blue one, my scanners can't detect whats behind them, which one will we go through? Type RED, YELLOW OR BLUE \n")
thirdChoice = str(thirdChoice.lower())

if thirdChoice == "red":
    print ("*** BURNT TO A CRISP *** \n There was fire on the other side of the door")
    exit()
elif thirdChoice == "blue":
    print ("*** YOU WERE MOLLED BY THE BEAST *** \n Damn it, how didn't my scanners pick that up")
    exit()
else:
    print("Congratulations you won, you have safely gotten to your destination! \n ")
