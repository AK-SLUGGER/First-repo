Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#

## Find Sum of Digits

12233
12233
1+2+2+3+3
11
x = 21321321

# Convert integer to a List(or any sequence)

x_1=[x]

x-1
21321320
x
21321321
x_1
[21321321]
# converted in a List

l=12233

s=0

for i in str(l):
    s=s+int(i)

    
s
11

for i in List(str(l)):
    i

    
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    for i in List(str(l)):
NameError: name 'List' is not defined. Did you mean: 'list'?
for i in list(str(l)):
    i

    
'1'
'2'
'2'
'3'
'3'

s=0
for i in str(l):
    s+=int(i)   #s = s+i

    
s
11

r='abc'
r*=2
r
'abcabc'
#r=r*2
r*2
'abcabcabcabc'

11=[1,2,3,4]
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
l1=[1,2,3,4]
l2=[1,2,9,6]

for i in l1:
    if i in l2:
        l1.remove(i)

        
l2
[1, 2, 9, 6]
l1
[2, 3, 4]


#l1[0] ->1
#l1 =[1,2,3,4]
l1=[1,2,3,4]
for i in l1:
    print(f'outside if i ={i},l1={l1}')
    if i in l2:
        l1.remove(i)
        print(f'inside if i=[i},l1={l1}')
        
SyntaxError: incomplete input
for i in l1:
    print(f'outside if i ={i},l1={l1}')
    if i in l2:
        l1.remove(i)
        print(f'inside if i=[i},l1={l1}')
        
SyntaxError: incomplete input
for i in l1:
    print(f'outside if i ={i},l1={l1}')
    if i in l2:
        l1.remove(i)
        print(f'inside if i ={i},l1={l1}')
        print(f'after if i ={i},l1={l1}')

        
outside if i =1,l1=[1, 2, 3, 4]
inside if i =1,l1=[2, 3, 4]
after if i =1,l1=[2, 3, 4]
outside if i =3,l1=[2, 3, 4]
outside if i =4,l1=[2, 3, 4]
for i in l1:
    print(f'outside if i ={i},l1={l1}')
    if i in l2:
        l1.remove(i)
        print(f'inside if i ={i},l1={l1}')
    print(f'after if i ={i},l1={l1}')

    
outside if i =2,l1=[2, 3, 4]
inside if i =2,l1=[3, 4]
after if i =2,l1=[3, 4]
outside if i =4,l1=[3, 4]
after if i =4,l1=[3, 4]


# ASCII values

ord('a')
97
ord('Z')
90
ord('A')
65
ord('z')
122

s='safsafdsafdsAdsfedgh'

# Break the loop if  a character is not lowercase using ASCII
#value using Break Keyword
for i in s:
...     if ord(i) <97 or ord(i)>122:
...         break
...     print(i)
... 
...     
s
a
f
s
a
f
d
s
a
f
d
s
>>> 
>>> #break the loop if a character is not lowercase using
>>> # .islower() method value using break keyword
>>> 
>>> for i in s:
...     if not i.islower():
...         break
...     print(i)
... 
...     
s
a
f
s
a
f
d
s
a
f
d
s
