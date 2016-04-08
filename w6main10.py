def upanddowngame():
    trycount=0
    
    inputnumber=input("input number")
    mynumber=input("my number")

  
    while inputnumber!=mynumber:
        
        if inputnumber>mynumber:
                print "High!"
                mynumber=input("Guess number!")
                trycount=trycount+1
        
        if inputnumber<mynumber:
                print "Low!"
                mynumber=input("Guess number!")
                trycount=trycount+1
        
        if inputnumber==mynumber:
             print "Correct!"
        
   
    
        
    print "trycount is "+str(trycount)