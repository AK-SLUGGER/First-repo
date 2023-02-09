Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l1=[1,1,2,3,4]
l2=[2,3,7,5]
l3=l1+l2
l3
[1, 1, 2, 3, 4, 2, 3, 7, 5]
l4=[]
for i in l3:
    if i not in l1:
        #print('non dup')
            l4.append(i)
        if i not in l2:
            l4.append(i)
            
SyntaxError: unindent does not match any outer indentation level

for i in l3:
    if i not in l1:
        #print('non dup')
            l4.append(i)
        if i not in l2:
             l4.append(i)
             
SyntaxError: unindent does not match any outer indentation level

for i in l3:
    if i not in l1:
        print(f"i={i}")
        l4.append(i)
        print(f"1st if l4={l4}")
        if i not in l2:
            l4.append(i)
            prtn(f"2nd if l4 ={l4}")

            
i=7
1st if l4=[7]
i=5
1st if l4=[7, 5]
l4
[7, 5]
for i in l3:
    print(f"i={i]")
    if i not in l4:
        if i not in l1:
            
SyntaxError: f-string: unmatched ']'
l1=[1,1,2,3,4]
>>> l2=[2,3,7,5]
>>> l3=l1+l2
>>> l4=[]
>>> for i in l3:
...     print(f"i={i]")
...     if i not in l4:
...         if i not in l1:
...             
SyntaxError: f-string: unmatched ']'
>>> for i in l3:
...     print(f"i={i}")
...     if i not in l4:
...         if i not in l1:
...             l4.append(i)
...         print(f"1st if l4={l4}")
...         if i not in l2:
...             l4.append(i)
...             print(f"2nd if l4 ={l4}")
... 
...             
i=1
1st if l4=[]
2nd if l4 =[1]
i=1
i=2
1st if l4=[1]
i=3
1st if l4=[1]
i=4
1st if l4=[1]
2nd if l4 =[1, 4]
i=2
1st if l4=[1, 4]
i=3
1st if l4=[1, 4]
i=7
1st if l4=[1, 4, 7]
i=5
1st if l4=[1, 4, 7, 5]
