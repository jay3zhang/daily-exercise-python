
# O(n^2)
def findMin1(alist):
	min = alist[0]
	for i in alist:
		issmallest = True
		for j in alist:
			if i > j:
				issmallest = False
		if issmallest:
			min = i
	return min

#O(n)
def findMin2(alist):
	minsofar = alist[0]
	for i in alist:
		if i<minsofar:
			minsofar = i
	return minsofar
 
# print('findMin1------') 
# print(findMin1([5,4,2,0,1]))
# print(findMin1([1,3,2,0,5]))

# print('findMin2------') 
# print(findMin2([5,4,2,0,1]))
# print(findMin2([1,3,2,0,5]))

import time
from random import randrange
def test(func):
    for listsize in range(1000,10001,1000): # 从1000到10000，间隔为1000
        alist = [randrange(100000) for x in range(listsize)]
        # '''
        # 产生listsize个大小在0-100000之间的数
        # 相当于
            # for x in range(listsize):
                # randrange(100000)
        # '''
        start = time.time()
        print(func(alist))
        end = time.time()
        print('size:%d,time:%f'%(listsize,end-start))
    
test(findMin1)
#test(findMin2)
