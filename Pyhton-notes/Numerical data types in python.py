#Numerical Data Types in Python

#int
#float
#complex(we dont use much in this course)

#int  -counting
#float -measuring ->>ArithmeticError decimal value

a=1
b=2
type(a)
#<class "int">
type (b)
#<class "int">
c=1.0
d=2.5
type (c)
#<class "float">
#Operators
#Addition +
"q"+"w"
#"qw"
a+b
#3
type(a+b)
#<class 'int'>
sum_a_b=a+b
type(sum_a_b)
#<class "int">
sum_c_d=c+d
sum_c_d
#3.5
type (sum_c_d)
# <class 'float'>
#[for numbers]When both the operands of '+'operator are of same 'type'\n the resulting sum is of same type
 
sum_a_c=a+c
sum_a_c
#2.0
type(sum_a_c)
#<class 'float'>
sum_c_a=c+a
sum_c_a
#2.0

type(sum_c_a)
#<class 'float'>
sum_c_a==sum_a_c
#True
1==1.0
#True
type(1)
#<class 'int'>
type(1.0)
#<class 'float'>
123456789==123456789.0
#False
#When you want to check the type the equality of 2variables pleadse use 'type' function not'=='
type(True)
#<class 'bool'>
#str -->text
#int --> integers
#float-->decimal numbers
#bool-->Truth or False
a+c
#2.0
c+a
#2.0
"t"+"r"
#'tr'
"r"+"t"
#"rt"
name= "Virat"
number=18#int literal
dist_sun_earth=147000000000
dist_sun_earth_un=147_000_000_000
#both gives the same no but its too easy to count and read
#type of both are also integers
#_ underscore character can be used to group numbers in an int literal to improve readability
#Do not use _ immediately after the decimal dot
#Never start an ordinary varible name with _ Syntatically valid
_12 =12
#12
#used for special purpose
#_ underscore also used to give us the previous inspected value
#addition
#if you want to add 10 number
1+2+3+4+5
#15
sum([1,2,3,4,5,])
#15 is the output same as one by one addition
# +&* are both commutative operators
#- operand is non commutative
#New operator '!=' is used for value inequality
a==1
#'True"
a!=1
#'False'
5!=3
#True
#Comparing values : '==' and '!='






