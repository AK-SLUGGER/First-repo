'''
while loop
To print a no 10 times
'''

t=0
while(t<10):
    print(t)
    t=t+1
    

'''
want 10 also
'''
t=0
while(t<=10):
    print(t)
    t=t+1
    

'''
if wannt 11
'''

t=0
while(t<=11):
    print(t)
    t=t+1

'''
infinite loop
'''
#t=1
#while(t>0):
 #   print(t)
  #  t=t+1
    
'''
Application of Infinite loop
example!!!

'''
x=float(input("Enter a Positive num\n"))
while (x<=0):
    x=float(input("Enter a Positive num\n"))

print(f"the positive no u have entered is {x}")



# in :- memebership operator

#how to check
'p' in 'python'
#Gives True

'p' in 'Python'
#Gives false

# also used to find substring in a string

'heal' in 'health'
#True
'hal' in 'health'
#False

#for- LOOP use
for i in "pyhton":
    print (i)


type(range)
# class type

for i in range(10):
    print(i)


for i in range(1,10):#from 1 to 9 print
     print(i)
     
for i in range(1,10,2):# last 2 jumps 2 value then print till 10
     print(i)
    
for i in "python"[:1]:#For print of only p,,,wrong practise
    print(i)


    
# use of while loop like for loop 
index=0

t="Python"
#t[index] # find index

while(index<len(t)):
    print(t[index])
    index=index+1
    
    
    







            
