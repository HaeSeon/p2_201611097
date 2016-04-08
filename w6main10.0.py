def leapYear():
    year=raw_input("input year : ")
    year=int(year)
    if (year%4 == 0) and (year%100 !=0 or year%400==0):
        print "leap year"
    else :
        print "normal year"