"""Author:Liya binu
date:14-11-2024
program to display current date and time"""
from datetime import datetime
now=datetime.now()
print("current date and time:",now)
print(now.strftime("%Y-%m-%d %H:%M:%S"))