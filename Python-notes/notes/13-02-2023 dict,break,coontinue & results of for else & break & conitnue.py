Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
13-02-2023
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
#13-02-2023
d={'Jan':1,'Feb':2,'Mar':3}}
SyntaxError: unmatched '}'
d={'Jan':1,'Feb':2,'Mar':3}
d
{'Jan': 1, 'Feb': 2, 'Mar': 3}
d.keys()
dict_keys(['Jan', 'Feb', 'Mar'])
d.values()
dict_values([1, 2, 3])
for i in d:
    print(i)

    
Jan
Feb
Mar
for i,v in d.items():
    print(i,v)

    
Jan 1
Feb 2
Mar 3
# Gather input(int) from user and print the same in words
12
12
'Twelve'
'Twelve'
#Contstrain the value 0 to 9
num_words={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
num_words
{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
n=input('Enter a digit')
Enter a digit4
n
'4'
'four'
'four'
num_words.keys()
dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9])
n==num_words.keys()
False
num_words.keys()[1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    num_words.keys()[1]
TypeError: 'dict_keys' object is not subscriptable
for key in num_words:
    if int(n)==key:
        print(num_words[int(n)])

        
four
# by makinfg it as afunc
def num_to_words(num):
    '''Returns word equivalent for a given digit'''
    for key in num_words:
    if int(n)==key:
        print(num_words[int(n)])
        
SyntaxError: expected an indented block after 'for' statement on line 3
# by making it is a function
def num_to_words(num):
    '''Returns word equivalent for a given digit'''
    for key in num_words:
        if num==key:
            print(num_words[num])

            
num_to_words(int(n))
four
def num_to_words(num):
    '''Returns word equivalent for a given digit'''
    for key in num_words:
        if num==key:
            return num_words[num]

        
num_to_words(3)
'three'
num_to_words(9)
'nine'
num_to_words(10)
# 10 is not in the dict
x=num_to_words(10)

X
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    X
NameError: name 'X' is not defined. Did you mean: 'x'?
x
num_words[10]
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    num_words[10]
KeyError: 10
num_words.get(9)
'nine'
num_words.get(10)
def num_to_words_2(num):
    '''Returns word equivalent for a given digit'''
    return num_words.get(num)

num_to_words_2(int(input('enter a digit'\n)))
SyntaxError: unexpected character after line continuation character
num_to_words_2(int(input('enter a digit')))
enter a digit3
'three'
num_to_words_2(int(input('enter a digit\n')))
enter a digit
7
'seven'
num_to_words_2(int(input('enter a digit\n')))
enter a digit
12
def num_to_words_2(num):
    '''Returns word equivalent for a given digit'''
    return num_words.get(num,'Enter a valid digit from 0 to 9)
                         
SyntaxError: incomplete input
def num_to_words_2(num):
    '''Returns word equivalent for a given digit'''
    return num_words.get(num,'Enter a valid digit from 0 to 9')

num_to_words_2(int(input('enter a digit\n')))
enter a digit
12
'Enter a valid digit from 0 to 9'


#### Break and continue statements
# Break
# if a no is divisible by 3 then stop the loop

for i in range(1,10):
    if (i%3==0):
        break
    print(i)

    
1
2
for i in range(1,10):
    if (i%3==0):
        continue
    print(i)

    
1
2
4
5
7
8

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Break & Continue.py
1
2
Outside loop

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Break & Continue.py
1
2
Outside loop
1
2
4
5
7
8
Outside loop

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Break with For else.py
1
2
Outside everything

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Break with For else.py
1
2
Outside everything
1
2
3
4
5
6
7
8
9
inside else
Outside everything

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Break with For else.py
1
2
Outside everything
1
2
3
4
5
6
7
8
9
inside else
Outside everything
1
2
3
4
5

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Break with For else.py
1
2
Outside everything
1
2
3
4
5
6
7
8
9
inside else
Outside everything
1
2
3
4
5
1
2
3
4
5
6
7
8
9
inside else
Outside everything

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Break with For else.py
1
2
Outside everything
1
2
3
4
5
6
7
8
9
inside else
Outside everything
1
2
3
4
5
1
2
3
4
5
6
7
8
9
inside else
Outside everything
1
i=2inside if
Outside everything

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Use of For else.py
Enter Password Abcd
Enter password again,Attempted 1 times 2 attempts left
Enter PasswordAbcd@1234

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Use of For else.py
Enter Password12
Enter password again,Attempted 1 times 2 attempts left
Enter Passwordavsdf
Enter password again,Attempted 2 times 1 attempts left
Enter Passwordsdfg
Enter password again,Attempted 3 times 0 attempts left
Suspicious
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Use of For else.py
Enter PasswordAbcd@1234
Login successful
>>> 
>>> 
>>> num_words
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    num_words
NameError: name 'num_words' is not defined
>>> num_words={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
>>> def num_to_words_2(num):
...     '''Returns word equivalent for a given digit'''
...     return num_words.get(num,'Enter a valid digit from 0 to 9')
... 
>>> 
>>> num_to_words_2(1)
'one'
>>> num_to_words_2('1')
'Enter a valid digit from 0 to 9'
>>> '2'+2
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    '2'+2
TypeError: can only concatenate str (not "int") to str
>>> n = 2
>>> m = "3"
>>> try:
...     n+m
... except:
...     print('please make sure both varibles are of same data type')
... 
...     
please make sure both varibles are of same data type
