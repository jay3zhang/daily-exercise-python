# coding=utf-8

# from pythonds.basic.stack import Stack

# 中缀表达式（正常表达式）转后缀，前缀原理相同，略
# eg. A + B -> A B +

def infix_to_postfix(infix):
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXTZ'+'0123456789'
    opstack = Stack()
    
    postfix_list = []
    taglist = infix.split()
    for tag in taglist:
        if tag in digits:
            postfix_list.append(tag)
        elif tag=='(':
            opstack.push(tag)
        elif tag==')':
            item = opstack.pop()
            while not item=='(':
                postfix_list.append(tag)
                item = opstack.pop()
        elif tag in '+-/*':
            
        
        

# 后缀计算

