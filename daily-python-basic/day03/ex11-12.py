# -*- coding: utf-8 -*-

#ex11
# print "How old are you?",   #35
# age = raw_input()  #返回str类型
# print "How tall are you?",  #6'22"
# height = raw_input()
# print "How much do you weigh?", #72.2
# weight = raw_input()
# #注意%r与%s的区别
# print "So, you're %r old, %r tall and %r heavy." % (
    # age, height, weight)
# print "So, you're %s old, %s tall and %s heavy." % (
    # age, height, weight)
    
# input() 和 raw_input() 有何不同？ 
# input() 函数会把你输入的东西当做 Python 代码进行处理，这么做会有安全问题，你应该避开
# 这个函数。

#ex12
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")
print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
    
# 1.在命令行界面下运行你的程序，然后在命令行输入 pydoc raw_input 看它说了些什么。如
# 果你用的是 Window，那就试一下 python -m pydoc raw_input 。 
# 2. 输入 q 退出 pydoc。 
# 3. 上网找一下 pydoc 命令是用来做什么的。 
# 4. 使用 pydoc 再看一下 open, file, os, 和 sys 的含义。看不懂没关系，只要通读一下，记下
# 你觉得有意思的点就行了。 