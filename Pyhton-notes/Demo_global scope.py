

def func(y):
    y='Hello'
    print(f'Inside{y}')
    return y+y
    
#global y
    
y=10
x=func(y)#value return by func y+y (inside func)
print(f'Outside{y}')
print(f'x={x}')


#By using global

def func():
    global z
    z='Hello'
    print(f'Inside{z}')
    return z+z
    
global z
    
z=10
x=func()#value return by
print(f'Outside{z}')
print(f'x={x}')
