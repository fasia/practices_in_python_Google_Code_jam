__author__ = 'fsiavash'


myinput2= open('A-large.in','r')


output_large= file('out-B.txt','a+')

tests= myinput2.readline().strip('\n')
#print('number of tests', tests)
for x in range(int(tests)):
    fr= myinput2.next().strip('\n') #numbers of friends
    line1 = fr.split()
    f= int(line1[0])
    s= int(line1[1])
    print f , s
    ticket=[]
    for i in range(f):
        temp= (myinput2.next().strip('\n') )
        ticket.append(temp.split())
    #print 't',ticket

    #s = myinput2.next().strip('\n') # seats row-col
    #print fr, s
    myarr = [[0 for ee in range(s)]for y in range(s)]
    maxim =0
    for j in ticket:
        myarr[int(j[0])-1][int(j[1])-1] =1
        myarr[int(j[1])-1][int(j[0])-1] =1

    max=0
    result=0
    for i in range(s):
        max= sum(myarr[i][:])
        if max>result:
            result=max
    print result
            #maxim *= 1- (myarr[i]*myarr[len(myarr)-1-i])
    output_large.write("Case #"+str(x+1)+': '+ str(result)+"\n")
    del myarr
    # while len(myarr)>0:
    #   result+=' '+findmatch(myarr[0])
    #
    # print'Case #',x+1,':', result

    # result = ''