import random

choices=["rock","paper","scissors"]

#computer choices randomly

computer=random.choice(choices)

user=input("enter your choice").lower

print ("computer choices",computer)
 
#game choices


if computer == user :
        print("its a Draw")

elif user=="paper":
    if computer=="rock":
        print("you won")
else:
        print("you lost")

if user=="rock":
     if computer=="scissors":
          print("you won")
     else:
          print("you lost")


else:
     print("invalid word!! please enter rock,paper or scissors")