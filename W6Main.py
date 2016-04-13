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




def sumList(aList):
    sum=0
    for i in range(0,len(aList)):
        sum=sum+aList[i]
    return sum


def lab6():
    aList=list()
    for i in range(1,1000):
        if i%4==0 and i%5!=0:
            aList.append(i)
    labsum=sumList(aList)
    print labsum

    leapYear()
    upanddowngame()




def main():
    lap6()



if __name__=="__main__":
    main()