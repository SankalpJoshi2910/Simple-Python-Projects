#Rock Paper Scissor

print("***Rock Paper Scissors***")
import random
import string
string.letters='rps'
#print(random.choice(string.letters))

wanna_play=input("\n Want to Play (y/n) : ")
if wanna_play=="y":
    while wanna_play=="y":
        user_choice=input("\nRock(r) Paper(p) Scissors(s) : ")
        computer_choice=random.choice(string.letters)
        if user_choice==computer_choice:
            print("\nComputer_choice : ", computer_choice)
            print("\nIt`s A Tie")
        elif user_choice=="r" and computer_choice=="p":
            print("\nComputer_choice : ", computer_choice)
            print("\nComputer Wins!!!!")
        elif user_choice=="r" and computer_choice=="s":
            print("\nComputer_choice : ", computer_choice)
            print("\nYou Wins!!!!")
        elif user_choice=="p" and computer_choice=="r":
            print("\nComputer_choice : ", computer_choice)
            print("\nYou Win!!!!")
        elif user_choice=="p" and computer_choice=="s":
            print("\nComputer_choice : ", computer_choice)
            print("\nComputer Wins!!!!")
        elif user_choice=="s" and computer_choice=="r":
            print("\nComputer_choice : ", computer_choice)
            print("\nComputer Wins!!!!")
        elif user_choice=="s" and computer_choice=="p":
            print("\nComputer_choice : ", computer_choice)
            print("\nYou Wins!!!!")
        wanna_play=input("\n Want to play more?? (y/n) : ")
        
else:
    print("\nCome Back Soon ^_^")
        
           


Other way to choose input for computer instead of random.choice
     

                list1=["r","p","s"]
                   import random
                         b=(random.randint(0,2))
                                   print(list1[b])
  
