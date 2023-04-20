Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 20-03-2023
# Oops practise



= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/20-03-2023 Student data oops example.py
messi = Student('leo',10)ython 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 20-03-2023
# Oops practise
SyntaxError: invalid syntax
# Instance = messi
 # class =Student
 
# Instance attributes : name , roll_no
# Initially name and roll_no only
dhoni = Student('MSD',7)
dhoni.roll_no
7
dhoni.name
'MSD'
dhoni.set_previous_school('csk')
dhoni.previous_school
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    dhoni.previous_school
AttributeError: 'Student' object has no attribute 'previous_school'. Did you mean: 'previous_schol'?
dhoni.previous_school
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    dhoni.previous_school
AttributeError: 'Student' object has no attribute 'previous_school'. Did you mean: 'previous_schol'?

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/20-03-2023 Student data oops example.py
dhoni = Student('MSD',7)
dhoni.set_previous_school('csk')
dhoni.previous_school
'csk'
# dhoni .previous_school ('csk') is a wrong practise
dhoni.get_previous_school()
'csk'
messi.get_previous_school()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    messi.get_previous_school()
NameError: name 'messi' is not defined

class Dog:
    pass

Dog()
<__main__.Dog object at 0x000001E26ACD3D90>
Dog()
<__main__.Dog object at 0x000001E26ACD3F50>
a =Dog()
b=Dog()
a == b
False
c = list()
d = list()
c == d
True
a
<__main__.Dog object at 0x000001E26ACD3FD0>
b
<__main__.Dog object at 0x000001E26ACD3E90>
c
[]
d
[]
type(a)==type(b)
True

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/20-03-2023 Class dog oops.py
dog = Dog('tomy',4)
dog_1=Dog('gypsy',5)
dog.name
'tomy'
dog_1.name
'gypsy'
dir(dog_1)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name']
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/20-03-2023 Class dog oops.py
>>> dog = Dog('tomy',4)
>>> dog_1=Dog('gypsy',5)
>>> dog.name
'tomy'
>>> dog_1.name
'gypsy'
>>> dog.species
'Canis familiaris'

>>> dog_1.species
'Canis familiaris'
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/20-03-2023 Class dog oops.py
>>> dir(Dog)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'species']
>>> dog = Dog('tomy',4)
>>> dog_1=Dog('gypsy',5)
>>> dog_1.species = 'Felis silverstris'
>>> dog.species
'Canis familiaris'
>>> dog_1.species
'Felis silverstris'
>>> dog.species == dog_1.species
False
>>> dog_2 = Dog('tyson',6)
>>> dog_2.species
'Canis familiaris'
>>> # Class invariant
>>> 
