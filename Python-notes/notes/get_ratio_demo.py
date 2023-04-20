# Given 2 lists find the meaningful ratios element wise and append it to a new list
#c[i]=a[i]/b[i]


def get_ratios(vect1,vect2):
    
    '''Assumes vect1 & vect2 as Lists of equal length
       and all elements are numbers
       Returns a new list with ratios such that vect1[i]/vect2[i]
'''
    ratios=[]
    
    for i in range(len(vect1)):
        
        try:
            ratios.append(vect1[i]/vect2[i])
        except ZeroDivisionError:
                ratios.append(float('nan'))# nan =not a number
        except:
            raise ValueError('The function get_ratios is called with bad arguments')
    return ratios


                           

a=[1,2,3,4]
b=[4,3,0,1]

c =get_ratios(a,b)


        
        
