# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input(
    "You are at the cross road ,Where do you want to go ? Type 'left' or 'right'\n"
).lower()

if choice == "left":
    choice1 = input(
        'You\'r came to a lake. There is an island middle of the lake.Type "wait" to wait or type "swim" to swim \n').lower()
    if choice1 == "wait":
        choice2 = input(
            "You arrived at the island unharmed.There is a house with 3 droos.one red,one yellow and one blue,"
            "which colour do you choose\n").lower()
        if choice2 == "yellow":
            print("You have entered a room with treasure. You Won The Game!")
        elif choice2 == "red":
            print("you have entered a room with full of snakes.Game Over")
        elif choice2 == "blue":
            print("You have entered a room of Lion. Game Over")
        else:
            print("You have enter wrong option")
    else:
        print("Your are bitten by crocodile.Game Over")
else:
    print("You have fell into a hole Game Over")
