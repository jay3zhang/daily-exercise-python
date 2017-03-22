# -*- coding: utf-8 -*-
#基本打印
print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'
#1.让你的脚本再多打印一行。 
print '\n'
#2. 让你的脚本只打印一行
#\r与，
print "Hello World!\r",
print "Hello Again"

import math
import time
i=1
while i<4:
    print '%d\r' % i,
    time.sleep(1)
    i=i+1
print i