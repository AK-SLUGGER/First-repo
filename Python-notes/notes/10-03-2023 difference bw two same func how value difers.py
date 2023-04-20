Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 10-03-2023
>>> 
>>> def fun(L):
...     L=['a','b']
...     return L
... 
>>> a=[1,2,3]
>>> b=fun(a)
>>> print(a==b)
False
>>> a
[1, 2, 3]
>>> print(a)
[1, 2, 3]
>>> b= fun(a)
>>> b
['a', 'b']
>>> def fun(L):
...     L.append(1)
... 
...     return L
... 
>>> a=[1,2,3]
>>> b=fun(a)
>>> b
[1, 2, 3, 1]
>>> a
[1, 2, 3, 1]
