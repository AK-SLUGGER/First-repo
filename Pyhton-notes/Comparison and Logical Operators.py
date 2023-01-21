Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Comparison operators
True
True
False
False
#Boolean data types
dir("")
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
2<3
True
2>3
False
2<=3
True
"a"<"b"
True
'b'<'a'
False
'A'>'a'
False
ord('a')
97
#ord is a fuctions that returns the askey value
ord('A')
65
ord('b')
98
#Askey or unicode
#and or not ....logical operators
# not -reverse Truth status
not True
False
not False
True
not 1
False
not 3
False
True ==1
True
True ==2
False
p =False
not p
True
q
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    q
NameError: name 'q' is not defined
True and False
False
# and ret True only when bith are True
#or ret True if ANY one of the operands are True
True or False
True
False or False
False
>>> not True and False
False
>>> not Turew or False
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    not Turew or False
NameError: name 'Turew' is not defined
>>> False and not True
False
>>> #'==' value equalty
>>> 2 ==2
True
>>> 2==3
False
>>> not True == False
True
>>> False == not True
SyntaxError: invalid syntax
>>> #due to order of presidence
>>> False==(not True)
True
>>> #< <= == >= > 1st preferance
>>> # not 2nd pref.
>>> # and 3rd pref.
>>> or 4th pref.
SyntaxError: invalid decimal literal
>>> # or 4h pref.
>>> True and False or True
True
>>> True and not False or not True
True
>>> True or False
True
>>> # Order of Pref.
>>> #!=
>>> #not equal to operator
>>> 2 !=3
True
