def aa():
    class Dog(object):
        def __init__(self,name):
            self.name=name
        def getName(self):
            print "my dog name is",self.name
        def talk(self):
            print "mung mung"

    class ShihTzuDog(object):
        def talk(self):
            print "si si"

    class Maltese(object):
        def talk(self):
            print "mal mal"


    mydog=Dog('puppy')
    mydog.talk()
    myshi=ShihTzuDog()
    myshi.talk()
    mymal=Maltese()
    mymal.talk()
    
    
def lab14():
    aa()
    
    
def main():
    lab14()
    
if __name__=="__main__":  
    main()   