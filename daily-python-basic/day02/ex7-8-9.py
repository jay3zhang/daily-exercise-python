# -*- coding: utf-8 -*-
###打印，打印
#ex7
# print "Mary had a little lamb."
# print "Its fleece was white as %s." % 'snow'
# #snow是一个字符串而不是变量
# print "And everywhere that Mary went."
# print "." * 10  # what'd that do?  输出10个*
# end1 = "C"
# end2 = "h"
# end3 = "e"
# end4 = "e"
# end5 = "s"
# end6 = "e"
# end7 = "B"
# end8 = "u"
# end9 = "r"
# end10 = "g"
# end11 = "e"
# end12 = "r"
# # watch that comma at the end.  try removing it to see what happens
# #comma 表示在同一行打印
# print end1 + end2 + end3 + end4 + end5 + end6,
# print end7 + end8 + end9 + end10 + end11 + end12

#ex8
# formatter = "%r %r %r %r"
# print formatter % (1, 2, 3, 4)
# print formatter % ("one", "two", "three", "four")
# print formatter % (True, False, False, True)
# print formatter % (formatter, formatter, formatter, formatter)
# print formatter % (
    # "I had this thing.",
    # #"l",
    # "That you could type up right.", 
    # "But it didn't sing.",  #该字符串中存在'，所以打印时用""包住以免混淆
    # "So I said goodnight."  )

# 使用 %s 还是 %r？ 
# 你应该使用 %s，只有在想要获取某些东西的 debug 信息时才能用到 %r。 %r 给你的是变量的“程序员原始版本”
# 字符中包含了中文（或者其它非 ASCII 字符），可是 %r 打印出的是乱码？ 
# 使用 %s 就行了。 

#ex9
# Here's some new strange stuff, remember type it exactly.
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print "Here are the days: ", days
# print 里的逗号分隔参数
print "Here are the months: %r" % months
# 为什么使用 %r 时 \n 新行就不灵了？ 
#%r 就是这个样子，它打印出的是你写出来的方式（或者近似方式）。它是用来 debug 的原始格式。 
print "Here are the months: ", months
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
