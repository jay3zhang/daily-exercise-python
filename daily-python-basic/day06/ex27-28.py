# -*- coding: utf-8 -*-
#逻辑关系&&布尔表达式练习
# and 与 
# • or 或 
# • not 非 
# • != (not equal) 不等于 
# • == (equal) 等于 
# • >= (greater-than-equal) 大于等于 
# • <= (less-than-equal) 小于等于 
# • True 真 
# • False 假 

##ex28
'''
1. True and True 
2. False and True 
3. 1 == 1 and 2 == 1 
4. "test" == "test" 
5. 1 == 1 or 2 != 1 
6. True and 1 == 1 
7. False and 0 != 0 
8. True or 1 == 1 
9. "test" == "testing" 
10.1 != 0 and 2 == 1 
11."test" != "testing" 
12."test" == 1 
13.not (True and False) 
14.not (1 == 1 and 0 != 1) 
15.not (10 == 1 or 1000 == 1000) 
16.not (1 != 10 or 3 == 4) 
17.not ("testing" == "testing" and "Zed" == "Cool Guy") 
18.1 == 1 and not ("testing" == 1 or 1 == 0) 
19."chunky" == "bacon" and not (3 == 4 or 3 == 3) 
20.3 == 3 and not ("testing" == "testing" or "Python" == "Fun") 
'''
# 为什么 "test" and "test" 返回 "test"， 1 and 1 返回 1，而不是返回 True 呢？
# Python 和很多语言一样，都是返回两个被操作对象中的一个，而非它们的布尔表达式 
# True 或 False 。
False or 1
bool(False or 1)