Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/Admin/Documents/first-dir/Pyhton-notes/Capture_emp_data  by List data type.py
nameVIRAT
dob05-11-1988
desgnBATSMAN
resDELHI
nameROHIT
dob01-12-2022
desgnBATSMAN2
resGURGAON
nameRAHUL
dob07-11-2022
desgnCAPTAIN
resHARYANA
nameISHAN
dob09-11-2022
desgnBOWLER
resHARYANA
nameKSDF
dob09-09-2022
desgnSWIPPER
resHARYANA
name-list
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    name-list
TypeError: unsupported operand type(s) for -: 'str' and 'type'
name-list
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    name-list
TypeError: unsupported operand type(s) for -: 'str' and 'type'
name_list
['VIRAT', 'ROHIT', 'RAHUL', 'ISHAN', 'KSDF']

= RESTART: C:/Users/Admin/Documents/first-dir/Pyhton-notes/Capture_emp_data  by List data type.py
namev
namer
namei
name_list
['v', 'r', 'i']
emp_id_list
['AB1', 'AB2', 'AB3']
name[3] = 'B'
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    name[3] = 'B'
TypeError: 'str' object does not support item assignment
name_list[2]='b'
emp_id_list[2]
'AB3'
emp_id-list.append('AB'+STR(4))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    emp_id-list.append('AB'+STR(4))
NameError: name 'STR' is not defined. Did you mean: 'str'?
emp_id_list.append('AB'+STR(4))
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    emp_id_list.append('AB'+STR(4))
NameError: name 'STR' is not defined. Did you mean: 'str'?
emp_id_list.append('AB'+str(4))
emp_id_list
['AB1', 'AB2', 'AB3', 'AB4']
dir(emp_id_list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
help(remove)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    help(remove)
NameError: name 'remove' is not defined
>>> help([].remove)
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.
    
    Raises ValueError if the value is not present.

>>> emp_id_list.remove('AB3')
>>> EMP-ID-LIST
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    EMP-ID-LIST
NameError: name 'EMP' is not defined
>>> emp_id_list
['AB1', 'AB2', 'AB4']
>>> emp_id_hist_list =['AB1', 'AB2', 'AB3', 'AB4']
>>> len(emp_id_list)
3
>>> 
==== RESTART: C:/Users/Admin/Documents/first-dir/Pyhton-notes/Demo_global.py ===
InsideHello
Outside10
>>> 
==== RESTART: C:/Users/Admin/Documents/first-dir/Pyhton-notes/Demo_global.py ===
InsideHello
Outside10
>>> 
==== RESTART: C:/Users/Admin/Documents/first-dir/Pyhton-notes/Demo_global.py ===
InsideHello
Outside10
x=HelloHello
InsideHello
OutsideHello
x=HelloHello
