import random
s = 1
w = 2
g = 3
randans = random.randint(1,3)
player = int(input("palyer's turn : \n choose one of these :\n Snake (1) \n Water (2)\n Gun (3)\n"))
print(randans)

if(player==1 and randans==2):
    print("You won the game \n ")
elif(player==2 and randans==3):
    print("You  won the game \n")
elif(player==3 and randans == 1):
    print("You won the game \n")
elif(player==1 and randans==3):
    print("You lost the game \n")
elif(player==2 and randans == 1):
    print("You lost the game \n")
elif(player == 3 and randans == 2):
    print("You lost the game \n")
elif(player == 1 and randans==1):
    print("it's a tie !!!")
elif(player == 2 and randans==2):
    print("it's a tie !!!")
elif(player == 3 and randans==3):
    print("it's a tie !!!")
else:
    print("wrong input ! try aganin")