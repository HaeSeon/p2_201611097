def drawSquareAtSave(size, pos):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    tracks=list()
    for i in range(0,4):
        tracks.append(t1.pos())
        t1.fd(size)
        t1.right(90)
    return tracks




def drawSquareForm(tracks):
    import turtle
    wn=turtle.Screen()
    t1=turtle.Turtle()


    for i in range(1,5):
 	    t1.goto(tracks[i])
    return tracks


def lab7():
    mytrack=drawSquareAtSave(100, (0,0))
    print mytrack
     

    tracks=dict()
    tracks=({0:(0,0),1:(200,0),2:(200,200),3:(0,200),4:(0,0)})
    mytracks=drawSquareForm(tracks)
    print mytracks

    
    
    
def main():
    lab7()



if __name__=="__main__":
    main()