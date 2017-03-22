# -*- coding: utf-8 -*-
#函数可以返回东西
def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b
def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b
def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b
def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
print "Let's do some math with just functions!"
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"

# 来个简单的例子吧： 24 + 34 / 100 - 1023 ——把它用函数的形式写出来。然后自己想
# 一些数学式子，像公式一样用变量写出来。