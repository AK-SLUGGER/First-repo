Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py
a=coordinates(2,3)
a.x
2
a.y
3
b=coordinates(3,2)
b.x
3
b.y
2
print(a)
<__main__.coordinates object at 0x00000176C3222510>

= RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py
b=coordinates(3,2)
print(b)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(b)
  File "C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py", line 13, in __str__
    return f('{self.x} , {self.y}')
NameError: name 'f' is not defined

= RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py
b=coordinates(3,2)
print(b)
3 , 2
a=coordinates(2,3)
print(a)
2 , 3

= RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py
b=coordinates(3,2)
print(b)
3 , 2
a=coordinates(2,3)
print(a)
2 , 3

= RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py
a=coordinates(2,3)
print(a)
2 , 3
>>> b=coordinates(3,2)
>>> print(b)
3 , 2
>>> distance_sq=(a.x-b.x)**2+(a.y-b.y)**2
>>> distance_sq
2
>>> (a.x-b.x)**2
1
>>> (a.y-b.y)**2
1
>>> distance_sq
2
>>> distance_sq**0.5
1.4142135623730951
>>> 
= RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py
>>> a=coordinates(2,3)
>>> b=coordinates(3,2)
>>> a.distance(b)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    a.distance(b)
  File "C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py", line 25, in distance
    return (x-diff_sq + y_diff_sq)**0.5 # Disatnce bw two points in 2d coordinates
NameError: name 'x' is not defined
>>> print(a)
<2,3>
>>> print(b)
<3,2>
>>> 
= RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\21-03-2023 Class coordinates.py
>>> a=coordinates(2,3)
>>> b=coordinates(3,2)
>>> a.distance(b)
1.4142135623730951
