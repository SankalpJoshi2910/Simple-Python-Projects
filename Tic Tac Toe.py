#Welcome TO tic tac toe

from turtle import *


for step in range(2):
  right(90)
  forward(100)
  penup()
  backward(100)
  left(90)
  forward(50)
  pendown()

penup()
goto(-50,-30)
pendown()
for step2 in range(2):
    forward(150)
    penup()
    backward(150)
    right(90)
    forward(30)
    left(90)
    pendown()


print("WElcome to Tic Tac Toe")

wanna_play=input("\nWant to play ?? (y/n): ")
turn=0
list1=[]
w1=[]
w2=[]

key=""

  
    
    
if wanna_play=="y":
  while wanna_play=="y":
    turn=turn+1
    a1=int(input("enter the block: "))
    
    if turn%2==0:
      w1.append(a1)
      print(w1)
    else:
      w2.append(a1)
      print(w2)
    
    
    if a1==1 and a1 not in list1:
      penup()
      goto(-25,-15)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")
    
    
    elif a1==2 and a1 not in list1:
      penup()
      goto(25,-15)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")
    
    
    elif a1==3 and a1 not in list1:
      penup()
      goto(75,-15)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")
        
        
    elif a1==4 and a1 not in list1:
      penup()
      goto(-25,-45)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")
        
        
    elif a1==5 and a1 not in list1:
      penup()
      goto(25,-45)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")
        
    elif a1==6 and a1 not in list1:
      penup()
      goto(75,-45)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")
        
    elif a1==7 and a1 not in list1:
      penup()
      goto(-25,-75)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")
        
    elif a1==8 and a1 not in list1:
      penup()
      goto(25,-75)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")
    
    elif a1==9 and a1 not in list1:
      penup()
      goto(75,-75)
      pendown()
      if turn%2==0:
        write("X")
      else:
        write("O")    
    
    else:
      print("invalid input:")
      turn=turn-1
    list1.append(a1) 
    
    for i in range(len(w2)):
      
      number=str(w2[i])
      if number not in key:
        key+=number
    print(key)
  
    if "1"and"4" and"7"in key:
      print("player 1 won")
      exit()
    
    if turn<=8:
      wanna_play=input("\n Want to play more?? (y/n) : ")
    else:
      exit()
else:
  print("Fuck OFf")
