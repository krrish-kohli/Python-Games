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


direction1st = input("You are at a crossroads. \nDo you want to go left or right?\n")
direction1 = direction1st.lower()

# Continue in the game
if direction1 == "left":
          direction2nd = input("You've come to a lake. There is an island in the middle of the lake.\n Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
          direction2 = direction2nd.lower()
          # Continue in the game
          if direction2 == "wait":
                    direction3rd = input("You arrive at the island unharmed. There is a house with 3 doors.\n One red, one yellow and one blue. Which colour do you choose?\n")
                    direction3 = direction3rd.lower()
                    # Game over
                    if direction3 == "red":
                              print("It's a room full of fire. You got burned. Game Over.")
                    # Game won
                    elif direction3 == "yellow":
                              print("You found the treasure! You Win!")
                    # Game over
                    else:
                              print("You've been eaten by the beasts. Game Over.")
          # Game over
          else:
                    print("You get attacked by an angry trout. Game Over.")
# Game over
else:
          print("You fell into a hole. Game Over.")
