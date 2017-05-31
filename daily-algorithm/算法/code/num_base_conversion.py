# coding=utf-8

# 16进制内的互相转换
#from pythonds.basic.stack import Stack

# 定义栈类
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

## 10进制->2进制
def conver_to_2(num):
    remstack = Stack()  #存放余数的栈
    
    while num>0:    # num大于0时，不断除于2，余数入栈
        rem = num % 2
        remstack.push(rem)
        num = num / 2
    
    tostr = ''
    while not remstack.isEmpty():
        tostr = tostr + str(remstack.pop()) #将栈中的余数拼接在一起
    # 小于10进制可以返回int，但大于10进制的数(如，16进制数1D5A)不能返回int，所以一律返回str类型   
    return tostr
    
def ten_converto_x(num,n):
    # 10进制转n进制
    # 可以加个判断看n是否符合条件
    digits = '0123456789ABCDEF' #可能出现的所有字符
    remstack = Stack()
    while num>0:
        rem = num % n
        remstack.push(rem)
        num = num / n

    tostr = ''
    while not remstack.isEmpty():
        tostr = tostr + digits[remstack.pop()]
        
    return tostr

def y_converto_ten(num,n):
    # n进制转10进制(n<=16)
    digits = '0123456789ABCDEF' #可能出现的所有字符
    strstack = Stack()
    
    for item in list(str(num)): #将n进制数的每一位转换为str入栈
        strstack.push(item)
    
    tonum = 0
    i = 0
    while not strstack.isEmpty():
        # n**i是n的i次方，index()返回位置索引，int类型
        tonum = tonum + digits.index(strstack.pop()) * (n**i)
        i = i+1
        
    return tonum

def y_converto_x(y,num,x):
    # n进制转m进制，先转为10进制再转为目标进制
    temp = y_converto_ten(num,y)
    tostr = ten_converto_x(temp,x)
    return tostr

# 涉及字母的输入要用str类型
# print(ten_converto_x(10,8))    
# print(y_converto_ten('1A',16)) 
# print(y_converto_x(2,1010,8))
