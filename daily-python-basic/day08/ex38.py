# -*- coding: utf-8 -*-
#python2.7
#列表的操作

# class Thing(object):
    # def test(self,hi):
    # ##class里定义的函数必须有self参数，这是python函数的工作原理。
        # print "hi"
        
# a = Thing()
# a.test('hello')

##
# 以mystuff.append('hello')为例。以下是它的工作原理：
# 1. Python 看到你用到了 mystuff ，于是就去找到这个变量。也许它需要倒着检查看你有没有在
# 哪里用 = 创建过这个变量，或者检查它是不是一个函数参数，或者看它是不是一个全局变量。不
# 管哪种方式，它得先找到 mystuff 这个变量才行。 
# 2. 一旦它找到了 mystuff ，就轮到处理句点 . (period) 这个操作符，而且开始查看 mystuff 
# 内部的一些变量了。由于 mystuff 是一个列表，Python 知道mystuff 支持一些函数。 
# 3. 接下来轮到了处理 append 。Python 会将 “append” 和 mystuff 支持的所有函数的名称
# 一一对比，如果确实其中有一个叫 append 的函数，那么 Python 就会去使用这个函数。 
# 4. 接下来 Python 看到了括号 ( (parenthesis) 并且意识到, “噢，原来这应该是一个函数”，到了
# 这里，它就正常会调用这个函数了，不过这里的函数还要多一个参数才行。 
# 5. 这个额外的参数其实是…… mystuff! 我知道，很奇怪是不是？不过这就是 Python 的工作原
# 理，所以还是记住这一点，就当它是正常的好了。真正发生的事情其实是 
# append(mystuff, 'hello') ，不过你看到的只是 mystuff.append('hello') 

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool!
print '#'.join(stuff[3:5]) # super stellar!



