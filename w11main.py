import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
t2=turtle.Turtle()
t2.speed(2)

def Drawline(size,pos):
    t2.pencolor("Pink")
    t2.penup()
    t2.goto(pos)
    t2.pendown()
    t2.fd(size)

pos1=(-300,0)
size1=100
Drawline(size1,pos1)

def k1():
    t1.fd(20)
    (x,y)=t1.pos()
    global point
    if -300<=x<=-200 and y==0:
        print "Game Over"
        t1.goto(0,0)
def k2():
    t1.left(15)

def k3():
    t1.right(15)

def k4():
    t1.back(10)

def mousegoto(x,y):
    t1.setpos(x,y)

    (x,y)=t1.pos()
    global point
    if -300<=x<=-200 and y==0:
        print "Game Over"
        t1.goto(0,0)

def addmouse():
    wn.onclick(mousegoto)


def addkeys():
    wn.onkey(k1, "Up")
    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")


addkeys()
addmouse()
wn.listen()
turtle.mainloop()