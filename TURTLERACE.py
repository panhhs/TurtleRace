#basic jekinw panta me auto
import turtle      #bibliotheken
import random



s =  turtle.Screen()
s.bgcolor("black")

t1 = turtle.Turtle() #baptisia

t2 = turtle.Turtle()

ref = turtle.Turtle()

t1.pencolor("green")

t1.fillcolor("green")

t2.pencolor("yellow")

t2.fillcolor("yellow")


t1.pu()

t2.pu()
t1.goto(-200,100)
t2.goto(-200,-100)
while t1.pos() < (300,100) and t2.pos() < (300,-100):
 n = random.randint(0, 6)
 t1.fd(n)
 n = random.randint(0, 6)
 t2.fd(n)

if t1.pos() > (300,100):
    print("green won")
    ref.pencolor("green")
    ref.write("Green wins", move = True, font=("Arial",20,"bold"))
    ref.color("black")
elif t2.pos() > (300,100):
    print("yellow won")
    ref.pencolor("yellow")
    ref.write("Yellow won", move = True, font=("Arial",20,"bold"))
    ref.color("black")

t1.pd()
t2.pd()
t1.rt(90)
t1.fd(200)
t2.lt(90)
t2.fd(200)


turtle.done()




