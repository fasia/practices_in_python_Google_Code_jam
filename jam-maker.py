__author__ = 'fsiavash'


myinput2= open('B-large.in','r')


def findmatch(a):
  if int(4*a/3) in myarr:
    #result += str(a)
    myarr.remove(int(a*4/3))
    myarr.remove(a)
  return str(a)


output_large= file('out-B-large.txt','a+')

result =''
tests= myinput2.readline().strip('\n')
#print('number of tests', tests)
for x in range(int(tests)):
  numbers= myinput2.next().strip('\n') #numbers of items
  #print('numbers:', numbers)
  myarr = []
  for s in myinput2.next().split():
    myarr.append(float(s))
  #print(myarr)

  myarr.sort()
  totalprob =1
  for i in range(len(myarr)/2):
     totalprob *= 1- (myarr[i]*myarr[len(myarr)-1-i])
  output_large.write("Case #"+str(x+1)+': '+ str(totalprob)+"\n")
  del myarr
  # while len(myarr)>0:
  #   result+=' '+findmatch(myarr[0])
  #
  # print'Case #',x+1,':', result

  # result = ''