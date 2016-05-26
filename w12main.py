def time():
    import time
    msg='[lhs edited {0}]'.format(time.strftime('%Y-%m-%d %H:%M:%S'))
    fin=open('output.txt', 'r')
    fout=open('outputUpper.txt','w')
    for line in fin:
        words=line.split()
        fout.write(msg)
        fout.write('\t')
        for word in words:
            if word =="line":
                fout.write('\t')
            fout.write(word)
        fout.write('\n')
    fin.close()
    fout.close()
    


def number():
    data=[1,2,3,4,5,6,7,8,9,10]
    fout=open('number.txt','w')
    for i in data:
        str='{0}\t'.format(i)
        if not i%2:
            str=str+'\n'
        fout.write(str)
    fout.close()
    
def lab12():
    time()
    number()
    
def main():
    lab12()
    
if __name__=="__main__":
    main() 
    