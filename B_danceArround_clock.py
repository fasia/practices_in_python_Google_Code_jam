__author__ = 'fsiavash'





myinput= open('B-small-practice.in','r')

myinput2= open('B-large-practice.in', 'r')


def swap_odd():
    #print 'before:', arrayDancers
    for i in range(0,len(arrayDancers)-1,2):
        #print 'before:', arrayDancers
        temp= arrayDancers[i]
        arrayDancers[i]= arrayDancers[i+1]
        arrayDancers[i+1]=temp
        #print 'aftre:', arrayDancers

    #print('after', arrayDancers)

def swap_even():
    for i in range(1,len(arrayDancers)-1,2):
        #print 'before:', arrayDancers
        temp= arrayDancers[i]
        arrayDancers[i]= arrayDancers[i+1]
        arrayDancers[i+1]=temp
        #print('after', arrayDancers)
    temp= arrayDancers[0]
    arrayDancers[0]= arrayDancers[len(arrayDancers)-1]
    arrayDancers[len(arrayDancers)-1]=temp
    #print(arrayDancers)



result =''
tests= myinput2.readline().strip('\n')
#print('number of tests', tests)
for x in range(int(tests)):
    #numbers= myinput2.next().strip('\n') #numbers of items
    #print('numbers:', numbers)
    myarr = []
    for s in myinput2.next().split():
        myarr.append(int(s))
    #print('myarr', myarr)

    arrayDancers=[None]* myarr[0]
    for i in range(len(arrayDancers)):
        arrayDancers[i]=i+1
    #print 'array of dancers',arrayDancers
    for i in range(myarr[2]%myarr[0]):
        #print('round',i)

        if arrayDancers[0]%2 == 0: # even dancer
            swap_even()
        else: swap_odd()

    #find left and right of the target dancer
    lengtharray= len(arrayDancers)
    inde= arrayDancers.index(myarr[1])
    output_large= file('B-out-large.txt','a+')

    if inde+1>lengtharray-1:
            print'Case #',x+1,':', arrayDancers[0], arrayDancers[inde-1%(len(arrayDancers)-1)]
            output_large.write("Case #"+str(x+1)+': '+ str(arrayDancers[0])+' '+ str(arrayDancers[inde-1%(len(arrayDancers)-1)]) +"\n")
    elif inde-1<0:
            print'Case #',x+1,':', arrayDancers[inde+1%(len(arrayDancers)-1)], arrayDancers[len(arrayDancers)-1]
            output_large.write("Case #"+str(x+1)+': '+ str(arrayDancers[inde+1%(len(arrayDancers)-1)])+' '+ str(arrayDancers[len(arrayDancers)-1]) +"\n")

    else:
            print'Case #',x+1,':', arrayDancers[inde+1%(len(arrayDancers)-1)], arrayDancers[inde-1%(len(arrayDancers)-1)]
            output_large.write("Case #"+str(x+1)+': '+ str(arrayDancers[inde+1%(len(arrayDancers)-1)])+' '+str(arrayDancers[inde-1%(len(arrayDancers)-1)])+"\n")


    #print(inde,'array is now:',arrayDancers,'index of target dancer', r[1])
    #print'Case #',x+1,':', arrayDancers[inde+1%(len(arrayDancers)-1)], arrayDancers[inde-1%(len(arrayDancers)-1)]
    #output_large= file('B-out-small.txt','a+')
    #output_large.write("Case #"+str(x+1)+':'+ result+"\n")
