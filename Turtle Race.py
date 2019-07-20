#Empty Race Track


print("welcome")

for i in range(0,256):
    if(i%64==0):
        print()
    elif(i%4==0):
        print(" ", end="")
    else:
        print("_",end="")




#Race Track complete

from turtle import *
from random import randint

for step in range(6):
  #write(step)
  #right(90)
  #penup()
  forward(200)
  #penup()
  backward(200)
  right(90)
  if(step<5):
    forward(30)
  left(90)
  pendown()

penup()  
goto(5,-15)
write("S")
goto(5,-45)
write("T")
goto(5,-75)
write("A")
goto(5,-105)
write("R")
goto(5,-135)
write("T")
goto(190,-45)
write("E")
goto(190,-75)
write("N")
goto(190,-105)
write("D")
goto(200,0)
right(90)
pendown()
forward(150)

t1= Turtle()
t1.color('green')
t1.shape('turtle')
t1.penup()
t1.goto(-15,-15)
t1.pendown()

t2= Turtle()
t2.color('blue')
t2.shape('turtle')
t2.penup()
t2.goto(-15,-45)
t2.pendown()

t3= Turtle()
t3.color('cyan')
t3.shape('turtle')
t3.penup()
t3.goto(-15,-75)
t3.pendown()

t4= Turtle()
t4.color('black')
t4.shape('turtle')
t4.penup()
t4.goto(-15,-105)
t4.pendown()

t5= Turtle()
t5.color('magenta')
t5.shape('turtle')
t5.penup()
t5.goto(-15,-135)
t5.pendown()

d1=0
d2=0
d3=0
d4=0
d5=0
for i in range(100):
  s1=randint(1,4)
  d1=d1+s1
  if(d1>=206):
    print("!!! Turtle 1 Won !!!")
    exit()
  s2=randint(1,4)
  d2=d2+s2
  if(d2>=205):
    print("!!! Turtle 2 Won !!!")
    exit()
  s3=randint(1,4)
  d3=d3+s3
  if(d3>=204):
    print("!!! Turtle 3 Won !!!")
    exit()
  s5=randint(1,4)
  d5=d5+s5
  if(d5>=202):
    print("!!! Turtle 5 Won !!!")
    exit()
  
  s4=randint(1,4)
  d4=d4+s4
  if(d4>=203):
    print("!!! Turtle 4 Won !!!")
    exit()
  t1.forward(s1)
  t2.forward(s2)
  t3.forward(s3)
  t4.forward(s4)
  t5.forward(s5)
