# -*- coding: utf-8 -*-
#python2.7
#分支和函数
from sys import exit

def gold_room():
    print "This room is full of gold.  How much do you take?"
    next = raw_input("> ")
    #if "0" in next or "1" in next:
    if int(next):
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")
    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
        '''
        exit(0) 有什么功能？
        在很多类型的操作系统里，`èxit(0)`` 可以中断某个程序，而其中的数字参数则用来表示程
        序是否是碰到错误而中断。 exit(1) 表示发生了错误，而 exit(0) 则表示程序是正常
        退出的。这和我们学的布尔逻辑 0==False 正好相反，不过你可以用不一样的数字表示不
        同的错误结果。比如你可以用 exit(100) 来表示另一种和 exit(2)` 或 exit(1) 不同
        的错误。
        '''
    else:
        dead("You greedy bastard!")
def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False
    while True:
        next = raw_input("> ")
        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."
def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
def dead(why):
    print why, "Good job!"
    exit(0)
def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"
    next = raw_input("> ")
    if next == "l":
        bear_room()
    elif next == "r":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
start()