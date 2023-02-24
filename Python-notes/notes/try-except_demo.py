


divisor =12

n=16
try:
    print(n/divisor)
    
except ZeroDivisionError:
        print('block2')
else:
    print('Block3')
    print('divisor is not zero')
finally:
    print('block4')
    
print('EOF')
