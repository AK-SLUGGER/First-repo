Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=12
id(x)
2889179923024
a=[1,2,'a'.True]
SyntaxError: invalid syntax
a=[1,2,'a',True]
a.remove('a')
a
[1, 2, True]
a.append(True)
a.append(True)
a
[1, 2, True, True, True]
a.remove(True)
a
[2, True, True, True]
True
True
b=[1,2,33,33,44]
b=[1,2,33,33,44,33]
b.remove(33)
b
[1, 2, 33, 44, 33]
dir([])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
help(b.remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

"Hello".index('H')
0
"Hello".index('i')
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    "Hello".index('i')
ValueError: substring not found
"Hello".index('l')
2

================================ RESTART: Shell ================================
b=[1,2,33,33,44,33]
b.index()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b.index()
TypeError: index expected at least 1 argument, got 0
b.index(33)
2
b.count(33)
3
del b[4]
b
[1, 2, 33, 33, 33]
help(b.insert)
Help on built-in function insert:

insert(index, object, /) method of builtins.list instance
    Insert object before index.

b.insert(5,'abc')
b
[1, 2, 33, 33, 33, 'abc']
b.insert(2,'abcd')
b
[1, 2, 'abcd', 33, 33, 33, 'abc']
"python"
'python'
s=list[Python]
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s=list[Python]
NameError: name 'Python' is not defined
s=list("Python")
s
['P', 'y', 't', 'h', 'o', 'n']
len(s)
6
len("python")
6
c="python"
c[0]==s[0]
False
c[2]==s[2]
True
c[2] is s[2]
True
id(c[2])
2051580019952
id(s[2])
2051580019952
#You can edit a list but you cant edit a string
c[0]="e"
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    c[0]="e"
TypeError: 'str' object does not support item assignment
s[0]='e'
help(list)

x=list
x
<class 'list'>
x==[]
False
#x is a constructor here
"a;b;c"  #'a' 'b' 'c'
'a;b;c'
'a;b;c'.split(';')
['a', 'b', 'c']
'a;b;c,d;oo'.split(';')
['a', 'b', 'c,d', 'oo']
'a;b;c,d;oo'.split(',')
['a;b;c', 'd;oo']
'a;b;c,d;oo'.split('o')
['a;b;c,d;', '', '']
'a;b;c,d;o'.split('o')
['a;b;c,d;', '']
'a;b;c,d;oo'.split(';oo')
['a;b;c,d', '']
'a;b;c,d;oop'.split('oo')
['a;b;c,d;', 'p']
'a;b;c,d;oop'.split('o')
['a;b;c,d;', '', 'p']
"a b c d".split()
['a', 'b', 'c', 'd']
"a b cd".split()
['a', 'b', 'cd']
 #  and or not
 
True & False # 2 data types in boolean
False
# and
a and b
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    a and b
NameError: name 'a' is not defined
False and True
False
False and False
False
True and True
True
(2>3) and (4<5)
False
q=2 >3
q
False
w=4<5
>>> w
True
>>> False and True
False
>>> (2<3) and (4<5)
True
>>> False or False
False
>>> False or True
True
>>> True or True
True
>>> True or False
True
>>> (2>3) or (4<5)
True
>>> (2>3) and (4>5)
False
>>> not (2>3)
True
>>> not True
False
>>> not False
True
>>> # not will reverse
>>> True and not False
True
>>> True  == True
True
>>> False == False
True
>>> not True ==False
True
>>> False == not True
SyntaxError: invalid syntax
>>> not True == False
True
>>> False == (not True)
True
