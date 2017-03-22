# -*- coding: utf-8 -*-
#读写文件
# from sys import argv
# script, filename = argv
filename=raw_input("filename:>")
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
raw_input("?")
print "Opening the file..."
target = open(filename, 'w')
# print "Truncating the file.  Goodbye!"
# target.truncate()
print "Now I'm going to ask you for three lines."
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")
print "I'm going to write these to the file."
# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")
target.write(line1+"\n"+line2+"\n"+line3+"\n")
print "And finally, we close it."
target.close()

#如果用 'w' 模式打开文件，那么不需要 target.truncate()
# 'w' 是什么意思？ 
# 它只是一个特殊字符串，用来表示文件的访问模式。如果你用了 'w' 那么你的文件就是写入
# (write)模式。除了 'w' 以外，我们还有 'r' 表示读取（read）， 'a' 表示追加(append)。