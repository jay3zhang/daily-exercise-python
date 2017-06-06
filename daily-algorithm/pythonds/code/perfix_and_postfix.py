# coding=utf-8

# 默认所有输入都符合规范，只有字母，数字，+-*/，没有负数

from pythonds.basic.stack import Stack

# 中缀表达式（正常表达式）转后缀，前缀原理相同，略
# eg. A + B -> A B +

def infix_to_postfix(infix):
    digits = 'ABCDEFGHIJKLMNOPQRSTUVWXTZ'+''.join([str(_) for _ in range(0,100)])
    
    prec = {}   #存放运算符的优先级
    prec['**'] = 4  #幂次方
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1
    # 左括号将赋予最低的值。这样，与其进行比较的任何运算符将具有更高的优先级，将被放置在它的顶部。
    opstack = Stack()
    postfix_list = []
    taglist = infix.split()     # 将输入的表达式分割为单个字符 
    
    for tag in taglist:
        if tag in digits:
            postfix_list.append(tag)
        elif tag=='(':
            opstack.push(tag)
        elif tag==')':
            item = opstack.pop()
            while not item=='(':    #抛出括号内的所有运算符
                postfix_list.append(item)
                item = opstack.pop()
        else:     #抛出优先级大于等于自己的运算符
            while (not opstack.isEmpty()) and (prec[opstack.peek()] >= prec[tag]):
                postfix_list.append(opstack.pop())
            # 将自己放入栈中
            opstack.push(tag)
        
    while not opstack.isEmpty():
        postfix_list.append(opstack.pop())
        
    return ' '.join(postfix_list)
        
# 后缀计算
def postfix_Eval(postfix):
    digits = ''.join([str(_) for _ in range(0,100)])
    
    operandStack = Stack()
    taglist = postfix.split()
    
    for tag in taglist:
        if tag in digits:     #将操作数压入栈中
            operandStack.push(int(tag))
        else:               # 遇到操作符则弹出两个操作数（后缀）
            op1 = operandStack.pop()    # 这是后面的
            op2 = operandStack.pop()    #这是操作符前面的数字
            result = domath(op1,op2,tag)
            operandStack.push(result)
            
    return operandStack.pop()

def domath(op1,op2,opsymbol): 
    if opsymbol=='+':
        return op2+op1
    elif opsymbol=='-':
        return op2-op1
    elif opsymbol=='*':
        return op2*op1
    else:
        return op2/op1    #一定要搞清楚除法和减法的操作数顺序，3-5和5-3不同
 
## 测试 
# print(infix_to_postfix('A * B + C * D'))
# print(infix_to_postfix('10 + 3 * 5 / ( 16 - 4 )'))
print(infix_to_postfix('5 * 3 ** ( 4 - 2 )'))
# print(infix_to_postfix('( A + B ) * ( C + D )'))
# print(infix_to_postfix('( A + B ) * C - ( D - E ) * ( F + G )'))

print('-'*10)
# print(postfix_Eval('7 8 + 3 2 + /'))
print(postfix_Eval('17 10 + 3 * 9 /'))