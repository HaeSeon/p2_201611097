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



def leapYear():
    year=raw_input("input year : ")
    year=int(year)
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        print "leap year"
    else :
        print "normal year"




def lap6():
    leapYear()
    upanddowngame()

def main():
    lap6()
if __name__=="__main__":
    main()