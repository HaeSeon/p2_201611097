def Coffee():
    allData=list()
    allData=[["Coffee","Water","Milk","Icecream"],
    ["Espresso","No","No","No"],
    ["Long Black","Yes","No","No"],
    ["Flat White","No","Yes","No"],
    ["Cappuccino","No","Yes-Frothy","No"],
    ["Affogato","No","No","Yes"]
    ]

    data=allData[1:]

    t=0
    for i in range (0,len(data)):
        print data[i][2]
        if data[i][2]!="No":
            t=t+1 
    t=float(t)
    percent=str(t/5*100)
    print "milk percent is",percent,"%" 



def Study():
    StudyData=list()
    StudyData=[
        ["English",100],
        ["Math",200],
        ["English",200],
        ["Math",200],
        ["English",100],
        ["Math",300]
    ]

    english=0
    math=0
    for i in StudyData:
        if i[0]=="English":
            english+=1
        elif i[0]=="Math":
            math+=1
    englishsum=0
    mathsum=0
    for i in StudyData:
        if i[0]=="English":
            englishsum+=i[1]
        elif i[0]=="Math":
            mathsum+=i[1]


    print "Math sum is ",mathsum
    print "English sum is ",englishsum
    print "Math average is ",str(mathsum/math)
    print "English average is "+str(englishsum/english)
    
    
def Song():
    song=list()
    song=["when I find myself in times of trouble",
    "mother Mary comes to me",
    "speaking words of wisdom let it be",
    "and in my hour of darkness",
    "she is standing right in front of me",
    "speaking words of wisdom let it be",
    "let it be let it be",
    "let it be let it be",
    "shisper words of wisdom let it be",
    "and when the broken-hearted people",
    "living in the world agree",
    "there will be an answer let it be",
    "for though they may be parted",
    "there is still a chance that they will see",
    "there will be an answer let it be",
    "let it be let it be",
    "let it be let it be",
    "yeah there will be an answer let it be",
    "let it be let it be",
    "let it be let it be",
    "whisper words of wisdom let it be",
    "let it be let it be",
    "ah let it be yeah let it be",
    "whisper words of wisdom let it be",

    "and when the night is cloudy",
    "there is still a light that shines on me",
    "shine on until tomorrow let it be",
    "i wake up to the sound of music",
    "mother Mary comes to me",
    "speaking words of wisdom let it be",

    "let it be let it be",
    "let it be yeah let it be",
    "oh there will be an answer let it be",
    "let it be let it be",
    "let it be yeah let it be",
    "whisper words of wisdom let it be"]
    doc=song
    d=dict()
    for line in doc:
        words=line.split()
        for c in words:
            if c not in d:
                d[c]=1
            else:
                d[c]=d[c]+1
    print max(d, key=d.get)


def lab10():
    Coffee()
    Study()
    Song()
    
    
def main():
    lab10()

if __name__=="__main__":
    main()
