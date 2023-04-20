

# Break & continue & for else

for i in range(1,10):
    if (i%3==0):
        break
    print(i)

else:
    print('inside else')
    
print('Outside everything')





######Using 11 in place of 3 for check what it gives

for i in range(1,10):
    if (i%11==0):
        break
    print(i)

else:
    print('inside else')
    
print('Outside everything')



####Using 6 in place of 3 for check what it gives
for i in range(1,10):
    if (i%6==0):
        break
    print(i)

else:
    print('inside else')
    
####print('Outside everything')



### using 100

for i in range(1,10):
    if (i%100==0):
        print(f'i={i}inside if')
        break
    print(i)

else:
    print('inside else')
    
print('Outside everything')
    
####Using 2
for i in range(1,10):
    if (i%2==0):
        print(f'i={i}inside if')
        break
    print(i)

else:
    print('inside else')
    
print('Outside everything')
