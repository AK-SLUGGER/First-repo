Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#1-03-2023
#Sets
#Unordered
#Elements have to be unique => No duplicates allowed
# Set is mutable -> modified but the elements have to be immutable
s= set()
s
set()
help(set)

s= set(['a','e','i','o','u'])
s
{'a', 'u', 'o', 'e', 'i'}
#set & dict use same curly braces
v={'One':'a','Two':'e'}
v
{'One': 'a', 'Two': 'e'}
# v is a dict with key value pair & s is a set
s
{'a', 'u', 'o', 'e', 'i'}
# set creates the order as seen above
s=={'e','a','o','i','u'}
True
# order doesnt matter
s=={'e','a','o','i','u','a','a','a'}
True
w=[1,2,3,4]
w==[1,2,3,4,1,1]
False
# but in set repetation doesnt matter
# collection of unique elements
{[1,2],[9,0]}
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    {[1,2],[9,0]}
TypeError: unhashable type: 'list'
{(1,2),(9,0)}
{(9, 0), (1, 2)}
# we cannot use mutable data types in set as per rule
r={}#r will be a dict not a set
type(r)
<class 'dict'>
t=[]
type(t)
<class 'list'>
p=()
type(p)
<class 'tuple'>
e=set()
type(e)
<class 'set'>
s
{'a', 'u', 'o', 'e', 'i'}
list(s)
['a', 'u', 'o', 'e', 'i']
tuple(s)
('a', 'u', 'o', 'e', 'i')
s
{'a', 'u', 'o', 'e', 'i'}
'food'
'food'
set('food')
{'o', 'd', 'f'}
set('food')==set('fooooddd')
True
set('food')=={'f','d','o'}#the order doent matter in set
True
tuple({'f','o','d'})
('o', 'd', 'f')
s
{'a', 'u', 'o', 'e', 'i'}
'a' in s
True
'b' in s
False
s
{'a', 'u', 'o', 'e', 'i'}
len(s)
5
o=set('fooooooooooooood')
len(o)
3
len(set('fooooooooooooood'))
3
t={'food'}
type(t)
<class 'set'>
t=set('food')
y={'food'}
t
{'o', 'd', 'f'}
y
{'food'}
len(t)
3
len(y)
1
#Methods
x1={1,2,3}
x1
{1, 2, 3}
x2={3,4,5}
x2
{3, 4, 5}
# Union : All the elements of x1 & x2
{1,2,3,4,5}
{1, 2, 3, 4, 5}
x1 | x2
{1, 2, 3, 4, 5}
x_union_op =x1 | x2
x_union_op
{1, 2, 3, 4, 5}
x1.union(x2)
{1, 2, 3, 4, 5}
x1
{1, 2, 3}
x2
{3, 4, 5}
x_union_method = x1.union(x2)
x_union_method
{1, 2, 3, 4, 5}
x1
{1, 2, 3}
x1|('a',b','c')
    
SyntaxError: unterminated string literal (detected at line 1)
x1.union(('a','b','c'))
    
{1, 2, 3, 'c', 'b', 'a'}
help(x1.union)
    
Help on built-in function union:

union(...) method of builtins.set instance
    Return the union of sets as a new set.
    
    (i.e. all elements that are in either set.)

x1.union(['a','b','c'])
    
{1, 2, 3, 'c', 'b', 'a'}
# intersection
    
x1
    
{1, 2, 3}
x2
    
{3, 4, 5}
x3={5,6,7}
    
x4={100,101,102}
    
x1|x2|x3|x4
    
{1, 2, 3, 4, 5, 6, 7, 100, 101, 102}
#Intersection
    
x1.union(x2,x3,x4)
    
{1, 2, 3, 4, 5, 6, 7, 100, 101, 102}
#Intersection
    
x1.intersection(x2)
    
{3}
# intersection returns common char
    
x1&x2
    
{3}
x2 & x3
    
{5}
a={1,2,3,4}
    
b={2,3,4,5}
    
c={3,4,5,6}
    
d={4,5,6,7}
    
a.intersection(b,c,d)
    
{4}
a&b&c&d
    
{4}
{'a','b','c'}.intersection({1,2,3})
    
set()
x1.difference(x2)
    
{1, 2}
x2.difference(x1)
    
{4, 5}
x1.intersection(x2)==x2.intersection(x1)
    
True
x1.union(x2)=x2.union(x1)
    
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
x1.union(x2)==x2.union(x1)
    
True
x1.difference(x2)==x2.difference(x1)
    
False
x1-x2
    
{1, 2}
x2-x1
    
{4, 5}
x1-x2==x1.difference(x2)
    
True
a={1,2,3,30,300}
    
b={10,20,30,40}
    
c={100,200,300,400}
    
a.difference(b,c)
    
{1, 2, 3}
a-b-c
...     
{1, 2, 3}
>>> x1
...     
{1, 2, 3}
>>> x2
...     
{3, 4, 5}
>>> x1-x2
...     
{1, 2}
>>> x1-x2-x3
...     
{1, 2}
>>> 1.difference(x2)
...     
SyntaxError: invalid decimal literal
>>> x1.difference(x2)
...     
{1, 2}
>>> a.difference(b)
...     
{1, 2, 3, 300}
>>> q=a.difference(b)
...     
>>> q.difference(c)
...     
{1, 2, 3}
>>> q.difference(c)==a.difference(b,c)
...     
True
>>> a-b
...     
{1, 2, 3, 300}
>>> q1=a-b
...     
>>> q1-c
...     
{1, 2, 3}
