Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-02-2023, raises a value error if even no is present.py
a=[1,2,3] # Contains even num2
find_even(a)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    find_even(a)
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-02-2023, raises a value error if even no is present.py", line 14, in find_even
    raise ValueError('No even no found')
ValueError: No even no found
b=[11,5,7]
find_even(b)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    find_even(b)
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-02-2023, raises a value error if even no is present.py", line 14, in find_even
    raise ValueError('No even no found')
ValueError: No even no found

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-02-2023, raises a value error if even no is present.py
a=[1,2,3]
find_even(a)
b=[11,5,7]
find_even(b)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    find_even(b)
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/16-02-2023, raises a value error if even no is present.py", line 14, in find_even
    raise ValueError('No even no found')
ValueError: No even no found
### You have to iterate all the elements until you find an even no
[1,2,3]
[1, 2, 3]
[2,1,3]
[2, 1, 3]
[3,1,2]
[3, 1, 2]

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/demo_while.py =
0
1
2
3
4

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
i=0,l[i]=1
while loop condition-> (l[i]%2)!=0:True

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
i=0,l[i]=1
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
i=0,l[i]=1
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
i=1,l[i]=3
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
i=2,l[i]=5
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py", line 7, in <module>
    while (l[i]%2)!=0:#Keep on checking untill[i] is odd
IndexError: list index out of range

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
i=0,l[i]=1
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
i=1,l[i]=3
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
i=2,l[i]=5
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py", line 8, in <module>
    while (l[i]%2)!=0:#Keep on checking untill[i] is odd
IndexError: list index out of range

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py", line 16, in <module>
    raise ValueError('No even no found')
ValueError: No even no found
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
i=0,l[i]=1
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
i=1,l[i]=3
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
i=0,l[i]=1
l[i]%2,1
while loop condition-> (l[i]%2)!=0:True
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/Even no ,Raisevalue error,while loop.py
>>> find_even_2([1,2,3,4])
