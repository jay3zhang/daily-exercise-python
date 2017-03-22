# -*- coding: utf-8 -*-
#python2.7
#for循环和列表
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number
# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit
# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i
# we can also build lists, first start with an empty one
elements = []
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
# now we can print them out too
for i in elements:
    print "Element was: %d" % i

#如何创建二维列表？
#就是在列表中包含列表，例如这样： [[1,2,3],[4,5,6]]
# 为什么 for-loop 可以使用未定义的变量？
# 循环开始时这个变量就被定义了，当然每次循环它都会被重新定义一次。
# 为什么 for i in range(1, 3): 只循环 2 次而非 3 次？
# range() 函数会从第一个数到最后一个，但不包含最后一个数字。所以它在 2 的时候就停
# 止了，而不会数到 3。这种含首不含尾的方式是循环中及其常见的一种用法。