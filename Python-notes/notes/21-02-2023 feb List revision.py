Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 ###List Revision
###21-02-2023

a=['coffee','tea','milk']
b=['carrot','brinjal','potato']
b.append('tomato')
b
['carrot', 'brinjal', 'potato', 'tomato']
lan(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    lan(a)
NameError: name 'lan' is not defined. Did you mean: 'len'?
len(a)
3
len(b)
4
a==b
False
a is b
False
#Identity , value ,type
a == b # checking value equality
False
a is  b # id eq
False
id(a)
2189957768960
id(b)
2189957764032
a2=['coffee','tea','milk']
id(a2)
2189957770752
a==a2
True
a is a2
False
s == a
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    s == a
NameError: name 's' is not defined
a==s
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a==s
NameError: name 's' is not defined
# slicing
s
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s
NameError: name 's' is not defined
a
['coffee', 'tea', 'milk']
a[1:3]
['tea', 'milk']
a[2]
'milk'
a[[1]

KeyboardInterrupt
a[1]
  
'tea'
a=['coffee','tea','milk']
  
a[len(a)-1]
  
'milk'
len(a)-1
  
2
a[-1]
  
'milk'
a[-len(a)]
  
'coffee'
s[:]
  
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    s[:]
NameError: name 's' is not defined

a[:]
  
['coffee', 'tea', 'milk']
a[-2:-3]
  
[]
s[-2:]
  
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    s[-2:]
NameError: name 's' is not defined
a[-2:]
  
['tea', 'milk']
s=['coffee','tea','milk','Mango']
  
s[-3:]
  
['tea', 'milk', 'Mango']
s[0:4]
  
['coffee', 'tea', 'milk', 'Mango']
s[0:4:2]
  
['coffee', 'milk']
#(0,0+2=2)
  
s[:-2]
  
['coffee', 'tea']
s[:-4]
  
[]
s[-len(s):]
  
['coffee', 'tea', 'milk', 'Mango']
s[-len(s)::-1]
  
['coffee']
s[:]
  
['coffee', 'tea', 'milk', 'Mango']
s[::-1]
  
['Mango', 'milk', 'tea', 'coffee']
# Reverse the list
  
s[-len(s)::-1]
  
['coffee']
s
  
['coffee', 'tea', 'milk', 'Mango']
s[:-3]
  
['coffee']
s[:-100]
  
[]
len(s)
  
4
s[0]
  
'coffee'
s[len(s)-1]
  
'Mango'
s[-len(s)]
  
'coffee'
s[3]
  
'Mango'
s[1:3]
  
['tea', 'milk']
s[1]
  
'tea'
s[2]
  
'milk'
s[1:3:2]
  
['tea']
#1,1+2 || condition is <3
  
x=[i for i in range(101)]
  
x
  
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
x[:]
  
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
x[::2]
  
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
x[::3]
  
[0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66, 69, 72, 75, 78, 81, 84, 87, 90, 93, 96, 99]
x[:20:2]
  
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
x.index(18)
  
18
x.index(20)
  
20
# All elements start index  0 , ends before 20, step =2=>consider every second element
  
##All elements starts index 0,ends 20::>0,2,4,6,.......
  
x=[i=1 for i in range(101)]
  
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
x=[i+1 for i in range(101)]
  
x
  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
len(x)
  
101
x[:10]
  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x[1:10]
  
[2, 3, 4, 5, 6, 7, 8, 9, 10]
x[1:10:2]
  
[2, 4, 6, 8, 10]
x
  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
x[-5]
  
97
x[-2]
  
100
x[-5:-2]
  
[97, 98, 99]
x[-5:-1]
  
[97, 98, 99, 100]
x.index(97)
  
96
x.index(100)
  
99
len(x)-x.index(97)
  
5
len(x)-x.index(100)
  
2
x[-5:-1]==x[len(x)-5:len(x)-1]
  
True
x[-5:-1]==x[len(x)-5:len(x)-2]
  
False
x
  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
id(x)
  
2189957871872
id(x[:])
  
2189958037760
c=x[:]
  
id(c)
  
2189958038720
y=x
  
y is x
  
True
c is x
  
False
d=[[1,2],'a','d']
  
e=d
  
g=d[:]
  
e is d
  
True
g is d
  
False
g[0] is d[0]
  
True
g[0] .append('hey')
  
g
  
[[1, 2, 'hey'], 'a', 'd']
d
  
[[1, 2, 'hey'], 'a', 'd']
e
  
[[1, 2, 'hey'], 'a', 'd']
id(g[0])
  
2189958037760
id(d[0])
  
2189958037760
'a' in d
  
True
'f' in d
  
False
'f' not in d
  
True
x[:-len(x)+1]
  
[1]
type(x[:-len(x)+1])
  
<class 'list'>
'str'[:2]
  
'st'
q=['w',1,(1,2)]
  
q[0]
  
'w'
type(q[0])
  
<class 'str'>
type(q[0:1])
  
<class 'list'>
q[0:1]
  
['w']
w=[[1,2],['a','b']]
  
w[0]
  
[1, 2]
w[0][0]
  
1
w[0][1]
  
2
w[1][0]
  
'a'
e = [[1,2,3],[4,5,6],[7,8,9]]
  
e
  
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
e[0]
  
[1, 2, 3]
e[0][2]
  
3

len(e)
  
3
max(e[0])
  
3
e[2][1]
  
8
r=[1,2,'a','c',(10,20)]
  
len(r)
  
5
del r[2]
  
r
  
[1, 2, 'c', (10, 20)]
len(r)
  
4
r.insert(2,'a')
  
r
  
[1, 2, 'a', 'c', (10, 20)]
a.pop()
  
'milk'
r.pop()
  
(10, 20)
r
  
[1, 2, 'a', 'c']
r.pop(1)
  
2
r
  
[1, 'a', 'c']
r.pop(-2)
  
'a'
r
  
[1, 'c']
x
  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
t
  
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    t
NameError: name 't' is not defined
t=x[10:21]
  
t
  
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
del t[2:6]
  
t
  
[11, 12, 17, 18, 19, 20, 21]
t[2:6]=[]
  
t
  
[11, 12, 21]
t=x[10:21]
  
k=x[21:31]
  
k
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
t + k
  
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
k +t
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
t.append(8)
  
t
  
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 8]
t.pop()
  
8
t
  
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
t=[8]+t
  
t
  
[8, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
del t[0]
  
t
  
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
t=[8,23]+t
  
t
  
[8, 23, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
t[:2]=[]
  
t
  
[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
d=8
  
d+=9
  
d
  
17
k
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
k+=[4,5]
  
k
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 4, 5]
k
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 4, 5]
k.pop()
  
5
k.pop()
  
4
k
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
k.extend([4,5])
  
k
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 4, 5]
k.pop()
  
5
k.pop()
  
4
k.append([4,5])
  
k
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31, [4, 5]]
k.remove([4,5])
  
k
  
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
c=[1,2,2,1,3]
  
c.remove(1)
  
c
  
[2, 2, 1, 3]
c.insert(2,'a')
  
c
  
[2, 2, 'a', 1, 3]
c
  
[2, 2, 'a', 1, 3]
dir([])
  
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
x
  
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]
w=[1,2,5,3,0,-1]
  
w.sort()
  
w
  
[-1, 0, 1, 2, 3, 5]
>>> sorted(w)
...   
[-1, 0, 1, 2, 3, 5]
>>> w
...   
[-1, 0, 1, 2, 3, 5]
>>> w.clear()
...   
>>> w
...   
[]
>>> w=[1,2,5,3,0,-1]
...   
>>> W
...   
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    W
NameError: name 'W' is not defined. Did you mean: 'w'?
>>> w
...   
[1, 2, 5, 3, 0, -1]
>>> w[::-1]
...   
[-1, 0, 3, 5, 2, 1]
>>> w.reverse()
...   
>>> w
...   
[-1, 0, 3, 5, 2, 1]
>>> w
...   
[-1, 0, 3, 5, 2, 1]
>>> max(w)
...   
5
>>> min(w)
...   
-1
