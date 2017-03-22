# -*- coding: utf-8 -*-
#函数和文件
# from sys import argv
# script, input_file = argv
input_file = raw_input("filename:>")
def print_all(f):
    print f.read()
def rewind(f):
    f.seek(0)
def print_a_line(line_count, f):
    print line_count, f.readline()
current_file = open(input_file)
print "First let's print the whole file:\n"
print_all(current_file)
#打印结束后光标已移至文件末尾
print "Now let's rewind, kind of like a tape."
#seek(0)重新将光标定位到文件开始
rewind(current_file)
print "Let's print three lines:"
current_line = 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)
current_line = current_line + 1
print_a_line(current_line, current_file)

# 为什么文件里会有间隔空行？ 
# readline() 函数返回的内容中包含文件本来就有的 \n，而 print 在打印时又会添加一个 
# \n，这样一来就会多出一个空行了。解决方法是在 print 语句结尾加一个逗号 ,，这样 print 就
# 不会把它自己的 \n 打印出来了。 
# readline() 是怎么知道每一行在哪里的？ 
# readline() 里边的代码会扫描文件的每一个字节，直到找到一个 \n 为止，然后它停止读取
# 文件，并且返回此前的文件内容。文件 f 会记录每次调用 readline() 后的读取位置，这样它
# 就可以在下次被调用时读取接下来的一行了。