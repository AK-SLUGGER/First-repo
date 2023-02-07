Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l_1=[1,2,3,4]
l_2=[1,2,8,7]
l=l_1+L-2
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    l=l_1+L-2
NameError: name 'L' is not defined
l=l_1+l_2
l3=[]
for i in l:
    if l.count(i)==1:
        l3.append(i)

        
print(l3)
[3, 4, 8, 7]
l3=[]
for i in l:
    print('i= ',i)
    print('l.count: ',l.count(i))
    if l.count(i)==1:
        print('before append',l3)
        l3.append(i)
        print('after append',l3)

        
i=  1
l.count:  2
i=  2
l.count:  2
i=  3
l.count:  1
before append []
after append [3]
i=  4
l.count:  1
before append [3]
after append [3, 4]
i=  1
l.count:  2
i=  2
l.count:  2

i=  8
l.count:  1
before append [3, 4]
after append [3, 4, 8]
i=  7
l.count:  1
before append [3, 4, 8]
after append [3, 4, 8, 7]
#solution 2nd to remove the duplicates from List
l1=[1,2,3,4]
l2=[1,2,8,7]
l3=[3,4,8,7]
l_total=l1+l2+l3 #concatenated list.
print('l_total',l_total)
l_total [1, 2, 3, 4, 1, 2, 8, 7, 3, 4, 8, 7]
l_remove=[]#assign empty list
[l_remove.append(x)for x in l_total if x not in l_remove]
[None, None, None, None, None, None]
print(l_remove)
[1, 2, 3, 4, 8, 7]



#Solutions for unique nos
a=[1,2,3,4,5]
b=[4,5,6,7,8]
#[1,2,3,6,7,8]
c=a+[i for i in b if i not in a]
c
[1, 2, 3, 4, 5, 6, 7, 8]
[i for i in b if i not in a]
[6, 7, 8]
############
l1[1,2,3,4]
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    l1[1,2,3,4]
TypeError: list indices must be integers or slices, not tuple
l1=[1,2,3,4]
l2=[1,2,8,7]
l3=l1+l2
l4=[]
for i in l3:
    if i not in l1:
        print('not dup')
        l4.append(i)
        if i not in l2:
            l4.append(i)

            
not dup
not dup
l4
[8, 7]
[i for i in l1 not in l2]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    [i for i in l1 not in l2]
TypeError: 'bool' object is not iterable
[i for i in l1 if i not in l2]
[3, 4]
[i for i in l2 if i not in l1]
[8, 7]
l5=[i for i in l1 if i not in l2]+[i for i in l2 if i not in l1]
l5
[3, 4, 8, 7]
l1
[1, 2, 3, 4]
>>> l2
[1, 2, 8, 7]
>>> l3
[1, 2, 3, 4, 1, 2, 8, 7]
>>> l3=[3,4,8,7]
>>> l1
[1, 2, 3, 4]
>>> l2
[1, 2, 8, 7]
>>> l3
[3, 4, 8, 7]
>>> l4=l1+l2+l3
>>> final_list=[]
>>> for i in l4:
...     if i not in final_list:
...         final_list.append(i)
... 
...         
>>> final_list
[1, 2, 3, 4, 8, 7]
>>> l4=l1=l2
>>> l4=l1+l2
>>> final_list=[]
... for i in l4:
...     if i not in final_list:
...         final_list.append(i)
...         
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> l4=l1+l2
>>> final_list=[]
>>> for i in l4:
...     if i not in final_list:
...         final_list.append(i)
... 
...         
>>> final_list
[1, 2, 8, 7]
