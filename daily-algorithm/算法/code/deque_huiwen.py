# coding=utf-8

from pythonds.basic.deque import Deque

def palchecker(str):
    wordDeque = Deque()
    for word in str:    #所有字母入队列
        wordDeque.addRear(word)
        
    Equal = True
    while wordDeque.size()>1 and Equal:
        # 队首，队尾各出一个字母依次比较
        first = wordDeque.removeFront()
        last = wordDeque.removeRear()
        if first!=last:
            Equal = False
    
    return Equal
    
print(palchecker("lsdkjfskf"))
print(palchecker("radar"))