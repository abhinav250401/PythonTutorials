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
print("Let\'s begin the game!..'")
#Taking the initial input
choice1=input("You're at a crossroad. Where do you want to go ? Type 'left' or 'right'.\n" ).lower()
if choice1=="left":
  choice2=input("You've come to a lake. There's an island in the middle of the lake. Type 'wait' to wait for a boat or type 'swim' to swim across.\n" ).lower()
  if choice2=="wait":
    choice3=input("You arrived at the island unharmed. Now you see a house with three doors. The doors are 'red', 'blue' and 'yellow' in color. Choose your door by typing the color\n")
    if choice3=="red":
      print("You got burned. GAME OVER ):")
    elif choice3=="blue":
      print("You got eaten. GAME OVER ):")
    else:
      print("YAY !! You found the treasure (:")
  else:
    print("A shark ate you ! Oops GAME OVER ):")
else:
  print("You fell into the valley of death. GAME OVER ):")
