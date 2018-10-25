__author__ = 'fsiavash'

import math
myinput2= open('C-small-practice.in','r')

arr=[['OOOOO','OOOOO','OOOOO','OOOOO','OOOOO'],#num0
    ['OOOOO','OOOOO','OOI/O','OOOOO','OOOOO'],           #1
     ['OOOOO','OOOOO','O/I/O','OOOOO','OOOOO'],             #2
     ['OOOOO','OOOOO','O/I/O','OO/OO','OOOOO'],#           3
     ['OOOOO','OO/OO','O/I/O','OO/OO','OOOOO'],
     ['OOOOO','O//OO','O/I/O','OO/OO','OOOOO'],
     ['OOOOO','O/O/O','O/I/O','O/O/O','OOOOO'],
     ['OOOOO','O///O','O/I/O','O/O/O','OOOOO'],
     ['OOOOO','O///O','O/I/O','O///O','OOOOO']]

output_large= file('out-io.txt','a+')
tests= myinput2.readline().strip('\n')
#print('number of tests', tests)
for x in range(int(tests)):
    fr= myinput2.next().strip('\n') #numbers of friends
    line1 = fr.split()
    f= int(line1[0])
    s= int(line1[1])
    print f , s
    d,r = divmod(s,8)     # how many full blocks of 8 + what is remaining number of the last block
    rowsOfBlock,remaining=divmod(d,8) # how many rows of full blocks of 8?    + how many single blocks of 8
    print d,r, rowsOfBlock, remaining
    result=''
    paddingBlocks=0
    for x in range(rowsOfBlock): # filling the rows of blocks of 8 I/O
            print 'in if'
            for y  in range(5): # 0 to 5 = 6 rows in a block
                for z in range(8):
                    result+= arr[8][y]
                result +='\n'
    if rowsOfBlock>0:
        paddingBlocks=8-(remaining+1) # how many zero blocks should be added to make the grid
        print paddingBlocks
    for y in range(5): # 6 rows in a block
        for a in range(remaining): # remaining blocks of 8 I/O should be added
            print 'in single blocks'
            result += arr[8][y]
        for bb in range(1):
            print 'in  non-full blocks'
            result += arr[r][y]
        if paddingBlocks>0:
            for cc in range(paddingBlocks): # padding the row of block with zeros to make the grid rectangular
                print 'in padding blocks'
                result += arr[0][y]
        result+='\n'

    print result
    output_large.write("Case #"+str(x+1)+': \n'+ str(result))










    # blockDi=  int(math.ceil(math.sqrt(d+1)))
    # b = [[arr[0] for ee in range(blockDi-1)]for y in range(blockDi-1)]
    #
    # print d, r, blockDi
    # row =''
    # counter=0
    # result=''
    # for x in range(blockDi):
    #     if counter<=d:
    #         print 'in if'
    #         for y  in range(5):
    #             counter +=1
    #             for z in range(blockDi):
    #                 result+= arr[len(arr)-1][y]
    #             result +='\n'
    #         counter +=1
    #
    #     elif counter == d+1:
    #         print 'in 1st else'
    #         for y  in range(5):
    #             counter +=1
    #             for z in range(blockDi):
    #                 print arr[r-1][y],
    #             print
    #         counter +=1
    #     elif counter >d+1:
    #         print 'in 2nd else'
    #         for y  in range(5):
    #             counter +=1
    #             for z in range(blockDi):
    #                 print arr[0][y],
    #             print
    #         counter +=1
    #
    #     print counter
    # print result
    #
    #
    #
    #




        # ticket=[]
        # for i in range(f):
        #     temp= (myinput2.next().strip('\n') )
        #     ticket.append(temp.split())
        #print 't',ticket

        #s = myinput2.next().strip('\n') # seats row-col
        #print fr, s


        #maxim *= 1- (myarr[i]*myarr[len(myarr)-1-i])
        #output_large.write("Case #"+str(x+1)+': '+ str(result)+"\n")
        # while len(myarr)>0:
        #   result+=' '+findmatch(myarr[0])
        #
        # print'Case #',x+1,':', result

        # result = ''