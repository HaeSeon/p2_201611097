def drawSquareAtSave(size, pos):
    t1.penup()
    t1.setpos(pos)
    t1.pendown()
    track=list()
    for i in range(0,4):
        track.appand(t1.pos())
        t1.forward(size)
        t1.right(90)
    return tracks


def lab7():
    mytrack=drawSquareAtSave(100,(0,0))
    print mytrack
    
def main():
    lab()