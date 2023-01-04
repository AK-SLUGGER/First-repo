'''
function use in arithmatic operators
'''

def multiply(x,y):#function signature

    product=x*y# function body

    return product #send back the value following 'return' keyword

Number_1=input('provide the first no\n')
Number_2=input('provide the second no\n')

Number_3=multiply(int(Number_1),int(Number_2))

print(f'Number_3 = {Number_3}')


      
 
