Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#2-03-2023
#Sets
x1={1,2,3}
x2={3,4,5}
x1.symmetric_difference(x2)
{1, 2, 4, 5}
x1^x2
{1, 2, 4, 5}
a={1,2,3,300,30}
b={40,10,20,30}
c={100,200,300,400}
a^b^c
{1, 2, 3, 100, 200, 40, 10, 400, 20}
a.symmetric_difference(b)
{1, 2, 3, 40, 10, 300, 20}
a.symmetric_difference(b,c)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.symmetric_difference(b,c)
TypeError: set.symmetric_difference() takes exactly one argument (2 given)
a.symmetric_difference(b^c)
{1, 2, 3, 100, 40, 200, 10, 400, 20}
a.symmetric_difference(b)
{1, 2, 3, 40, 10, 300, 20}
type(a.symmetric_difference(b))
<class 'set'>
a.symmetric_difference(b).symmetric_difference(c)
{1, 2, 3, 100, 200, 40, 10, 400, 20}
a.symmetric_difference(b).symmetric_difference(c)==a^b^c
True
a.symmetric_difference(b).symmetric_difference(c)==a.symmetric_difference9b^c)
SyntaxError: unmatched ')'
a.symmetric_difference(b).symmetric_difference(c)==a.symmetric_difference(b^c)
True
a^b
{1, 2, 3, 40, 10, 300, 20}
b^b
set()
b^a
{1, 2, 3, 20, 40, 10, 300}
b^a==a^b
True
x1.isdisjoint(x2)
False

q={1,2,3}
r={9,8,7}
q.isdisjoint(r)
True
help(q.isdisjoint)
Help on built-in function isdisjoint:

isdisjoint(...) method of builtins.set instance
    Return True if two sets have a null intersection.

q&r
set()
(q&r)==set()
True
q.isdisjoint(r)
True
(q&r)==set()# Find intersection and check whether it is empty or not
True
q.isdisjoint(r)
True
r
{8, 9, 7}
r-{8}# removes the member
{9, 7}
s1={8,0,1}
r
{8, 9, 7}
r.isdisjoint(s1)
False
r.intersection(s1)
{8}
>>> r.isdisjoint(s1-{8})
True
>>> q&r
set()
>>> q|r
{1, 2, 3, 7, 8, 9}
>>> q.issubset({1,2,3,4,5})
True
>>> q<={1,2,3,4,5}
True

>>> r
{8, 9, 7}
>>> q,=r
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    q,=r
ValueError: too many values to unpack (expected 1)
>>> q<=r
False
>>> q.issubset(r)
False
>>> q.issubset(q)
True
>>> q<=q
True
>>> x1
{1, 2, 3}
>>> x2
{3, 4, 5}
>>> x3={1,2,3,4}
>>> x1<x3
True
>>> x3<x1
False
>>> x1<=x1
True
>>> x1<x1
False
x1
x1.issuperset(x2)
False
x1.issuperset(x3)
False
x3.issuperset(x1)
True
x1.subset(x3)
True
x3>=x1
True
x1>=x3
False
x1>=x1
True
x3>x1
True Proper superset
