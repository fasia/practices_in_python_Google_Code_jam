__author__ = 'fsiavash'


myinput2= open('D-small-practice-1.in','r')
mystring='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def permute(i, s):
    slist = list(s)
    for j in i:

        print slist.index(j)

tests= myinput2.readline().strip('\n')
for x in range(int(3)):
    subStringNum= myinput2.next().strip('\n') #numbers of substrings
    #print('numbers:', numbers)
    myarr= []
    for s in myinput2.next().split():
        myarr.append(s)
        print myarr
    for i in myarr:
        if mystring.find(i):
            permute(i, mystring)
        else:
            print 'IMPOSSIBLE'
    del myarr

        #output_large= file('D-out-large.txt','a+')
        #output_large.write("Case #"+str(x+1)+': '+str(modulo_out)+"\n")
        #print(counter[0]+1)
        #counter[0]=0
        #del myarr
        #while len(myarr)>0:
        # result+=' '+findmatch(myarr[0])

        #print'Case #',x+1,':', result

        #result = ''