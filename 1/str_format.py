age =20
name='Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name,age))
print('why is {0} playing with that python'.format(name))
print(name+' is '+str(age)+' years old')


print('{} was {} years old when he wrote this book'.format(name,age))
print('why is {} playing with that python'.format(name))
#保留小数点(.)后三位
print('{0:6f}'.format(11/3))
#使用下划线填充文本，并保持文字处于中间位置
# #	使用(^)定义'___hello___'字符串长度为	12
print('{0:_^12}'.format('hello'))
#基于关键词输出'Swaroop wrote A Byte of	Python'
print('{name} wrote {book}'.format(name='Swaroop',book='A byte of python'))
#print默认以'\n'结尾可以指定end为什么结尾
print('a',end=' ')
print('b',end=' ')

print('what\'s your problem')
print('This is the first line\nThis is the second line')
#在字符串前增加r或R来指定一个原始（Raw）字符串
print(r"NewLines are indicated by \n")
#在一类情况下这一方法会颇为有用：如果你有一行非常长的代码，你可以通过使用反斜杠\将其拆分成多个物理行。这被称作显式行连接（Explicit	Line Joining)
