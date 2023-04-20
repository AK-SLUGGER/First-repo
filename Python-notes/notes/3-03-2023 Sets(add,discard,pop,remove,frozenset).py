Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#03-03-2023
#set() function
x={'a','b','c'}
x
{'c', 'b', 'a'}
x.add(d)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x.add(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
x.add('z')
x
{'c', 'b', 'a', 'z'}
# to add an element in a set
x.remove('z')
x
{'c', 'b', 'a'}
# to remove a member
x.remove('q')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x.remove('q')
KeyError: 'q'
# q i not present
'q' in x
False
x.discard('q')
x
{'c', 'b', 'a'}
# discard no rises if membe ris not present
x.discard('b')
x
{'c', 'a'}
x.add('b')
x
{'c', 'b', 'a'}
x.pop()
'c'
x
{'b', 'a'}
x.pop()
'b'
x
{'a'}
x.pop()
'a'
x
set()
x.pop()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    x.pop()
KeyError: 'pop from an empty set'
# set is empty
x={'a','b','c'}
# pop return & removes the elements
x
{'c', 'b', 'a'}
x.clear()
# to make it empty
x
set()
x={'a','b','c'}
#add,remove,discard,pop,clear


#Frozen Sets

# Problem on set
x={'a','b','c'}
x
{'c', 'b', 'a'}
x.discard('d')
x
{'c', 'b', 'a'}
y=x.discard('d')
y
print(y)
None
x={'a','b','c',None}
x.discard('d')
y=x.discard('d')
y
print(y)
None
x
{'c', 'b', 'a', None}
'd' in x
False


#Frozen Sets

#Frozen seta are immutable

x=frozenset(['a','b','c'])
x
frozenset({'c', 'b', 'a'})
len(x)
3
x & {'c','d','e'}
frozenset({'c'})
x.add('q')
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    x.add('q')
AttributeError: 'frozenset' object has no attribute 'add'
dir(x)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']
x1=frozenset(['a'])
x2=frozenset(['b'])
x3=frozenset(['c'])
x={x1,x2,x3}
x
{frozenset({'c'}), frozenset({'a'}), frozenset({'b'})}
# to define set of sets use frozen set
>>> d = {x:1}
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    d = {x:1}
TypeError: unhashable type: 'set'
>>> d= {x1:1}
>>> d
{frozenset({'a'}): 1}
>>> type(d)
<class 'dict'>
>>> p=1
>>> l=1
>>> id(p)
140714660324136
>>> id(l)
140714660324136
>>> l1=[1,2,3]
>>> l2=l1
>>> l3=[1,2,3]
>>> id(l1)
2799507648640
>>> id(l2)
2799507648640
>>> id(l3)
2799507648960
>>> l1=[a,b]
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    l1=[a,b]
NameError: name 'a' is not defined
>>> l1=['a','b']
>>> id(l1)
2799507648384
>>> l1
['a', 'b']
>>> l2
[1, 2, 3]
>>> id(l2)
2799507648640
