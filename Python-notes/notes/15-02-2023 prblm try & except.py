Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 15-02-2023
>>> try:
...     result=4/0
... except ZeroDivisionError:
...     print('msg')
... 
...     
msg
>>> a=[1,2,3]
>>> b=[7,8,0]
>>> for i in range(len(a)):
...     print(a[i]/b[i])
... 
...     
0.14285714285714285
0.25
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    print(a[i]/b[i])
ZeroDivisionError: division by zero
>>> = RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\15-02-2023.py =
... 
SyntaxError: invalid syntax
>>> [1,2,3]
[1, 2, 3]
>>> [1,23]
[1, 23]
>>> # Type error : non-numerical
