Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Concatenation ,indexing,slicing
first_name = "Abhishek" #Side note: String "Abhishek" is a literalas it \is created explicity by typing(literally)
first_name
'Abhishek'
last_name = "Khola"
full_name = first_name + last_name
full_name
'AbhishekKhola'
full_name + first_name + "" + last_name
'AbhishekKholaAbhishekKhola'
full_name = first_name + " " + last_name
full_name
'Abhishek Khola'
full_name = first_name + last_name
full_name_2 = first_name +last_name
full_name_2
'AbhishekKhola'
#Strings are immutable =>Not Editable
# Requird output: " Abhishek Khola'
#Dont use this approach first_name + " " + last_name
print("first_name" + "last_name")
first_namelast_name
print(first_name,last_name)
Abhishek Khola
f {first_name} {lastname}
SyntaxError: invalid syntax
f'{first_name} {last_name}'
'Abhishek Khola'
first_name-2 = first_name #To keep first_name undisturbed
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
first_name_2 = first_name # To keep first name undisturbed
first_name_2
'Abhishek'
first_name_2[6]
'e'
frist_name_2[6] = "T" #Expectation AbhishEk
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    frist_name_2[6] = "T" #Expectation AbhishEk
NameError: name 'frist_name_2' is not defined. Did you mean: 'first_name_2'?
len("AbhishekKhola")
13
len("first-name")
10
first_name_2[10-1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    first_name_2[10-1]
IndexError: string index out of range
first_name_2[8-1]
'k'
len(first_name)
8
first-name_2[8-1]
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    first-name_2[8-1]
NameError: name 'first' is not defined. Did you mean: 'list'?
first_name_2[8-1]
'k'
first_name_2[8] = # error immutablity and logically wrong
SyntaxError: incomplete input
first_name_2[8] ="" #error immutability and logically wrong
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    first_name_2[8] ="" #error immutability and logically wrong
TypeError: 'str' object does not support item assignment
>>> print(full_name[0:8],' ',full_name[8:13])
Abhishek   Khola
>>> Abhishek   Khola
SyntaxError: incomplete input
>>> #ADD A SPACE AFTER ABHISHEK
>>> # SPLIT 'ABHISHEKKHOLA' INTO 2 STRINGS (SUB STRINGS) AND THEN ADD A SPACE AFTER THE 1ST SUBSTRING
>>> #IMPLEMENTATION
>>> #HOW TO CREATE SUBSTRINGS? USE SLICING
>>> len(first_name)
8
>>> len(last_name)
5
>>> full_name_2
'AbhishekKhola'
>>> full_name_2[0:len(first_name)]+''+full_name_2[len(first_name):]
'AbhishekKhola'
>>> full_name_2[0:len(first_name)]+''+full_name_2[len(first_name):] #generalised version
'AbhishekKhola'
>>> full_name_2[0:len(first_name)]+' '+full_name_2[len(first_name):]
'Abhishek Khola'
>>> first_name_3="Leo"
>>> last_name_3="Messi"
>>> full_name_3=first_name_3+last_name_3
>>> full_name_3
'LeoMessi'
>>> print(full_name[0:8]+""+full_name[8:])
AbhishekKhola
>>> print (full_name_3[0:8]+" "+full_name_3[8:])
LeoMessi 
>>> full_name_3[0:len(first_name_3)]+" "+full_name_3[len(first_name_3):]#Generalised version
'Leo Messi'
>>> full_name_3[0:len(first_name)]+" "+full_name_3[len(first_name):]
'LeoMessi '
#Find location of a substring
'''for example in Health is wealth we have to find the loc of eal- sub'''
'Health is wealth'
#find location of eal
'Health is wealth'.find('eal')
>>> 'Health is wealth'.find('eal')



