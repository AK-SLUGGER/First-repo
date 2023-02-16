




def readInt():
    '''READS input from user
       Returns square if it is an int
  '''
    while True:
       n = input(' enter a no  \n')
       try:
           n=int(n)
           print('sq= ',n**2)
           break# Exit loop as user has given numerical i/p
       except ValueError:
          print(n,' is not an int')
