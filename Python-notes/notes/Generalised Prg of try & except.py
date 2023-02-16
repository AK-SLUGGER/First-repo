


def readValue(requestMsg,changeType,errorMsg):
    '''Reads input from user
       Returns after changing the Type or else returns appropriate Msg
  '''
    while True:
       n = input(requestMsg)
       try:
           n=changeType(n)
           return(n)
       except ValueError:
          print(n,errorMsg)    
           
       
