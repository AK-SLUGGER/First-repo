Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Numerical data types
#Numbers
#int
#float
#float  is used for Decimal (Measurement)
#Integer - int
int('2')
2
2=2
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
2+2
4
#int div
#quotient is returned in it

9//3
3
9//2
4
#// also returns integer
9/2
4.5
/ gives actual value
SyntaxError: invalid syntax
9/3
3.0
#Addition,Multiplication,subtraction   depends on operands if any one of the operand is a float it will gives a float
2.0*4
8.0
2
2
*
2*4
8
# return values data type is float if one of the operand is float
#- operator can be used for two purposes
2-3
-1
3-2
1
-2
-2
x=8
-x
-8
2=8
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
# without using the + operator add 2 numbers
2 - -8
10
2 + 8
10
2 ** 3
8
6 ** 2
36
pow(2,6)
64

# Also use pow function
4%3
1
5%3
2
# % gives the remainder
6 %3
0
pow(2,3,2)
0
(2 **3)%
SyntaxError: incomplete input
(2**3)%2
0
pow(6,3,4)
0
6**3
216
216 %4
0
()
()
(6**3) %4
0
1_000_000_000 ===1000000000
SyntaxError: invalid syntax
1_000_000 == 1000000
True
1_000_000
1000000
x = 100
x = 100 #integer literal
y = int("7")# its not literal
y
7
#Floats
34.89
34.89
100_00.22_33
10000.2233
100_00.22_33#cant use the_ after .
10000.2233
100_00._22>33
SyntaxError: invalid decimal literal
100.0.is integer()
SyntaxError: invalid syntax

100.0.is_integer()
True
100.88.is_integer()
False
# e notation floating point number
18e3
18000.0
18*1000
18000
1.8765e2
187.65
12e900#their is a limit for e notations
inf
-12e900
-inf
12e10
120000000000.0
-12e10
-120000000000.0
float
<class 'float'>
float('12.6')
12.6
int(12.6)
12
int(12.999)
12
int("12.6")
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    int("12.6")
ValueError: invalid literal for int() with base 10: '12.6'
#"12.6" to an int
int(float('12.6'))
12
#Absolute functions
abs(-12)
12
abs(12.88)
12.88
round(1.99)
2
round(1.99334,4)#defined with decimal accuracy 4
1.9933
round(1.9933,3)
1.993
round(1.9933,1)
2.0
round(1.9936,3)
1.994
round(1.46,1)
1.5
round(1.44,1)
1.4
0.1
0.1
x = 0.1
x + x + x
0.30000000000000004
>>> #Upper there is an error in output bec evrey dec no cangt be representated  in binary
>>> round(1.5)
2
>>> round(2.5)
2
>>> #when the dec digit is 5 it should return the nearest evn no
>>> round(3.5)
4
>>> round(576.5)
576
>>> round(6.5)
6
>>> #f strings
>>> n=123.45
>>> f"{n}"
'123.45'
>>> f"{n:.1f}"#.1f represents want only 1 floating point precision
'123.5'
>>> r=1234.56789
>>> f"{r:.3f}"
'1234.568'
>>> q=12345678
>>> f"{q:,}"
'12,345,678'
>>> #f'{var name:.<precision>f}'
>>> #f'{var name:,}'
>>> q=12345667.1234566
>>> f"{q:,.3f}"
'12,345,667.123'
>>> #f'{var name:,.<precision>f}'
>>> pow(9,0.5)#Square root of 9 ,,,Math notation 9^0.5
3.0
>>> #x ^ 0.5 is a square root
>>> int(pow(9,0.5))
3
>>> sqrt_number=pow(9,0.5)
>>> sqrt_number
3.0
>>> int(sqrt_number)
3
int(8.6)
8
round(8.6)
9
round(8.51)
9
round(8.5)
8
