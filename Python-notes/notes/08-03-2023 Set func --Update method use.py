Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


# 08-03-2023
#  Set Updation methods
x1 = {'a','c','b'}
x2={1,5,9}
x1.union(x2)
{1, 5, 9, 'c', 'b', 'a'}
x1
{'c', 'b', 'a'}
x2
{1, 5, 9}
# update for every operation (inter. , union, difference)
x1.update(x2)
x1
{1, 5, 9, 'c', 'b', 'a'}
# x1 is updated
x3 ={'a','b','c'}
x3
{'c', 'b', 'a'}
x3.union(x2)
{1, 5, 9, 'c', 'b', 'a'}
x3.union(x2)==x1.update(x2)
False
x3
{'c', 'b', 'a'}
x2
{1, 5, 9}
x1
{1, 5, 9, 'b', 'a', 'c'}
x3
{'c', 'b', 'a'}
x4=x3.union(x2)
x4
{1, 5, 9, 'c', 'b', 'a'}
x1.update(x2) ### Returns none ,but modifies x1
### update doent return any thing
x3
{'c', 'b', 'a'}
x3.union(x2)==x1
True
x3.union(x2)==x1.update(x2) ## Return False because RHS ret. None and LHS ret the union set
False


set_1={1,2,3}
set_2={7,8,9}
set_1.union(set_2)
{1, 2, 3, 7, 8, 9}
set_1.update(set_2)
set_1
{1, 2, 3, 7, 8, 9}
set_2
{8, 9, 7}
{8, 9, 7}
{8, 9, 7}
set_3={1,2,3} # values same as set_1
set_3.union(set_2)
{1, 2, 3, 7, 8, 9}
set_3
{1, 2, 3}
set_4={1,2,3}
x=set_3.union(set_2)
x
{1, 2, 3, 7, 8, 9}
y= set_3.update(set_2)
y
set_3
{1, 2, 3, 7, 8, 9}
print(y)
None
type(y)
<class 'NoneType'>
l=[1,2,3]
def func(list_x):
    s=sum(list_x)
    list_x.append(s)
    return None

func([1,2,3])
l
[1, 2, 3]
func(l)
l
[1, 2, 3, 6]
x4
{1, 5, 9, 'c', 'b', 'a'}
set_4
{1, 2, 3}
set_2
{8, 9, 7}
set_4|=set_2 #set_4=set_4|set_2
set_4
{1, 2, 3, 7, 8, 9}
del set_1
set_1={1,2,3}
#Intersection Update
set_1. intersection(set_2)
set()
set_5={2,7,10}
set_2.intersection(set_5)
{7}
set_2
{8, 9, 7}
set_5
{2, 10, 7}
set_2.intersection_update(set_5)
set_2
{7}
set_2={7,8,9}
set_2
{8, 9, 7}
set_2 &= set_5  # &= sign for above intersection_update
set_2
{7}

# Difference_update

set_1
{1, 2, 3}
set_5
{2, 10, 7}
set_1.difference(set_5)
{1, 3}
set_5.difference(set_1)
{10, 7}
set_1.difference_update(set_5)
set_1
{1, 3}
set_1={1,2,3}
set_5.difference_update(set_1)
set_5
{10, 7}
set_5.update({2})
set_5
{2, 10, 7}
set_1-=set_5 # -= operator used for difference_update
set-1
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    set-1
TypeError: unsupported operand type(s) for -: 'type' and 'int'
set_1
{1, 3}
set_1={1,2,3}

# Symmetric_difference
>>> 
>>> set_1.symmetric_difference(set_5)
{1, 3, 7, 10}
>>> # it excludes all the common elements
>>> set_1.symmetric_difference_update(set_5)
>>> set_1
{1, 10, 3, 7}
>>> 
>>> dir(set)
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
>>> ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
