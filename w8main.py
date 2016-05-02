def charCount():
    sentence='sangmyung university'
    d=dict()
    for c in sentence:
        if c not in d:
            d[c]=1
        else :
            d[c]+=1       
    return d
    return len(d)
    return d.keys()
    return d.values()

def bargraph():
    sentence='sangmyung university'
    d=dict()
    for c in sentence:
        if c not in d:
            d[c]=1
        else :
            d[c]+=1


    import matplotlib
    import matplotlib.pyplot as plt


    plt.bar( range(len(d)),d.values(), align='center')
    plt.xticks(range(len(d)),list(d.keys()))
    plt.show()

def lab8():
    mychar=charCount()
    print mychar
 
    bargraph()
def main():
    lab8()

if __name__=="__main__":
    main()