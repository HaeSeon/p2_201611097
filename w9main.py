def Locations():
    Locations=tuple()
    Locations=[(37.576549, 126.985520),(37.571618, 126.976551),(37.574577, 126.957754),(37.570180, 126.983026),(37.565804, 126.976946)]
    print Locations
    x=list()
    for i in Locations:
        "x={0} y={1}".format(i[0],i[1])
        import math
        distance= math.sqrt((37.575869-i[0])**2+(126.976637-i[1])**2)
        x.append(distance)
    print "minimum distance:",min(x)
    
def Seoulpeople():
    my2dlist=[
    [74425,76326],
    [61164,61636],
    [109688,115744],
    [144796,146776],
    [174996,181676],
    [177841,177434],
    [204630,205980],
    [223373,232245],
    [161055,166130],
    [171576,176735],
    [279169,293772],
    [239450,251066],
    [148690,156510],
    [182977,196992],
    [237792,242641],
    [283869,296762],
    [209344,210282],
    [118965,114441],
    [186503,186856],
    [195734,203014],
    [254381,249472],
    [212401,229111],
    [271654,295354],
    [319197,335045],
    [229829,231671]
    ]   

    mansum=0
    for i in my2dlist:
        mansum+=i[0]
    print "man's sum is:",mansum

    manaverage=mansum/len(my2dlist)
    print "man's average is",manaverage


    womansum=0
    for i in my2dlist:
        womansum+=i[1]
    print "woman's sum is",womansum

    womanaverage=womansum/len(my2dlist)
    print "woman's average is",womanaverage



    x=list()
    for i in my2dlist:
        gusum=i[0]+i[1]
        x.append(gusum)
   
    import matplotlib
    import matplotlib.pyplot as plt
    plt.bar(range(len(x)),x,align='center')

    plt.show()
    
    
def lab9():
    Locations()
    Seoulpeople()

    
def main():
    lab9()
    
    
if __name__=="__main__":
    main()