

#To generalize this scoping there is an echo name

#called  Scope LEGB

# L- Local
# E - Enclosing
# G - Global
# B - Builtin


#Function is dedicated to do specific task

def emp_id_generator():
    pass   #pass is a pasing sentence 


## name, emp_id,department,dob,gender,designation,place of residence

name=input("name")
emp_is=''#int
department =input('dep') #str
gender = input ('gender')#M or F ---bool,str
dob =input("dob")#Str
designation = input('desgn')#str
place_of_residence=input('res')#str


'''
name_2=input("name")
emp_is_2=''#int
department_2 =input('dep') #str
gender_2 = input ('gender')#M or F ---bool,str
dob_2 =input("dob")#Str
designation_2 = input('desgn')#str
place_of_residence_2=input('res')#str
'''
#FOR capturing the data of employes we have to re enter again and again like
#above but to ease this we can do this by looping


# Above process by Looping (But for the storing it we use...
#List :-data type


for i in range(5):
  name=input("name")
  emp_id=''#int
  department =input('dep') #str
  gender = input ('gender')#M or F ---bool,str
  dob =input("dob")#Str
  designation = input('desgn')#str
  place_of_residence=input('res')#str

#List data type is a muttable func
  
  #defined by[]
  
  type[]
  #shows list

 # If you want a letter to the list u can use append

 #EX:- Z[1,W,TRUE,FALSE]
 #YOU CAN ADD ITEMS IN LIST-> Z.append('23')
 #Now the list is Z [1,W,TRUE,FALSE,23]

 #List supports slicing as well

 
#By use of List data type
name_list = [] #list contaning name of all employes
dob_list = [] #list contaning dob
emp_id_list = [] # list with all emp id
designation_list = [] #list of all designation
#emp_count--int



for i in range(5):
  name=input("name")
  name_list.append(name)
  emp_id=''#int
  #department =input('dep') #str
  #gender = input ('gender')#M or F ---bool,str
  dob =input("dob")#Str
  dob_list.append(dob)
  designation = input('desgn')#str
  designation_list.append(designation)
  place_of_residence=input('res')#str
 
   
