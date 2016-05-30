def file():
    result=list()
    try:
        fin1=open('python.txt','a')
        fin2=open('outputNumber.txt','r')
        for line in fin2:
            fin1.write(line)
        fin1.close()
        fin2.close()
    except Exception as e:
        print e
    return result


import turtle
wn=turtle.Screen()
t1=turtle.Turtle()



def getCoordsFormFile():
    aFile='reccoords.txt'
    aFile=open(aFile,'w')
    aFile.write('0,0,100,100'+'\n')
    aFile.write('200,200,150,150'+'\n')
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
        t1.setpos(mycoord[0])
        t1.pendown()
        for i in mycoord:
            t1.goto(i)   
    frec.close()

def lab13(): 
    file()
    getCoordsFormFile()
    drawSquareWithCoords()

def main(): 
    lab13() 
    
if __name__=="__main__":  
    main()  