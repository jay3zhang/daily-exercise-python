# -*- coding: utf-8 -*-
#数字和数学计算

# + plus 加号 
# - minus 减号 
# / slash 斜杠-除
# * asterisk 星号-乘
# % percent 百分号-余数
# < less-than 小于号 
# > greater-than 大于号 
# <= less-than-equal 小于等于号 
# >= greater-than-equal 大于等于号 

print "I will now count my chickens:"
print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
print "Now I will count the eggs:"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print "Is it true that 3 + 2 < 5 - 7?"
print 3 + 2 < 5 - 7
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
print "Oh, that's why it's False."
print "How about some more."
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
#结果
'''
I will now count my chickens:
Hens 30
Roosters 97
Now I will count the eggs:
7
Is it true that 3 + 2 < 5 - 7?
False
What is 3 + 2? 5
What is 5 - 7? -2
Oh, that's why it's False.
How about some more.
Is it greater? True
Is it greater or equal? True
Is it less or equal? False
'''

#python2和python3除法比较
'''
>>> 2/3
0
>>> 2//3
0
>>> 2.0/3
0.6666666666666666
>>> 2.0//3
0.0
#python3
>>> 2/3
0.6666666666666666
>>> 2.0/3
0.6666666666666666
>>> 2//3
0
>>> 2.0//3
0.0
'''

#1.换成浮点数试试
print 2.0+1 #3.0
print 2.0<3 #true
print 2.0==2  #true