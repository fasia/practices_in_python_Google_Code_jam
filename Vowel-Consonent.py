__author__ = 'fsiavash'


myinput2= open('C-large-practice.in','r')

myinput = [20,40,10]
#myinput1= open('A-large-practice.in', 'r')

def wordLength(n):
    if n==1: # last letter which should only have V
          return V%1000000007
    elif n ==0:
        return 1
    else:
        return V* wordLength(n-1)%1000000007+(C*V*wordLength(n-2))%1000000007

#tests= myinput2.readline().strip('\n')
for x in range(int(1)):
    #numbers= myinput2.next().strip('\n') #numbers of items
    #print('numbers:', numbers)
    myarr = [20,10,50]
    #for s in myinput2.next().split():
     #   myarr.append(int(s))
    L= myarr[2]
    V= myarr[1]
    C=myarr[0]
    output=wordLength(L) # false means that cons is not accepted
    modulo_out= output%1000000007
    output_large= file('C-out-large.txt','a+')
    output_large.write("Case #"+str(x+1)+': '+str(modulo_out)+"\n")
    #print(counter[0]+1)
    #counter[0]=0
        #del myarr
        #while len(myarr)>0:
        # result+=' '+findmatch(myarr[0])

        #print'Case #',x+1,':', result

        #result = ''