Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.


#10/02/2023
states={'Karnataka':{'capitals':'Bengaluru','sweet':'MysorePak'},'Maharashtra':{'capital':'Mumbai','sweet':'Jalebi'},'Telangana':{'capital':'Hyderabad','sweet':'kurbanika meta'}}

# states is a nested Dictonary

dir(states)  #Available methods
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
states.pop('Telanagana')  #Return the value of the specified key
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    states.pop('Telanagana')  #Return the value of the specified key
KeyError: 'Telanagana'
states.pop('Telangna') #Return the value of the specified key
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    states.pop('Telangna') #Return the value of the specified key
KeyError: 'Telangna'
states.pop('Telangana') #Return the value of the specified key
{'capital': 'Hyderabad', 'sweet': 'kurbanika meta'}

states # Check what has changed in the states Dictionary
{'Karnataka': {'capitals': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}}
states={'Karnataka':{'capitals':'Bengaluru','sweet':'MysorePak'},'Maharashtra':{'capital':'Mumbai','sweet':'Jalebi'},'Telangana':{'capital':'Hyderabad','sweet':'kurbanika meta'}}
states.popitem() # removes the last key value pair added and
('Telangana', {'capital': 'Hyderabad', 'sweet': 'kurbanika meta'})
#returns it as a tuple


states['usa']='california'

states['Japan']='Tokyo'
states
{'Karnataka': {'capitals': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}, 'usa': 'california', 'Japan': 'Tokyo'}
states.popitem()
('Japan', 'Tokyo')
states.keys()
dict_keys(['Karnataka', 'Maharashtra', 'usa'])
states.popitem()
('usa', 'california')
states={'Karnataka':{'capitals':'Bengaluru','sweet':'MysorePak'},'Maharashtra':{'capital':'Mumbai','sweet':'Jalebi'},'Telangana':{'capital':'Hyderabad','sweet':'kurbanika meta'}}

# Change key to correct spelling =>Replace''Telangana'' with 'Telanagana'
#.pop(<key_name>)=>Returns the value & Remove the key from the dict
#dict_name[<key_name> is present =<value_name>
#case1:<key_name>is present is present=>value is upated
#case2:<key_name> is not present => a New key-value pair is added to the dictionary

states.keys()
dict_keys(['Karnataka', 'Maharashtra', 'Telangana'])
'Telangana'in states.keys()
True
'Telanagana' in states.keys()
False

#case2

#Remove 'Telanagana'and then add'Telangana' then assign the previous value
states['Telangana']=states.pop('Telanagana')
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    states['Telangana']=states.pop('Telanagana')
KeyError: 'Telanagana'
states['Telanagana']=states.pop('Telangana')
'Telanagana' in states.keys()
True
'Telangana' in states.keys()
False
states
{'Karnataka': {'capitals': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}, 'Telanagana': {'capital': 'Hyderabad', 'sweet': 'kurbanika meta'}}
states.pop()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    states.pop()
TypeError: pop expected at least 1 argument, got 0


[1,2,3].pop()
3
s=[1,2,3]
s.pop() # Returns and removes the value at Last index
3
s
[1, 2]
s.remove(2)  # List
s
[1]
states['Punjab']  # You can't access a key that is not ready
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    states['Punjab']  # You can't access a key that is not ready
KeyError: 'Punjab'
states['Punjab']  # You can't access a key that is not already present
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    states['Punjab']  # You can't access a key that is not already present
KeyError: 'Punjab'


states[['Karnataka']]  # Unhashable please research
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    states[['Karnataka']]  # Unhashable please research
TypeError: unhashable type: 'list'
states
{'Karnataka': {'capitals': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}, 'Telanagana': {'capital': 'Hyderabad', 'sweet': 'kurbanika meta'}}
states.clear()  ## clear all the items of dictionary and make it an 'empty dictionary'
# 'Empty Dictionary'
states
{}
states={'Karnataka':{'capitals':'Bengaluru','sweet':'MysorePak'},'Maharashtra':{'capital':'Mumbai','sweet':'Jalebi'},'Telangana':{'capital':'Hyderabad','sweet':'kurbanika meta'}}

states
{'Karnataka': {'capitals': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}, 'Telangana': {'capital': 'Hyderabad', 'sweet': 'kurbanika meta'}}
states['Telangana']
{'capital': 'Hyderabad', 'sweet': 'kurbanika meta'}
states['Telangana'].keys()
dict_keys(['capital', 'sweet'])
type(states['Telangana'])
<class 'dict'>
states['Telangana'].pop('capital')
'Hyderabad'
states['Telangana']
{'sweet': 'kurbanika meta'}
states
{'Karnataka': {'capitals': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}, 'Telangana': {'sweet': 'kurbanika meta'}}
states={'Karnataka':{'capitals':'Bengaluru','sweet':'MysorePak'},'Maharashtra':{'capital':'Mumbai','sweet':'Jalebi'},'Telangana':{'capital':'Hyderabad','sweet':'kurbanika meta'}}
states.get('Maharashtra')
{'capital': 'Mumbai', 'sweet': 'Jalebi'}
states.get('Bihar')
states['Bihar']
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    states['Bihar']
KeyError: 'Bihar'
states.get ('Bihar')
a= states.get('Bihar')
a
print(a)
None
a= states.get ('Bihar',-1)  # returns specified value as 2nd argument
a
-1
a=states.get('Bihar','State to be added')
a
'State to be added'


d1={'a':100,'b':200,'c':300}
d2={'b':'ABCD','d':'WXYZ'}
D1
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    D1
NameError: name 'D1' is not defined. Did you mean: 'd1'?
d1
{'a': 100, 'b': 200, 'c': 300}
d2
{'b': 'ABCD', 'd': 'WXYZ'}
d1.update(d2)
d1  # The value corresponding to 'b' changed from 200 ->'ABCD',
{'a': 100, 'b': 'ABCD', 'c': 300, 'd': 'WXYZ'}
# A new key "d" is added to the dictionary

# .update()Merges a dictionary with another dictionary or with an iterable of key_value pairs
d2
{'b': 'ABCD', 'd': 'WXYZ'}
d1
{'a': 100, 'b': 'ABCD', 'c': 300, 'd': 'WXYZ'}
d2.update(d1)
D2
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    D2
NameError: name 'D2' is not defined. Did you mean: 'd2'?
d2
{'b': 'ABCD', 'd': 'WXYZ', 'a': 100, 'c': 300}
d1
{'a': 100, 'b': 'ABCD', 'c': 300, 'd': 'WXYZ'}
d1.update(b=200,p=1000)
d1
{'a': 100, 'b': 200, 'c': 300, 'd': 'WXYZ', 'p': 1000}
d1={'a':100,'b':200,'c':300}
d1.update(b=2000,p=1000)
d1
{'a': 100, 'b': 2000, 'c': 300, 'p': 1000}
d2
{'b': 'ABCD', 'd': 'WXYZ', 'a': 100, 'c': 300}
d2.update([('d':'Update'),('12,'Twelve')])
                           
SyntaxError: unterminated string literal (detected at line 1)
>>> d2.update([('d':'Update'),('12,"Twelve")])
...                            
SyntaxError: unterminated string literal (detected at line 1)
>>> d2.update([('d':'Update'),('12',"Twelve")])
...                            
SyntaxError: invalid syntax
>>> d2.update([('d','Update'),('12',"Twelve")])
...                            
>>> d2
...                            
{'b': 'ABCD', 'd': 'Update', 'a': 100, 'c': 300, '12': 'Twelve'}
>>> states
...                            
{'Karnataka': {'capitals': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}, 'Telangana': {'capital': 'Hyderabad', 'sweet': 'kurbanika meta'}}
>>> d2.update(states)
...                            
>>> d2
...                            
{'b': 'ABCD', 'd': 'Update', 'a': 100, 'c': 300, '12': 'Twelve', 'Karnataka': {'capitals': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}, 'Telangana': {'capital': 'Hyderabad', 'sweet': 'kurbanika meta'}}
>>> 
>>> 
>>> # States['Telangana']=ststes.pop('Telangana')
...                            
>>> 
>>> # dict_name[<new_key>]=dict_name.pop(<old_keys>)Replace old Key
...                            
>>> #with new key and preserve the value
...                            
>>> d=dict(a=1,b=2)  # one more way to create dict
...                            
>>> d
...                            
{'a': 1, 'b': 2}
