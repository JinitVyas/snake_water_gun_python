# snake water gun or stone paper sessior game using python


import random #for computer's turn
import os
from playsound import playsound # for additional sfx

def won(comp , you ): # definition of the function  

    # for all the possible cases when computer chooses snake :    
    if(comp == 's' ):
        if(you == 'w'):
            return False
        elif(you == 'g'):
            return True
        elif(you == 's'):
            return None

    # for all the possible cases when computer chooses snake :
    if(comp == 'w' ):
        if(you == 'g'):
            return False
        elif(you == 's'):
            return True
        elif(you == 'w'):
            return None

    # for all the possible cases when computer chooses snake :
    if(comp == 'g' ):
        if(you == 's'):
            return False
        elif(you == 'w'):
            return True
        elif(you == 'g'):
            return None

comp = random.choice(['s','w','g']) #the function that chooses a random answer for computer
print("computer's turn : \n Snake (s) \n Water (w) \n Gun (g)\n")  # computer's turn
you = input ("Choose something : \n Snake (s) \n Water (w) \n Gun (g)\n\n\n") # player's turn

print(f"You entered : {you}")  # printing your responce
print(f"Bot Entered {comp}") # finally exposing the random choice of computer



a = won (comp,you) #calling the function
if a == None : # condition when both chose equal
    print("tie!")
elif a == True: # condition when player wins
    print("You Won ! ")
    root_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file_path = os.path.join(root_dir,"sound_fx","win_sfx.mp3")
    playsound(sound_file_path)
    
elif a == False: # condition when computer wins
    print("You Lose ! ")
    root_dir = os.path.dirname(os.path.abspath(__file__))
    sound_file_path = os.path.join(root_dir,"sound_fx","lose_sfx.mp3")
    playsound(sound_file_path)
