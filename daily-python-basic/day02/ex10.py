# -*- coding: utf-8 -*-
#转义字符
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#\b--退格符
# %r 打印出来的是你作为程序员写在脚本里的东西，而 %s 打印
# 的是你作为用户应该看到的东西。 
formatter = "%r %r %r %r"
print formatter % (tabby_cat,
    persian_cat,
    backslash_cat,
    fat_cat)