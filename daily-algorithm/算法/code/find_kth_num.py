# coding=utf-8

# 寻找随机数列中第 k 小的数

# O(nlogn)
# 先排序，然后找到第K小的数
def find_kth(k,s):
    alist = list(s)
    alist.sort()
    
    if len(alist)<k:
        return 0
        
    return alist[k-1]


# O(n)
