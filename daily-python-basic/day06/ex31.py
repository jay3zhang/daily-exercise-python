# -*- coding: utf-8 -*-
#python2.7
#if判断练习
print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"
door = raw_input("> ")
if door == "1":
    print "There's a giant bear here eating a cheese cake.  What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    bear = raw_input("> ")
    if bear == "1":
        print "The bear eats your face off.  Good job!"
    elif bear == "2":
        print "The bear eats your legs off.  Good job!"
    else:
        print "Well, doing %s is probably better.  Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    insanity = raw_input("> ")
    
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello.  Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck.  Good job!"
else:
    print "You stumble around and fall on a knife and die.  Good job!"
    
    
##
# 可以用多个 if/else 来取代 elif 吗？
# 有时候可以，不过这也取决于额 if/else 是怎样写的，而且这样一来 python 就需要去
# 检查每一处 if/else，而不是像 if/elif/else 一样，只要检查到第一个 True 就
# 可以停下来了。试着写些代码看两者有何不同。
# 怎样判断一个数字处于某个值域中？
# 两个办法：经典语法是使用 1 < x < 10，或者用 x in range(1, 10) 也可以。
# 怎样用 if/elif/else 区块实现四个以上的条件判断？
# 简单，多写几个 elif 区块就可以了。