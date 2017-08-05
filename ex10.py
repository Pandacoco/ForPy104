#coding=utf-8

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

#SD

#01 可用的转义字符
    
# \a 响铃；\b 退格；\000 空；\v 纵向制表符；\r 回车；\f 换页

a = "\a I'm handsome."
b = "I'm \bhandsome."
c = "I'm \000 handsome."
d = "I'm \f handsome."
e = """
I'm
\v@ Handsome
\v@ Cool
\v@ Easygoing
\v@ Gentle 
"""

print a
print b
print c
print d
print e

#02 使用'''三个单引号取代三个双引号

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print fat_cat 
# 跟三个双引号效果一样

#03 将转义序列和格式化字符串放到一起，创建一种更复杂的格式。

do = "I'll do a list:"
good = "\t* %s\n\t* %s\n\t* %s\n\t* %s"

print do 
print good % ("Catfood", "Fishes", "Catnip", "Grass")


