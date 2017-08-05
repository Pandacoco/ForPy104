#coding=utf-8

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'white'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

# study drills

#01 修改所有的变量名字
#02 使用更多的格式化字符，比如%r

name = 'Ming'
age = 25
hometown = 'Beijing'
title = 'markeing specialist'
salary = 8000

print "Let's talk about %s." % name
print "He's %d now." % age
print "He's from %s." % hometown
print "He's now a %r, and earn %d every month." % (title, salary)

#03 搜索所有的python格式化字符
    #%%	百分号标记 #就是输出一个%
    #%c	字符及其ASCII码
    #%s	字符串
    #%d	有符号整数(十进制)
    #%u	无符号整数(十进制)
    #%o	无符号整数(八进制)
    #%x	无符号整数(十六进制)
    #%X	无符号整数(十六进制大写字符)
    #%e	浮点数字(科学计数法)
    #%E	浮点数字(科学计数法，用E代替e)
    #%f	浮点数字(用小数点符号)
    #%g	浮点数字(根据值的大小采用%e或%f)
    #%G	浮点数字(类似于%g)
    #%p	指针(用十六进制打印值的内存地址)
    #%n	存储输出字符的数量放进参数列表的下一个变量中
    
#04 将英寸和磅转换成厘米和千克

inchs = 5
lbs = 5
cms = inchs * 2.45
kgs = lbs * 0.454

print "%d 英寸是 %d 厘米." % (inchs, cms)
print "%d 磅是 %d 千克。" % (lbs, kgs)