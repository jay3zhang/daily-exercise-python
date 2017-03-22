# -*- coding: utf-8 -*-
#字符串和文本
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print x
print y
print "I said: %r." % x
#区别字符串中的%s与'%s'
#%s表示同一个字符串
#'%s'表示字符串中的字符串
print "I also said: %s." % y    #I also said: Those who know binary and those who don't..
print "I also said: '%s'." % y  #I also said: 'Those who know binary and those who don't.'.
#注意下面这种用法
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
#
w = "This is the left side of..."
e = "a string with a right side."
print w + e