Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#17-02-2023

#Revision class


# PRGM for first 10 odd nos using while loop

i=1
# Bool
type (bool)
<class 'type'>
help(bool)

 True==1
 
SyntaxError: unexpected indent
True==1
True
False==0
True
if True :
    print(True)

    
True
else:
    
SyntaxError: invalid syntax
if 1:
    print(True)
else:
    print(False)

    
True
1<2
True
1
1
while i<=11:
    print(2*i-1)
    i=i+1

    
1
3
5
7
9
11
13
15
17
19
21
while i<=11:
    print(2*i-1)
    i=i+1

    
i
12
#### glitch i value goes to 12 & previous its value is 1
while i<11:
    print(2*i-1)
    i=i+1

    
i=1
while i<11:
    print(2*i-1)
    i=i+1

    
1
3
5
7
9
11
13
15
17
19
n=0
while(n<=10):
    if(n%2!=0):
        print('Odd no:',n)
        n=n+1

        
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    while(n<=10):
KeyboardInterrupt



while(n<=10):
    if(n%2!=0):
        print('Odd no:',n)
    n=n+1

    
Odd no: 1
Odd no: 3
Odd no: 5
Odd no: 7
Odd no: 9
n=0
while(n<20):
    print(2*n-1)
    n=n+1

    
-1
1
3
5
7
9
11
13
15
17
19
21
23
25
27
29
31
33
35
37
# 20 odds
Limit =20
Limit=2*10

n=0
while(n<Limit):
    if(n%2!=0):
        print('Odd no:',n)
    n=n+1
    
SyntaxError: multiple statements found while compiling a single statement
n=0
while(n<Limit):
    if(n%2!=0):
        print('Odd no:',n)
    n=n+1
    
SyntaxError: multiple statements found while compiling a single statement

n=0
while(n<Limit):
    if(n%2!=0):
        print('Odd no:',n)
    n=n+1

    
Odd no: 1
Odd no: 3
Odd no: 5
Odd no: 7
Odd no: 9
Odd no: 11
Odd no: 13
Odd no: 15
Odd no: 17
Odd no: 19

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py
Please enter the number20
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py", line 14, in <module>
    print_odds(o)
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py", line 7, in print_odds
    while(n<Limit):
TypeError: '<' not supported between instances of 'int' and 'str'

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py
Please enter the number20
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py", line 14, in <module>
    print_odds(o)
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py", line 7, in print_odds
    while(n<=Limit):
TypeError: '<=' not supported between instances of 'int' and 'str'

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py", line 13, in <module>
    o=input(int('Please enter the number'))
ValueError: invalid literal for int() with base 10: 'Please enter the number'

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py
Please enter the number20
Odd no: 1
Odd no: 3
Odd no: 5
Odd no: 7
Odd no: 9
Odd no: 11
Odd no: 13
Odd no: 15
Odd no: 17
Odd no: 19
Odd no: 21
Odd no: 23
Odd no: 25
Odd no: 27
Odd no: 29
Odd no: 31
Odd no: 33
Odd no: 35
Odd no: 37
Odd no: 39
>>> print_odds()
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print_odds()
TypeError: print_odds() missing 1 required positional argument: 'odd_num'
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/17 feb revision while loop for odd numbers by func.py
Please enter the number10
Odd no: 1
Odd no: 3
Odd no: 5
Odd no: 7
Odd no: 9
Odd no: 11
Odd no: 13
Odd no: 15
Odd no: 17
Odd no: 19
>>> print_odds(odd_num)
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print_odds(odd_num)
NameError: name 'odd_num' is not defined
