name = raw_input("Put in your name: ")

import turtle
import random
wn=turtle.Screen()


import time

t1=turtle.Turtle()
t2=turtle.Turtle()


t1.speed(10)

t2.shape("turtle")
t2.color("Green")
t2.penup()




size1=100
size2=50
pos1=(-300,0)
pos2=(-150,-200)
pos3=(130,100)
pos4=(-170,150)
pos5=(-100,-50)
pos6=(50,-100)
pos7=(-50,200)







def getCoordsFormFile():
    aFile='reccoords.txt'
    aFile=open(aFile,'w')
    aFile.write('-50,100,50,200'+'\n')
    aFile.write('-300,-100,-200,0'+'\n')
    aFile.write('50,-200,150,-100'+'\n')
    aFile.close()


def drawSquareWithCoords():
    frec=open('reccoords.txt')
    coords=[]
    for line in frec:
        line1=line.split(',')
        coords.append([(line1[0],line1[1]),(line1[2],line1[3].strip())])
        for coord in coords:
            x1=int(coord[0][0])
            x2=int(coord[1][0])
            y1=int(coord[0][1])
            y2=int(coord[1][1])
        mycoord=((x1,y1),(x2,y1),(x2,y2),(x1,y2),(x1,y1))
        t1.penup()
        t1.pencolor("Pink")
        t1.fillcolor("pink")
        t1.begin_fill()
        t1.setpos(mycoord[0])
        t1.pendown()
        for i in mycoord:
            t1.goto(i) 
        t1.begin_fill()
    frec.close()
    
getCoordsFormFile()
drawSquareWithCoords()

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
    


def Setting(): 
   
    DrawTriangleup(size1,pos2)
    DrawCircle(size2,pos3)
    DrawTriangleup(size2,pos4)
    DrawTriangledown(size2,pos4)
    DrawCircle(size2,pos5)


 

Setting()






result=0

    
x=float()
y=float()
    
def k1():
    t2.fd(15)
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
    global result
    
    if 50<=x<=70 and -10<=y<=10:
        t2.write("treasure")
        result=result+10
	print "score:",result
   
    if 220<=x<=230 and -180<=y<=-170:
        t2.write("treasure")
        result=result+10
        print "score:",result
    if -280<=x<=270 and -200<=y<=-190:
        t2.write("treasure")
        result=result+10
        print "score:",result
    if -195<=x<=-185 and -10<=y<=10:
        t2.write("treasure")
        result=result+10
	print "score:",result
    if -300<=x<=-280 and 50<=y<=70:
        t2.write("treasure")
        result=result+10
	print "score:",result
    if -200<=x<=-180 and 205<=y<=215:
        t2.write("treasure")
        result=result+10
	print "score:",result
    if 55<=x<=65 and 145<=y<=155:
        t2.write("treasure")
        result=result+10
	print "score:",result
    if 260<=x<=270 and 210<=y<=230:
        t2.write("treasure")
        result=result+10
	print "score:",result

    score()
    
  
    
    
def k2():
    t2.left(15)
 
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
def k3():
    t2.right(15)
 
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
def k4():
    t2.back(10)
 
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


    


def score():
    user=open('score.txt', 'a')
    if result>=70:
	t2.goto(0,0)
        msg='user {0}'.format(name + '\t' + time.strftime('%Y.%m.%d , %H:%M:%S'))
        print("End Game"+'\t'+'Score' + '\t'+ str(result) )
        user.write('\n' + 'Score' + '\t'+ str(result) +'\t' + msg)
        user.close()
  
	wn.exitonclick()



def addkeys():
    wn.onkey(k1, "Up")

    wn.onkey(k2, "Left")
    wn.onkey(k3, "Right")
    wn.onkey(k4, "Down")


addkeys()
wn.listen()
turtle.mainloop()

wn.exitonclick()