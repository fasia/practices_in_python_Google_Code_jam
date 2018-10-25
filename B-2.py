__author__ = 'fsiavash'



myarr2= [15, 20, 60, 75, 80, 100]

myarr1= [9, 9, 12, 12, 12, 15, 16, 20]

myinput2= open('A-small-practice.in','r')

myinput1= open('A-large-practice.in', 'r')

def findmatch(a):
  if int(4*a/3) in myarr:
    #result += str(a)
    myarr.remove(int(a*4/3))
    myarr.remove(a)
  return str(a)




myarr = []
result =''
tests= myinput2.readline().strip('\n')
#print('number of tests', tests)
for x in range(int(tests)):
  numbers= myinput2.next().strip('\n') #numbers of items
  #print('numbers:', numbers)
  for s in myinput2.next().split():
    myarr.append(int(s))
  #print(myarr)
  #del myarr
  while len(myarr)>0:
    result+=' '+findmatch(myarr[0])

  print'Case #',x+1,':', result
  output_large= file('out-small.txt','a+')
  output_large.write("Case #"+str(x+1)+':'+ result+"\n")
  result = ''