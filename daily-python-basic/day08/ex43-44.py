# -*- coding: utf-8 -*-
#python2.7
#基本的面向对象的分析和设计
##继承

#大部分使用继承的场合都可以用合成取代，而多级继承则需要不惜一切地避免之。
#python 的继承与C++的不同在于有个super()函数
class Parent(object):
    def altered(self):
        print "PARENT altered()"
        
class Child(Parent):  #继承Parent类
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()    #调用的是父类Parent类的方法
        print "CHILD, AFTER PARENT altered()"
dad = Parent()
son = Child()
dad.altered()
son.altered()

##python的多重继承
#class child(parent,person):

#合成 --类似C++里的友元
# 类似调用一个模块
class Other(object):
    def override(self):
        print "OTHER override()"
    def implicit(self):
        print "OTHER implicit()"
    def altered(self):
        print "OTHER altered()"
class Child(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"
son = Child()
son.implicit()
son.override()
son.altered()
##继承vs合成
# 1. 不惜一切代价地避免多重继承，它带来的麻烦比能解决的问题都多。如果你非要用，那你得准备
# 好专研类的层次结构，以及花时间去找各种东西的来龙去脉吧。 
# 2. 如果你有一些代码会在不同位置和场合应用到，那就用合成来把它们做成模块。 
# 3. 只有在代码之间有清楚的关联，可以通过一个单独的共性联系起来的时候使用继承，或者你受现
# 有代码或者别的不可抗拒因素所限非用不可的话，那也用吧。 