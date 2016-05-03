def charCount():
    sentence='sangmyung university'
    d=dict()
    for c in sentence:
        if c not in d:
            d[c]=1
        else :
            d[c]+=1       
    return d

def bargraph(d):


    import matplotlib
    import matplotlib.pyplot as plt


    plt.bar( range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()

    
def countDigitalsLatters(word):
    d=dict()
    d={"word":0, "number":0}
    for i in word:
        if i.isdigit()==True:
            d["number"]=d["number"]+1
        else:
            d["word"]=d["word"]+1
            
    import matplotlib
    import matplotlib.pyplot as plt
    plt.bar(range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)), list(d.keys()))
    plt.show()  
    
def appliances():
    myhouse={ 'TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'}
    friendhouse={'coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'}
    print "only myhouse : " ,myhouse.difference(friendhouse)
    print "only friend's house:" , friendhouse.difference(myhouse)
    print "myhouse and friend's house : ", myhouse.intersection(friendhouse)
    print "all: ", myhouse.union(friendhouse)
    print  "appliances number: ",len(myhouse)+len(friendhouse-myhouse)    

def lab8():
    d=charCount()
    print d
 
    bargraph(d)
    
    word="7 hongjidong"
    countDigitalsLatters(word)
    
    appliances()
def main():
    lab8()

if __name__=="__main__":
    main()

wn.exitonclick()