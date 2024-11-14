'''Python program to find current date and time
Author:Kenaz mathukutty
Created:14/11/2024'''
from datetime import datetime
now=datetime.now( )
print("current date and time:",now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))