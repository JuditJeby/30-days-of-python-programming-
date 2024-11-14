Write a Python program to display the current date and time.


Explanation:

The said code imports the "datetime" module, gets the current date and time, and finally prints it in a formatted string.

The first line import datetime imports the datetime module which supplies classes for manipulating dates and times.
The second line now = datetime.datetime.now() creates a datetime object for the current date and time.
The third line print ("Current date and time : ") prints the string "Current date and time : " to the console.
The fourth line print (now.strftime("%Y-%m-%d %H:%M:%S")) uses the strftime() method of the datetime object to format the date and time as a string in the format "YYYY-MM-DD HH:MM:SS" and prints it to the console.
