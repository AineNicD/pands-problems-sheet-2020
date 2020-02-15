# Weekly task 5

#Write a program that outputs whether or not today is a weekday. 
# An example of running this program on a Thursday is given below.
#$ python weekday.py
#Yes, unfortunately today is a weekday.
#An example of running it on a Saturday is as follows.
#$ python weekday.py
#It is the weekend, yay!

#In the python calender the days of week are 0-6, Monday is number 0.
import calendar
import datetime 


weekDay = datetime.datetime.today().weekday()

if weekDay<5:
    print ("Yes, unfortunately today is a weekday.")
else:
    print ("It is the weekend, yay!")




#references;
#https://docs.python.org/3.4/library/calendar.html
#https://stackoverflow.com/questions/45870820/how-to-check-if-today-is-monday-in-python
#https://docs.python.org/3/library/datetime.html#datetime.date.weekday
#https://pythontic.com/datetime/date/weekday
#https://stackoverflow.com/questions/9847213/how-do-i-get-the-day-of-week-given-a-date
#https://www.guru99.com/calendar-in-python.html







