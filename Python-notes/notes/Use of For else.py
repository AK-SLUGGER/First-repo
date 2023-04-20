### Use of for else

###Warn after 3 unsuccessful attempts

password='Abcd@1234'
for i in range(3):
    pw = input('Enter Password')
    if pw == password:
        print('Login successful')
        break
    print(f'Enter password again,Attempted {i+1} times {2-i} attempts left')

else:
    print('Suspicious')


    
