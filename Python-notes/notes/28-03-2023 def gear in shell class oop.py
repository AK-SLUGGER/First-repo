Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/28-03-2023 oops class car gear & speed practise.py
>>> innova=Car('red',130,toyota,190,'MUV','Auto')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    innova=Car('red',130,toyota,190,'MUV','Auto')
NameError: name 'toyota' is not defined
>>> innova=Car('red',130,'toyota',190,'MUV','Auto')
>>> isinstance(innova,Car)
True
>>> innova.gear_shift(49)
2
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/28-03-2023 oops class car gear & speed practise.py
>>> innova=Car('red',130,'toyota',190,'MUV','Auto')
>>> innova.gear_shift(123)
'Overspeeding'
>>> innova.gear
>>> print(innova.gear)
None
>>> innova.gear_shift(113)
'Overspeeding'
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/28-03-2023 oops class car gear & speed practise.py
>>> innova=Car('red',130,'toyota',190,'MUV','Auto')
>>> innova.gear_shift(123)
'Overspeeding'
>>> innova.gear
>>> print(innova.gear)
None
>>> innova.gear_shift(113)
4
>>> innova.gear
4
>>> print(innova.gear)
4
