Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=Health
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x=Health
NameError: name 'Health' is not defined
>>> x='Health'
>>> x
'Health'
>>> x[0]+x[1].upper()+x[2:4]+x[4].upper()+x[5]
'HEalTh'
>>> x
'Health'
