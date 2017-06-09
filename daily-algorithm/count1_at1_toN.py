
# -*- coding:utf-8 -*-
# 1到N的整数中1出现的次数
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        res=0
        tmp=n
        base=1
        while tmp:
            last=tmp%10
            tmp=tmp/10
            res+=tmp*base
            if last==1:
                res+=n%base+1
            elif last>1:
                res+=base
            base*=10
        return res
        
        
def NumberOf1Between1AndN2(self, n):
        ones, m = 0, 1
        while m <= n:
            if ((n // m) % 10) != 0 and ((n // m) % 10) != 1:
                ones += (n // 10 // m + 1) * m
            elif ((n // m) % 10) == 1:
                ones += (n // m // 10) * m + n % m + 1
            m *= 10
        return ones