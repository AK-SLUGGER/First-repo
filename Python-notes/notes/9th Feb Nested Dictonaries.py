Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Dictonaries
dict
<class 'dict'>
capitals=(('india','New Delhi'),
          ('england','london'),
          ('srilanka','colambo'),
          ('japan','tokyo'))
capitals
(('india', 'New Delhi'), ('england', 'london'), ('srilanka', 'colambo'), ('japan', 'tokyo'))
capitals_dict=dict(capitals)
capitals_dict
{'india': 'New Delhi', 'england': 'london', 'srilanka': 'colambo', 'japan': 'tokyo'}
capitals = ((['India'],'New Delhi'),
            ('England','London'),
            ('Sri Lanka','Colmbo'),
            ('Japan','Tokyo'))
capitals_dict = dict(capitals)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    capitals_dict = dict(capitals)
TypeError: unhashable type: 'list'
capitals_dict
{'india': 'New Delhi', 'england': 'london', 'srilanka': 'colambo', 'japan': 'tokyo'}
capitals_dict['India']='Delhi'
capitals_dict
{'india': 'New Delhi', 'england': 'london', 'srilanka': 'colambo', 'japan': 'tokyo', 'India': 'Delhi'}
capitals_dict['USA']='Washington DC'
capitals_dict
{'india': 'New Delhi', 'england': 'london', 'srilanka': 'colambo', 'japan': 'tokyo', 'India': 'Delhi', 'USA': 'Washington DC'}
capitals_dict.keys()
dict_keys(['india', 'england', 'srilanka', 'japan', 'India', 'USA'])
dir({})
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
capitals_dict.items()
dict_items([('india', 'New Delhi'), ('england', 'london'), ('srilanka', 'colambo'), ('japan', 'tokyo'), ('India', 'Delhi'), ('USA', 'Washington DC')])
x = capitals_dict.items()
x
dict_items([('india', 'New Delhi'), ('england', 'london'), ('srilanka', 'colambo'), ('japan', 'tokyo'), ('India', 'Delhi'), ('USA', 'Washington DC')])
dir(x)
['__and__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__xor__', 'isdisjoint', 'mapping']
capitals_dict
{'india': 'New Delhi', 'england': 'london', 'srilanka': 'colambo', 'japan': 'tokyo', 'India': 'Delhi', 'USA': 'Washington DC'}
for i in capitals_dict:
    print(i)

    
india
england
srilanka
japan
India
USA
for key,values in capitals_dict.items():
    print(key,value)

    
Traceback (most recent call last):
  File "<pyshell#31>", line 2, in <module>
    print(key,value)
NameError: name 'value' is not defined. Did you mean: 'values'?
for key,value in capitals_dict.items()
SyntaxError: incomplete input
for key,value in capitals_dict.items():
    print(key,value)

    
india New Delhi
england london
srilanka colambo
japan tokyo
India Delhi
USA Washington DC
capitals_dict['Nepal']='Kathmandu'
capital_dict['Nepal']
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    capital_dict['Nepal']
NameError: name 'capital_dict' is not defined. Did you mean: 'capitals_dict'?
capitals_dict['Nepal']
'Kathmandu'
bool
<class 'bool'>
>>> 
>>> ####Nested Dictonary
>>> 
>>> states ={{'a'}:'b'}
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    states ={{'a'}:'b'}
TypeError: unhashable type: 'set'
>>> states={'Karnataka':{'capital':'Bengaluru'}}
>>> states={'Karnataka':{'capital':'Bengaluru','sweet':'MysorePak'},'Maharashtra':{'capital':'Mumbai','sweet':'Jalebi'}}
>>> states
{'Karnataka': {'capital': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}}
>>> states['Karnataka']
{'capital': 'Bengaluru', 'sweet': 'MysorePak'}
>>> states['Karnataka']['sweet']
'MysorePak'
>>> states['Maharashtra']['sweet']
'Jalebi'
>>> del states['Maharashtra']
>>> states
{'Karnataka': {'capital': 'Bengaluru', 'sweet': 'MysorePak'}}
>>> states['Maharashtra']={'capital':'Mumbai','sweet':'Jalebi'}
>>> ststes
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    ststes
NameError: name 'ststes' is not defined. Did you mean: 'states'?
>>> states
{'Karnataka': {'capital': 'Bengaluru', 'sweet': 'MysorePak'}, 'Maharashtra': {'capital': 'Mumbai', 'sweet': 'Jalebi'}}
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
