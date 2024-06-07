#basic jekinw panta me auto
import turtle      #bibliotheken
import random



s =  turtle.Screen()
s.bgcolor("black")

nigga = turtle.Turtle() #baptisia

nigger = turtle.Turtle()

ref = turtle.Turtle()

nigga.pencolor("green")

nigga.fillcolor("green")

nigger.pencolor("yellow")

nigger.fillcolor("yellow")


nigga.pu()

nigger.pu()
nigga.goto(-200,100)
nigger.goto(-200,-100)
while nigga.pos() < (300,100) and nigger.pos() < (300,-100):
 n = random.randint(0, 6)
 nigga.fd(n)
 n = random.randint(0, 6)
 nigger.fd(n)

if nigga.pos() > (300,100):
    print("green won")
    ref.pencolor("green")
    ref.write("Green wins", move = True, font=("Arial",20,"bold"))
    ref.color("black")
elif nigger.pos() > (300,100):
    print("yellow won")
    ref.pencolor("yellow")
    ref.write("Yellow won", move = True, font=("Arial",20,"bold"))
    ref.color("black")

nigga.pd()
nigger.pd()
nigga.rt(90)
nigga.fd(200)
nigger.lt(90)
nigger.fd(200)


turtle.done()





