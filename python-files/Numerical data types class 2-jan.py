Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
n=1.625
f'{n:.2f}'
'1.62'
n=1.626
f'{n:.2f}'
'1.63'
#round of automatically done in previous statement
n=1.615
f'[n:.2f]'
'[n:.2f]'
f'{n:.2f}'
'1.61'
#.615 IS DECIMAL =>
round(1.615)
2
round(1.615,2)
1.61
round(1.61,2)
1.61
n=1.626666635
round(n)
2
round(n,7)
1.6266666
a=0.1
b=0.1
c=0.1
a+b+c
0.30000000000000004
# errors in pyhton (not every no can be exp by binary)
0.1
0.1
round(1.41215)
1
round(1.41215,4)
1.4122
x=1.41215
f'{x:.4f}'
'1.4122'
q=123456789
q=123_456_789
print(q)
123456789
print(f'{q}')
123456789
print(f'{q:,}')
123,456,789
w=12345.678
print(f'{w:,.2f}')
12,345.68
print(f'{w:,.3f}')
12,345.678
print(f'{w:,.5f}')
12,345.67800
messi_sr=0.96
f'{messi_sr}'
'0.96'
f'{messi_sr:.1%}'
'96.0%'
f'{messi_sr:%}'
'96.000000%'
#f string :.nf ,',',%
#2
123.12
123.12
123.00
123.0
n=123.0
n
123.0
type(n)
<class 'float'>
n.is_integer()
True
m=123.12
m.si_integer()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    m.si_integer()
AttributeError: 'float' object has no attribute 'si_integer'. Did you mean: 'is_integer'?
m.is_integer()
False
#functions
#pow(),int(),rounnd(),help(),type()
#Common thing is paranthesses()
pow
<built-in function pow>
int
<class 'int'>
round
<built-in function round>
help
Type help() for interactive help, or help(object) for help about object.
ptint
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    ptint
NameError: name 'ptint' is not defined. Did you mean: 'print'?
print
<built-in function print>
n
123.0
print(n)
123.0
pow(2,3)
8
pow=12
pow(2,3)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    pow(2,3)
TypeError: 'int' object is not callable
pow
12
type(pow)
<class 'int'>
type(print)
<class 'builtin_function_or_method'>
print
<built-in function print>
print('hey,this is bulitin func')
hey,this is bulitin func
print='not a fun anymore'
print
'not a fun anymore'
type(print)
<class 'str'>
del print
type (print)
<class 'builtin_function_or_method'>
#del is used to again makes the builtin function
#see the upper examples
del pow
pow
<built-in function pow>
len('1234567')
7
#fun call using paranthesis ;[opitonal:arguments if any]
#executed /evaluated -predefined processes
#returns some value
length =len('123')
length
3
len
<built-in function len>
len('123')#step:fun call[with arg]
3
#concatenate word as many no of times a user ask you
'abcd'*2
'abcdabcd'
'abcd"*5
SyntaxError: incomplete input
'kchri'*5
'kchrikchrikchrikchrikchri'
''''

... 
... 
... ''''
SyntaxError: incomplete input
>>> '''
... '''
'\n'
>>> ""' '""
' '
>>> # program to cocatenate
>>> string_1='abcd'
>>> n_concat=input('How many times you want to concatenate')
How many times you want to concatenate
>>> new_string=string_1*n_concat#cant work due to string and int function cant concat
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    new_string=string_1*n_concat#cant work due to string and int function cant concat
TypeError: can't multiply sequence by non-int of type 'str'
>>> new_string=string_1*int(n_concat)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    new_string=string_1*int(n_concat)
ValueError: invalid literal for int() with base 10: ''
>>> print(new_string)
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    print(new_string)
NameError: name 'new_string' is not defined
>>> new_string=string_1*int(n_concat)
... print(new_string)
SyntaxError: multiple statements found while compiling a single statement
>>> new_string=string_1*int(n_concat)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    new_string=string_1*int(n_concat)
ValueError: invalid literal for int() with base 10: ''
>>> string_1='abcd'
