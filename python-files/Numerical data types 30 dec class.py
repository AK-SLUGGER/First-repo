Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
 help(bin)
 
SyntaxError: unexpected indent
help(bin)
Help on built-in function bin in module builtins:

bin(number, /)
    Return the binary representation of an integer.
    
    >>> bin(2796202)
    '0b1010101010101010101010'

bin(5)#101 <->0b101
'0b101'
type(bin(5))
<class 'str'>
int('0b101')
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int('0b101')
ValueError: invalid literal for int() with base 10: '0b101'
int('0b101',2)#2 is base
5
int('0b101',base=2)
5
0o2375
1277
#0o2375 into decimal
#0o represents octal number
int('0o2375',base=8)
1277
# octal converted to decimal
help(oct)
Help on built-in function oct in module builtins:

oct(number, /)
    Return the octal representation of an integer.
    
    >>> oct(342391)
    '0o1234567'

help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.
    
    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.

round(2.33)
2
round(2.33,1)
2.3
round(2.38,1)
2.4
round(2.38)
2
round(4.49)
4
round(4.51)
5
round(3123213.49999)
3123213
round(312332123.5011)
312332124
round(9.5)
10
round(2.5)
2
round(3.5)
4
round(232323.5)
232324
round(232326.5)
232326
>>> #it takes nearest even digit (concept)
>>> abs(-2)==2
True
>>> abs92)==2
SyntaxError: unmatched ')'
>>> #|x| mode of x
>>> pow(2,3)#power function
8
>>> pow(4,9)
262144
>>> pow(4,0.5)
2.0
>>> help(pow)
Help on built-in function pow in module builtins:

pow(base, exp, mod=None)
    Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments
    
    Some types, such as ints, are able to use a more efficient algorithm when
    invoked using the three argument form.

>>> pow(2,3,2)
0
>>> pow92,3)%2
SyntaxError: unmatched ')'
>>> pow(2,3)%2
0
>>> #pow(2,3)%2<==>pow(2,3,2)
>>> pow(2,3,4)#(2 to the power 3)%4???
0
>>> pow(2,3,3)#(2 to the power 3)%3
2
>>> 8%2
0
>>> 8%3
2
>>> # base ** exponent function
>>> 2.5**3.243
19.521781524958914
