#coding=utf-8

# 将各个变量罗列出来
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who knows %s and those who %s." % (binary, do_not)

# 打印上方所列出的变量
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# 将各个变量罗列出来
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# 打印上方所列出的变量
print joke_evaluation % hilarious

# 将各个变量罗列出来
w = "This is the left side of ..."
e = "a string with a right side."

# 打印上方所列出的变量
print w+e

# SD

#01 写注释（见上方）

#02 找出“字符串包含字符串”的位置
x = "There are %d types of people." % 10
y = "Those who knows %s and those who %s." % (binary, do_not)
print "I said: %r." % x
print "I also said: '%s'." % y
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious