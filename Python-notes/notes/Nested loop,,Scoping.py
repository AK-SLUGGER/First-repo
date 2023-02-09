

#Iteration

#for repetation of 2,3,4 five times


for i in range(2,5):
    print(i)

for j in range(3):
    for i in range(2,5):
        print(i)

 #above code will repeat the 2,3,4 three times!!!!
for j in range(3):
    print(f'Outside inner for loop j={j}')
      
    for i in range(2,5):
         print(f'Inside the inner for loop i={i}')


#  Above both are examples of Nested loop :-loop in a loop is called nested loop

# CONCEPT OF SCOPING

x=10

print(f'before func() definition x={x}')

def func():#Here func(_) _ place is called Parameter
    x="Hey!"
    print(x)

func() #Here func(_)_ place value is called argument
print(x)

#In above we can observe that it will print
#1:-print(f statement)
# 2:- func() call=Hey!
#3 :- print(x)=10

#Another example of scoping

x=10

print(f'before func() definition x={x}')

def func():
    x="Hey!"
    print(x)

def foo(x):
    print(x,"inside foo")

foo('where am i')    
func()
print(x)

##In above we can observe that it will print
#1:-print(f statement)
#2:-Where am i inside foo
# 3:- func() call=Hey!
#4 :- print(x)=10 

#FUNCTION IS DEFINED INSIDE A FUNCTION (SCOPING)

x=10 #Global scope
def foo():# fuction def -- outer

        y=5#Enclosing scope(local scope)
        x=4

        def add():#function def--inner
            #Actual local scope
            y=15
            x=14

            print(f'the value of x={x},y={y},sum={x+y}')
            
            add()
 
foo()
##above scoping it will take y=15 x=14 and sum is 29 executes the inner local first




x=10 #Global scope
def foo():# fuction def -- outer

        y=5#Enclosing scope(local scope)
        x=4

        def add():#function def--inner
            #Actual local scope
            y=15
            #x=14

            print(f'the value of x={x},y={y},sum={x+y}')
            
            add()
 
foo()

#if we comment out x=14 in add() func the it will take above x value
##here x=4 and y=15 and sum is 19





