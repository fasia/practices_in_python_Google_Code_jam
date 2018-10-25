__author__ = 'fsiavash'

myinput= open('B-small-practice.in','r')

myinput2= open('B-large-practice.in', 'r')
output_large= file('B-out-large3.txt','a+')

def dance():
        if k%2==0: #dancer with even number
            #afterdance[(arrayDancers.index(target)-moves)%d]=target # n counterclockwise moves
            #print after
            #index=afterdance.index(target)
            righti= (((k-1)%d-m)%d)+1
            lefti= (((k+1)%d-m)%d)+1

        else: #dancer is odd
            righti= (((k-1)%d+m)%d)+1
            lefti= (((k+1)%d+m)%d)+1

        return lefti, righti
    #print('after dance:', after)

tests= myinput2.readline().strip('\n')
#print('number of tests', tests)
for x in range(int(tests)):
    myarr = []
    for s in myinput2.next().split():
         myarr.append(int(s))
    k=myarr[1]
    d = myarr[0]
    m= myarr[2]%d # reduce number of moves by modulo
    left, right = dance()
    # if target%2 != 0:
    #     l=((target - 2 + 2 * moves) % d) + 1
    #     r=((target + 2 * moves) % d) + 1
    #     print "solution given for odd number dancer is:", l, r



    print'Case #',x+1,':', left, right
    output_large.write('Case #'+str(x+1)+': '+str(left)+' '+ str(right)+'\n')
