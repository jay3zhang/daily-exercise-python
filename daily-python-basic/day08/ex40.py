# -*- coding: utf-8 -*-
# python2.7
# 模块、类、对象

##模块和字典差不多
#Python 里边有这么一个通用的模式：
# 1. 拿一个类似 key=value 风格的数据容器 
# 2. 通过 key 的名称获取其中的 value 
# 对于字典来说，key 是一个字符串，获得值的语法是 [key] 。对于模块来说，key 是函数或者变量的名
# 称，而语法是 .key 。除了这个，它们基本上就没什么区别了。
##模块和类差不多
##对象相当于迷你版的 import
class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])
bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

