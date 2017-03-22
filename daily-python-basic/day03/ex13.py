# -*- coding: utf-8 -*-
#参数、解包、变量
from sys import argv
# script, first, second, third = argv
# script, first, second = argv
script, first, second, third,forth = argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "Your forth variable is:", forth
# 再写两个脚本，其中一个接受更少的参数，另一个接受更多的参数，在参数解包时给它们取一些
# 有意义的变量名。 