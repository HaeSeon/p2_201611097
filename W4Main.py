import turtle
wn=turtle.Screen()
t1=turtle.Turtle()
def makeMaze(size,bigger,turns,sides,angle):
 for i in range(sides):
  if(i%2):
   size=size+bigger
   t1.fd(size)
   t1.right(angle)
makeMaze(20,10,10,50,90)
wn.exitonclick()