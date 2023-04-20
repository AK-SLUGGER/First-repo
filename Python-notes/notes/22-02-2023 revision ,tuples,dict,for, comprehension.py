Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
###22-02-2023ython 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
SyntaxError: invalid syntax
### 22-02-2023 feb
###Tuple
t=()
type(t)
<class 'tuple'>
s=tuple()
s
()
s==t
True
w=(1)
# w is not tuple
type(w)
<class 'int'>
c=8
c=8.5
type(c)
<class 'float'>
c.is_integer()
False
d=9.0
d.is_integer()
True
type((9.0))
<class 'float'>
(9.0).is_integer()
True
9.0.is_integer()
True
c
8.5
c=8
dir(c)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
r =(1,)
type(r)
<class 'tuple'>
s=([1,2])
type(s)
<class 'list'>
s=([1,2],)
type(s)
<class 'tuple'>
d=(1,2,3)
a,b,c=d
a
1
b
2
c
3
e='a',1,5
e
('a', 1, 5)
type(e)
<class 'tuple'>
q,w,e=[1.4.9]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
q,w,e=[1,4,9]
q
1
w
4
e
9

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/tuple func revision 21-02-2023.py
sum_diff(1,2)
(3, -1)
sum_a_b,diff_a_b=sum_diff(4,2)
sum_a_b
6
diff_a_b
2
e='a',1,5
f=list(e)
f
['a', 1, 5]
f[0]='l'
f
['l', 1, 5]
e
('a', 1, 5)
e[0]='l'
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    e[0]='l'
TypeError: 'tuple' object does not support item assignment
e
('a', 1, 5)
e=('l',)+e[1:]
e
('l', 1, 5)
a=8
b=9

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/temp_swap-demo.py
l=9

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/temp_swap-demo.py
l=9
m=8
swap(l,m)
(8, 9)
a=7
b=2
a,b=b,a
a
2
b
7


### revision dictionaries
#Dictionaries are mutable
d={}
type(d)
<class 'dict'>
e=dict()
e
{}
d==e
True
# Key value pair
s
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    s
NameError: name 's' is not defined
s=(1,2,3)
s
(1, 2, 3)
s[0]
1
d={'0':0,1:'p'}
d[0]
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    d[0]
KeyError: 0
d.keys()
dict_keys(['0', 1])
d={'0':0,1:'p',[2]:2}
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    d={'0':0,1:'p',[2]:2}
TypeError: unhashable type: 'list'
d={'0':0,1:'p',(2):2}
d
{'0': 0, 1: 'p', 2: 2}
d.keys()
dict_keys(['0', 1, 2])
3 in d.keys()
False
3 not in d.keys()
True
d[3]
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    d[3]
KeyError: 3
d.pop()
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.pop(1)
'p'
d
{'0': 0, 2: 2}
d[(2,)]=d.pop(2)
d
{'0': 0, (2,): 2}
#new key value pair is created
d[1]='q'
d
{'0': 0, (2,): 2, 1: 'q'}
e=d
id(e)
1529866207168
id(d)
1529866207168
e is d
True
e
{'0': 0, (2,): 2, 1: 'q'}
d
{'0': 0, (2,): 2, 1: 'q'}
d.popitem()# returns teh last as a tuple
(1, 'q')
d
{'0': 0, (2,): 2}
d.values()
dict_values([0, 2])
for i in d:
    print(i)

    
0
(2,)
for i,v in d.items():
    print(i,v)

    
0 0
(2,) 2
g=dict([('a',1),('b',2)])
g
{'a': 1, 'b': 2}
g=dict([('a',1),(x,2)])
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    g=dict([('a',1),(x,2)])
NameError: name 'x' is not defined
g
{'a': 1, 'b': 2}
g.updaet({'x':2})
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    g.updaet({'x':2})
AttributeError: 'dict' object has no attribute 'updaet'. Did you mean: 'update'?
g.update({'x':2},{'c':3})
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    g.update({'x':2},{'c':3})
TypeError: update expected at most 1 argument, got 2
g.update({'x':2,'c':3})
g
{'a': 1, 'b': 2, 'x': 2, 'c': 3}
g
{'a': 1, 'b': 2, 'x': 2, 'c': 3}
g['a']
1
g.get('p')
g.get('a')
1


##Nested dict
##h={<immutable>:{}}
h={{2:3}:4}
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    h={{2:3}:4}
TypeError: unhashable type: 'dict'
h={4:{2:3}}
h
{4: {2: 3}}
h.keys()
dict_keys([4])


##for loops
a=[1,2,3,4]
b=[1,2,6,7]
for i in a:
    if i in b:
        a.remove(i)

        
a
[2, 3, 4]
for i in a:
    print(f'a={a},i={i},outside if')
    if i in b:
        a.remove(i)
        print(f'\t a={a},i={i},Inside if')

        
a=[2, 3, 4],i=2,outside if
	 a=[3, 4],i=2,Inside if
a=[3, 4],i=4,outside if
a=[1,2,3,4]
for i in a:
    print(f'a={a},i={i},outside if')
    if i in b:
        a.remove(i)
        print(f'\t a={a},i={i},Inside if')

        
a=[1, 2, 3, 4],i=1,outside if
	 a=[2, 3, 4],i=1,Inside if
a=[2, 3, 4],i=3,outside if
a=[2, 3, 4],i=4,outside if
a.index(3)
1
a[1]
3
d=[i for i in range(10)]
d
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
e=[]
for i in range(10):
    e.append(i)
... 
...     
>>> e
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> f=[]
>>> for i in range(10):
...     if i%2==0:
...         e.append(i)
... 
...         
>>> f
[]
>>> for i in range(10):
...     if i%2==0:
...         f.append(i)
... 
...         
>>> f
[0, 2, 4, 6, 8]
>>> g=[i for i in range(10) if i %2 ==0]
>>> g
[0, 2, 4, 6, 8]
>>> h=[]
>>> for i in range(10):
...     IF I %2 ==0:
...         
SyntaxError: invalid syntax
>>> for i in range(10):
...     if i%2==0:
...         h.append(i)
...     else:
...         h.append(i*2)
... 
...         
>>> h
[0, 2, 2, 6, 4, 10, 6, 14, 8, 18]
>>> j=[i if i%2==0 else i*2 for i in range(10)]
>>> j
[0, 2, 2, 6, 4, 10, 6, 14, 8, 18]
