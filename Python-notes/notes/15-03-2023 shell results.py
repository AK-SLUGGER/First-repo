Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
####15-03-2023
msg='Welcome'
border='*'

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 banner .demo.py
banner('welcome','*')
*******
welcome
*******
banner('welcome','-')
-------
welcome
-------
banner('good evening ','-')
-------------
good evening 
-------------

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 banner .demo.py
banner('wecome')
******
wecome
******
banner('welcome','#')
#######
welcome
#######
banner('wecome')
******
wecome
******
#Default takes if not assign the second takes from the func def
print('Hello world','good','Evening', sep = '|')
Hello world|good|Evening
print('Hello world','good','Evening', sep = '++')
Hello world++good++Evening
print('Hello world','good','Evening')
Hello world good Evening
# by default sep is space
banner('welcome',border='|')
|||||||
welcome
|||||||
banner(message="hey",border="-")
---
hey
---
banner(border="-",message="hey")
---
hey
---
banner('-')
*
-
*
banner('-','hey')
hey
-
hey
# Object Oriented Programming
#name,roll_no
name='Virat'
roll_no=18

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 students details oops demo.py
namename='Virat'
roll_no=18
SyntaxError: multiple statements found while compiling a single statement

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 students details oops demo.py
name
['Virat']

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 students details oops demo.py
name[0]
'Virat'
name[1]
'rohith'
# Remem each time whose name is in which position of list
# which is not possible

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 student details version -2 oops.py
students_dict
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    students_dict
NameError: name 'students_dict' is not defined. Did you mean: 'student_dict'?

student_dict['virat']
18

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 student details version -2 oops.py
main()
name:Virat
roll no:18
student_name
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    student_name
NameError: name 'student_name' is not defined

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 student details version -2 oops.py
main()
name:virat
roll no:18
virat's roll no. is 18

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 student details version -2 oops.py
>>> main()
name:virat
roll no. :18
virat's roll no. is 18
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 student details version -2 oops.py
>>> main()
name:Virat
roll no. :18
Virat's roll no. is 18
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/OOP student data (begining) 15-03-2023.py
>>> virat=Student('Virat',18)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    virat=Student('Virat',18)
NameError: name 'Student' is not defined. Did you mean: 'student'?
>>> virat = student('Virat',18)
>>> virat.name
'Virat'
>>> virat,roll_no
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    virat,roll_no
NameError: name 'roll_no' is not defined
>>> virat.roll_no
18
>>> rohith = student('rohith',45)
>>> rohith.name
'rohith'
>>> dir(rohith)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'name', 'roll_no']
>>> # Instance of the class called Student
