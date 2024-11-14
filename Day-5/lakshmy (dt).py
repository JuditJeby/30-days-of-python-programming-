'''
  author:Lakshmy Byju
  date:14/11/2024
  python program to find current dare and time 
  
   '''

from datetime import datetime
now=datetime.now( )
print("current date and time:",now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))