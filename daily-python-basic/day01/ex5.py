# -*- coding: utf-8 -*-
#更多的变量和打印--格式化字符串
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth
# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)
    
#%r--不管什么格式都打印出来
# 如何将浮点数四舍五入？ 
# 你可以使用 round() 函数，例如： round(1.7333)
print round(1.52)

#使用变量将英寸和磅转换成厘米和千克
inch = 10
cm = inch*2.54  #1inch=2.54cm
lb = 10
kg = lb*0.4535924   #1lb=0.4535924kg