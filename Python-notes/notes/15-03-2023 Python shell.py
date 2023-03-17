Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# 15-03-2023

def banner():
    '''
     consumes a string as message and a another char(a str)
     as the border

     prints the message with border
     '''

    
msg ='Welcome'
border='*'

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 Banner .demo.py
banner('welcome','*')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    banner('welcome','*')
TypeError: banner() takes 0 positional arguments but 2 were given

= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 Banner .demo.py
banner('welcome','*')
*******
welcome
*******
banner('Yogita kchrii','*')
*************
Yogita kchrii
*************
banner('Yogita kchrii','@@@@@@@')
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Yogita kchrii
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 Banner .demo.py
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 Banner .demo.py", line 5, in <module>
    def banner(message,border=''*''):
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 Banner .demo.py
Traceback (most recent call last):
  File "C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 Banner .demo.py", line 5, in <module>
    def banner(message,border=''*''):
TypeError: can't multiply sequence by non-int of type 'str'
>>> 
= RESTART: C:/Users/Admin/Documents/first-dir/Python-notes/notes/15-03-2023 Banner .demo.py
>>> banner('Yogita kchrii')
*************
Yogita kchrii
*************
>>> print('hello world' , 'good', 'evening',sep='|')
hello world|good|evening
>>> print('Hello world' , 'good', 'evening',sep='++')
Hello world++good++evening
>>> print('Hello world' , 'good', 'evening')
Hello world good evening
>>> banner('welcome',border ='|')
|||||||
welcome
|||||||
>>> banner(message='hey',border="#")
###
hey
###
