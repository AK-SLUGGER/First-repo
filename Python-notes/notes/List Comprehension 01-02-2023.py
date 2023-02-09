Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a,b=(1,2)
a
1
b
2
#Tuple unpacking
a,b,c=(1,2)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a,b,c=(1,2)
ValueError: not enough values to unpack (expected 3, got 2)
a,b,c=(1,2,3)
a
1
b
2
c
3
a,b=((1,2),3)
a
(1, 2)
b
3
def func(x,y):
    '''it consumes 2 numbers x 
       returns diff of x & y,sum of x & y
       '''
    return x-y,x+y
g=func(2,3)
SyntaxError: invalid syntax
g=func(2,3)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    g=func(2,3)
NameError: name 'func' is not defined
def func(x,y):
    '''it consumes 2 numbers x 
       returns diff of x & y,sum of x & y
       '''
    return x-y,x+y

g=func(1,2)
g
(-1, 3)
#list comphresension
#list comprehension
l=[]
#cretae a list l that contains only even int from 0-10
[0,2,4,6,8,10]
[0, 2, 4, 6, 8, 10]
for i in range(0,11,2):
    l.append(i)

    
l
[0, 2, 4, 6, 8, 10]
list2=[i for i in range(0,11,2)]
list2
[0, 2, 4, 6, 8, 10]
#method#1
# iterate a for loop with range as req start=0,stop=11,step=2
# value ret by range is append to an empty list
#Method # 2
# list2a=[<loop variable> || <for loop>] # empty
# < for loop > ->for i in range(0,11,2) # COLONS ARE OMITTED
#<LOOP VARIABLE> ->i
list2= [i for i in range(0,11,2)]
list2
[0, 2, 4, 6, 8, 10]
# goal of list comprehension to create a new list
[ s for s in range (1,10) ]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
p=[]
for s in range(1,10):
    p.append(s)

    
p
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'123456789'
'123456789'
#create  a list of digits and each ele in list should be of type int
q=[]
s='123456789'
list(s)
['1', '2', '3', '4', '5', '6', '7', '8', '9']
q
[]
for i in s:
    i int =int(i) # convert each char in str to int
    
SyntaxError: invalid syntax
for i in s:
    i_int =int(i) # convert each char in str to int
    q.append(i_int)#append the converted int to the list

    
q
[1, 2, 3, 4, 5, 6, 7, 8, 9]
# Verify whether each element of list q is int
for j in q:
    print(type(j))

    
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
<class 'int'>
for j in q:
    print(isinstance(j,int))

    
True
True
True
True
True
True
True
True
True
q.append('21')
q
[1, 2, 3, 4, 5, 6, 7, 8, 9, '21']
for j in q:
    print(isinstance(j,int))

    
True
True
True
True
True
True
True
True
True
False
q.pop()
'21'
q
[1, 2, 3, 4, 5, 6, 7, 8, 9]
q_comprehension = [int (i) for i in s]
q_comprehension
[1, 2, 3, 4, 5, 6, 7, 8, 9]
q
[1, 2, 3, 4, 5, 6, 7, 8, 9]
q_comprehension check type = [isinstance(i,int) for i in q_comprehension]
SyntaxError: invalid syntax
q_comprehension_check_type = [isinstance(i,int) for i in q_comprehension]
>>> q_comprehension_check_type
[True, True, True, True, True, True, True, True, True]
>>> q_comprehension_check_type = [(isinstance(i,int),i) for i in q_comprehension]
>>> q_comprehension_check_type
[(True, 1), (True, 2), (True, 3), (True, 4), (True, 5), (True, 6), (True, 7), (True, 8), (True, 9)]
>>> q_comprehension_check_type
[(True, 1), (True, 2), (True, 3), (True, 4), (True, 5), (True, 6), (True, 7), (True, 8), (True, 9)]
>>> # without comprehension
>>> s
'123456789'
>>> w=[]
>>> w_t_c=[]
>>> counter=0
>>> for i in s:
...     w.append(int(i))
...     w_t_c.append(isinstance(w[counter],int))
...     counter =counter +1
... 
...     
>>> w
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> w_t_c
[True, True, True, True, True, True, True, True, True]
>>> counter=0
>>> w=[]
>>> w_t_c=[]
>>> for i in s:
...     w.append(int(i))
...     w_t_c.append((isinstance(w[counter],int),w[counter]))
...     counter =counter +1
... 
...     
>>> w
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> w_t_c
[(True, 1), (True, 2), (True, 3), (True, 4), (True, 5), (True, 6), (True, 7), (True, 8), (True, 9)]
