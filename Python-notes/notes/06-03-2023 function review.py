Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#6-03-2023
# create a function that conumes a list, \
#appends a vlaue and  \ returns the odified list
list
<class 'list'>
type(list)
<class 'type'>
help(list)

list=[1,2,3]
list
[1, 2, 3]
list(('1','11'))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    list(('1','11'))
TypeError: 'list' object is not callable
del list
list(('1','11'))
['1', '11']
def func1(list_1):
    list_1.append('abc')
...     return list_1
... 
>>> l1=[1,'1',3.14]
>>> l1
[1, '1', 3.14]
>>> func1(l1)
[1, '1', 3.14, 'abc']
>>> l1
[1, '1', 3.14, 'abc']
>>> def func1(list_1):
...     k=1
...     list_1.append('abc')
...     print(k)
...     return list_1
... 
>>> l1=[1,2,3]
>>> func1(l1)
1
[1, 2, 3, 'abc']
>>> k
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    k
NameError: name 'k' is not defined
>>> list_1
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list_1
NameError: name 'list_1' is not defined. Did you mean: 'list'?
>>> 
>>> 
>>> ###  Mechanism to achieve two things Abstraction & decomposition
>>> #Abstraction : To hide the details , the 'How' and then the client will just know
>>> # Cares only about what
>>> len(l1)
4
>>> # Decomposition : Split larger codes in multiple sets and make each them as a new fuc for use
