Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 17-03-2023

# OOPS:- Data attributes (componrents of data which are bundeled together)

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
ronaldo=student('ronaldo',7)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    ronaldo=student('ronaldo',7)
TypeError: student() takes no arguments

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
ronaldo = student('ronaldo',7)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    ronaldo = student('ronaldo',7)
TypeError: student() takes no arguments

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
ronaldo.set_previous_school("school-1")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ronaldo.set_previous_school("school-1")
NameError: name 'ronaldo' is not defined

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
ronaldo.set_previous_school("school-1")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    ronaldo.set_previous_school("school-1")
NameError: name 'ronaldo' is not defined
ronaldo.set_previous_school("school-1")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    ronaldo.set_previous_school("school-1")
NameError: name 'ronaldo' is not defined

========== RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py ==========
abhishek = Student('abhishek',7)
self.name=name
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    self.name=name
NameError: name 'name' is not defined
self.abhishek=abhishek
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    self.abhishek=abhishek
NameError: name 'self' is not defined
abhishek = Student('abhishek',7)
del abhishek
sachin=Student('Sachin',3)
sachin.name
'Sachin'
3.roll
SyntaxError: invalid decimal literal
sachin.roll
3
sachin=Student("Tendulkar",10)
sachin.name
'Tendulkar'
sachin.roll
10

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
ronaldo(Student('cr7",7)
                
SyntaxError: incomplete input
ronaldo=Student("cr7",7)
                
ronaldo.name
                
'cr7'
ronaldo.get_previous_school
                
<bound method Student.get_previous_school of <__main__.Student object at 0x000001D7931E78D0>>
ronaldo.set_previous_school("School_1")
                
ronaldo.get_previous_school()
                
'School_1'
ronaldo.get_previous_school()
                
'School_1'
SyntaxError: incomplete inputronaldo=Student("cr7",7)
                
SyntaxError: invalid syntax


= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
ronaldo=Student("cr7",7)
                
ronaldo.get_previous_school()
                
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    ronaldo.get_previous_school()
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py", line 14, in get_previous_school
    if self.previous_school == None:
AttributeError: 'Student' object has no attribute 'previous_school'. Did you mean: 'get_previous_school'?

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
>>> ronaldo=Student("cr7",7)
...                 
>>> ronaldo.get_previous_school()
...                 
'First please call the set_previous_school'
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
>>> ronaldo=Student("cr7",7)
...                 
>>> ronaldo.get_previous_school()
...                 
'First please call the set_previous_school method'
>>> ronaldo.set_previous_school("School_1")
...                 
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-03-2023 Data attributes ex.py
>>> ronaldo=Student("cr7",7)ronaldo.get_previous_school()
...                 
SyntaxError: invalid syntax
>>> ronaldo=Student("cr7",7)
...                 
>>> ronaldo.get_previous_school()
...                 
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    ronaldo.get_previous_school()
AttributeError: 'Student' object has no attribute 'get_previous_school'. Did you mean: 'previous_school'?
>>> ronaldo=Student("cr7",7)
...                 
>>> ronaldo.previous_school="Random School"
...                 
>>> ronaldo.previous_school
...                 
'Random School'
>>> ronaldo.roll
...                 
7
>>> ronaldo.roll=101 # Bad practise
...                 
>>> # Define a separate method
...                 
>>> Student
...                 
<class '__main__.Student'>
