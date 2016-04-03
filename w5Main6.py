a=raw_input('a input kawi, bawi, bo : ')
b=raw_input('b input kawi, bawi, bo : ')
if a=='kawi':
    if b=='kawi':
        print "%s" %"Draw"
    elif b=='bo':
        print "%s" %"kawi Win"
    elif b=='bawi':
        print "%s" %"bawi win"
elif a=='bawi':
    if b=='bo':
        print "%s" %"bo Win"
    elif b=='bawi':
        print "%s" %"Draw"
elif a=='bo':
    if b=='bo':
        print "%s" %"Draw"