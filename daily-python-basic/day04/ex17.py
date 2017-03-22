# -*- coding: utf-8 -*-
#更多文件操作
from sys import argv
from os.path import exists
script, from_file, to_file = argv
print "Copying from %s to %s" % (from_file, to_file)
# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()
print "The input file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
#exists()判断文件是否存在
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
out_file = open(to_file, 'w')
#to_file不存在时，创建一个to_file
print "Does the output file exist? %r" % exists(to_file)
#'w'的意思是清空重写
out_file.write(indata)
print "Alright, all done."
out_file.close()
in_file.close()


# 你写了 indata = open(from_file).read() 这意味着你无需再运行
# `ìn_file.close()`` 了，因为 read() 一旦运行， 文件就会被读到结尾并且被 close 掉。

# Windows的type替代linux的cat
# $ cat copied.txt
# To all the people out there.
# I say I don't like my hair.
# I need to shave it off.
# $