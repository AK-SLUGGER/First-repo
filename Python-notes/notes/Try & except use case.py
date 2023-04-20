   # Try &  Except use case


try:
   print(x)
except:
    print('Please declare  a variable before use')


print('2nd line')



####

n1=input('input Num1')
n2=input('Input Num2')

try:
    print(n1/n2)
except:
    print('Enter valid nums')


#####

n1=input('input Num1 \n')
n2=input('Input Num2 \n')

try:
    print(n1/n2)
except (ZeroDivisionError,TypeError):
    print('Make sure n2 is non zero')    
#except TypeError:
    #print(int(n1)/int(n2))

####    
n1=input('input Num1 \n')
n2=input('Input Num2 \n')

try:
    print(n1/n2)
##except (ZeroDivisionError,TypeError):
    ##print('Make sure n2 is non zero')
except :
    print('Error .Please Rectify')
    
    
    
