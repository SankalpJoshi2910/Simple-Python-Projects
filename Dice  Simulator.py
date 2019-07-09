import random
import time
print("Dice Rolling :")
roll_dice=input("Roll Dice? (y/n) : ")

if roll_dice=="y":
    
    while roll_dice=="y":
           print("\nRolling the Dice.....")
           time.sleep(1)
           dice= int(random.randint(1,6))
           print("The value is : ", dice)
    
           if dice==1 or dice==6:
               print("\nGot the 2nd chance!!!")
               print("\nRolling the Dice.....")
               time.sleep(1)
               dice= int(random.randint(1,6))
               print("the value is : ", dice)
        
           else:
              print("\nOther player Turn")
        
           roll_dice=input("\nPress y to roll dice again : ")
           if roll_dice!="y":
               print("Thanks For Playing ^_^ ")
           
else:
    print("Thanks For playing")
