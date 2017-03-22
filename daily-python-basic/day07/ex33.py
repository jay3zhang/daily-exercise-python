# -*- coding: utf-8 -*-
#python2.7
#while循环

# 1. 尽量少用 while-loop，大部分时候 for-loop 是更好的选择。 
# 2. 重复检查你的 while 语句，确定你测试的布尔表达式最终会变成 False 。 
# 3. 如果不确定，就在 while-loop 每次结束时打印出你要测试的值，看看它的变化。
i = 0
numbers = []
while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)
    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i
print "The numbers: "
for num in numbers:
    print num

# 1. 将这个 while 循环改成一个函数，将测试条件(i < 6)中的 6 换成一个变量。 
# 2. 使用这个函数重写你的脚本，并用不同的数字进行测试。 
# 3. 为函数添加另外一个参数，这个参数用来定义第 8 行的加值 + 1 ，这样你就可以让它任意加值
# 了。 
# 4. 再使用该函数重写一遍这个脚本。看看效果如何。 
# 5. 接下来使用 for-loop 和 range 把这个脚本再写一遍。你还需要中间的加值操作吗？如果你
# 不去掉它，会有什么样的结果？

# 觉得循环不好理解，很大程度上是因为不会顺着代码的运行方式去理解代码。当循环开始时，
# 它会运行整个区块，区块结束后回到开始的循环语句。如果想把整个过程视觉化，你可以在
# 循环的各处塞入 print 语句，用来追踪变量的变化过程。你可以在循环之前、循环的第一句、
# 循环中间、以及循环结尾都放一些 print 语句，研究最后的输出，并试着理解循环的工作过
# 程。