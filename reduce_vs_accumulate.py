import itertools
lis = [1,3,4,10,4]
print ("The summation of list using accumulate is :") 
print (list(itertools.accumulate(lis,lambda x,y : x+y))[-1]) 
