Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Different functions which are used in Lists
sum[1,2,3]
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    sum[1,2,3]
TypeError: 'builtin_function_or_method' object is not subscriptable
sum([1,2,3])
6
sum([1,2,3.9])
6.9
min
<built-in function min>
n=[ i for i in range(1,10_001)]
n

n[-1]
10000
n[0]
1

#create a variable to hold sum. initlz it to 0
#iterate over n and add each value to the sum holder variable
counter=0
for i in n:
    counter=counter+1

    
counter
10000
for i in n:
    counter=counter+i

    
counter
50015000
sum(n)
50005000

n=1_000_000_000
# use of maths formula for addition
n*(n+1)//2# sum of 1st billion nos
500000000500000000
n=[i for i in range(1,10_001)]

n[0]
1
n[-1]
10000
max(n)
10000
min(n)
1
l=[1,2,3,4,99,8,13131,83]
max(l)
13131
min(l)
1
l.index(max(l))
6
l[6]
13131
a=['d','a','b','c']
max(a)
'd'
min(a)
'a'
a['bd','ba','ab','ac']
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a['bd','ba','ab','ac']
TypeError: list indices must be integers or slices, not tuple
a=['bd','ba','ab','ac']
max(a)
'bd'
min(a)
'ab'
a['bd','ba','ab','ac',1212]
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    a['bd','ba','ab','ac',1212]
TypeError: list indices must be integers or slices, not tuple
a=['bd','ba','ab','ac',1212]
max(a)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    max(a)
TypeError: '>' not supported between instances of 'int' and 'str'
min(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    min(a)
TypeError: '<' not supported between instances of 'int' and 'str'


#Dcitonary
#Use of dictionary in Python
# keys , values

num_words={1:'one',2:'two',3:'three'}
num_words
{1: 'one', 2: 'two', 3: 'three'}
num_words.keys()
dict_keys([1, 2, 3])
num_words.values()
dict_values(['one', 'two', 'three'])
num_words[1]
'one'
num_words[2]
'two'
num_words[-1]
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    num_words[-1]
KeyError: -1
num_words_2={'one':1,'two':3.0,'three':'tree'}
num_words-2
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    num_words-2
TypeError: unsupported operand type(s) for -: 'dict' and 'int'
num_words_2
{'one': 1, 'two': 3.0, 'three': 'tree'}
num_words_2.keys()
dict_keys(['one', 'two', 'three'])
num_words_.values()
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    num_words_.values()
NameError: name 'num_words_' is not defined. Did you mean: 'num_words'?
num_words_2.values()
dict_values([1, 3.0, 'tree'])
>>> num_words_2['one']
1
>>> num_words_2[3.0]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    num_words_2[3.0]
KeyError: 3.0
>>> 
>>> 
>>> #Keys hve to be immutable ,Values can be mutable
>>> num_words_3 ={'Virat':18,'Rohit':45}
>>> 
>>> dict_words_3={('a','b','c'):18}
>>> dict_words_3
{('a', 'b', 'c'): 18}
>>> dict_coordinate ={('x1','y1','z1'):(0,0,0),('x2','y2','z2'):(1,2,3)}
>>> dict_coordinate
{('x1', 'y1', 'z1'): (0, 0, 0), ('x2', 'y2', 'z2'): (1, 2, 3)}
>>> dict_coordinate[('x1','y1','z1')]
(0, 0, 0)
>>> dict_coordinate[('x1','y1','z1')]=(1,0,0)#values are mutable in dictonaries
>>> dict_coordinate[('x1','y1','z1')]
(1, 0, 0)
>>> dict_coordinate[('x1','y1','z1')]=1,23  #packes as tuple so it gives errors
>>> dict_coordinate[('x1','y1','z1')]
(1, 23)
>>> dict_coordinate[('x1','y1','z1')]=1 2332
SyntaxError: incomplete input
>>> dict_coordinate[('x1','y1','z1')]
(1, 23)
>>> 
>>> 
>>> {} # empty dictonary , observe no colon(:)
{}
>>> type{}
SyntaxError: invalid syntax
>>> type({})
<class 'dict'>
