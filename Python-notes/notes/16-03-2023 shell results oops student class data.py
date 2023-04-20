Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 16-03-2023


= RESTART: C:\Users\Admin\Documents\first-dir\Python-notes\notes\OOP student data (Introduction) 15-03-2023.py
virat=student('Virat',18)
type(virat)
<class '__main__.student'>
# Double __ underscore :: dunder
# Custom defined
type(list)
<class 'type'>
type([1,2])
<class 'list'>
dir(virat)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'roll_no']
dir([1])
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
# Attributs
# Attributes
isinstance(virat,Student)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    isinstance(virat,Student)
NameError: name 'Student' is not defined. Did you mean: 'student'?
>>> isinstance(virat,student)
True
>>> isinstance(virat,list)
False
>>> isinstance([1,2],list)
True
>>> # to check for instance
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 OOPS student data updation prac.py
>>> virat=student('Virat',18)
>>> virat.get_previous_school
<bound method student.get_previous_school of <__main__.student object at 0x000001E70EBE0050>>
>>> virat.name
'Virat'
>>> virat.roll
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    virat.roll
AttributeError: 'student' object has no attribute 'roll'
>>> virat.set_previous_school('data school')
Previous School:'Data school'
>>> virat.set_previous_school()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    virat.set_previous_school()
TypeError: student.set_previous_school() missing 1 required positional argument: 'school_name'
>>> virat.get_previous_school
<bound method student.get_previous_school of <__main__.student object at 0x000001E70EBE0050>>
>>> virat.set_previous_school('data school')
Previous School:'Data school'
>>> virat.get_previous_school()
"'Data school'"
