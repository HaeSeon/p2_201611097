import turtle
import random
wn=turtle.Screen()

t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()

t1.speed(7)

t2.shape("turtle")
t2.color("Green")
t2.penup()

t3.shape("turtle")
t3.color("Black")
t3.speed(5)
t3.penup()



size1=100
size2=50
pos1=(-300,0)
pos2=(-150,-200)
pos3=(130,100)
pos4=(-170,150)
pos5=(-100,-50)
pos6=(50,-100)
pos7=(-50,200)

def DrawSquare(size,pos):
    t1.pencolor("Pink")
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.fillcolor("Pink")
    t1.begin_fill()
    for i in range(0,4):
        t1.fd(size)
        t1.right(90)
    t1.end_fill()

def DrawTriangleup(size,pos):
    t1.pencolor("Orange")
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.fillcolor("Orange")
    t1.begin_fill()
    for i in range(0,3):
        t1.fd(size)
        t1.left(120)
    t1.end_fill()
    
def DrawTriangledown(size,pos):
    t1.pencolor("Orange")
    t1.penup()
    t1.goto(pos)
    t1.pendown()
    t1.fillcolor("Orange")
    t1.begin_fill()
    for i in range(0,3):
        t1.fd(size)
        t1.right(120)
    t1.end_fill()
    

    
def DrawCircle(size,pos):
    t1.pencolor("Grey")
    t1.penup()
    t1.goto(pos)
    t1.fillcolor("Grey")
    t1.begin_fill()
    t1.circle(size2)
    t1.end_fill()
    
def Turtle3():
    t1.speed(7)

    t2.shape("turtle")
    t2.color("Green")
    t2.penup()

    t3.shape("turtle")
    t3.color("Black")
    t3.speed(5)
    t3.penup()

    while True: 
        fd=random.randrange(1,100)
        head=random.randrange(0,360)
        t3.fd(fd)
        t3.setheading(head)
    


def Setting(): 
    DrawSquare(size1,pos1)    
    DrawTriangleup(size1,pos2)
    DrawCircle(size2,pos3)
    DrawTriangleup(size2,pos4)
    DrawTriangledown(size2,pos4)
    DrawCircle(size2,pos5)
    DrawSquare(size1,pos6)
    DrawSquare(size1,pos7)
    Turtle3()

Setting()



    
x=float()
y=float()
    
def k1():
    t2.fd(10)
    (x,y)=t2.pos()
    global point
    if -300<=x<=-200 and -100<=y<=0:
        print "Game Over"
        t2.goto(0,0)
    if -50<=x<=50 and 100<=y<=200:
        print "Game Over"
        t2.goto(0,0)
    if 50<=x<=150 and -200<=y<=-100:
        print "Game Over"
        t2.goto(0,0)
    if y<=1.73205080756888*x+150*1.73205080756888-200 and y<=1.73205080756888*(-x)-1.73205080756888*50-200 and y>=-200:
        print "Game Over"
        t2.goto(0,0)
    if y<=1.73205080756888*x+170*1.73205080756888+150 and y>=1.73205080756888*x+1.73205080756888*120+150 and y<=-1.73205080756888*x+150-1.73205080756888*120 and y>=-1.73205080756888*x+150-1.73205080756888*170: 
        print "Game Over"
        t2.goto(0,0)
    if (x+100)*(x+100)+y*y<=2500:
        print "Game Over"
        t2.goto(0,0)
    if (x-130)*(x-130)+(y-150)*(y-150)<=2500:
        print "Game Over"
        t2.goto(0,0)

def k2():
    t2.left(15)

def k3():
    t2.right(15)

def k4():
    t2.back(10)

wn.onkey(k1, "Up")
wn.onkey(k2, "Left")
wn.onkey(k3, "Right")
wn.onkey(k4, "Down")
wn.listen()
wn.exitonclick()



if  t2.pos()==t3.pos():
    print "You win!!!"

wn.exitonclick()