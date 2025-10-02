import random
''' 
1 is for snake
-1 for water
0 for gun
''' 

computer=random.choice([1,-1,0])
print("Welcome to Snake Water Gun game")
youstr=input("Enter your choice:")
youDict={"s":1,"w":-1,"g":0}
you=youDict[youstr]
reverseDict={1:"snake",-1:"water",0:"gun"}

print(f"Computer chose {reverseDict[computer]}\nYou chose {reverseDict[you]}")
if computer==you:
    print("It's a tie")

else:
    '''if computer ==-1 and you==1: (python-you ) == -2
        print("You win")
    elif computer==-1 and you==0: (python-you ) == -1
        print("You lose")
    elif computer==1 and you==-1: (python-you ) == 2    
        print("You lose")
    elif computer==1 and you==0: (python-you ) == 1
        print("You win")
    elif computer==0 and you==-1: (python-you ) == 1
        print("You win")
    elif computer==0 and you==1:    (python-you ) == -1
        print("You lose")
        
        the below logic is written on the basis of the difference between computer and you'''

    if (computer-you == -1) or (computer-you == 2):
        print("You lose")
    else:
        print("You win")
