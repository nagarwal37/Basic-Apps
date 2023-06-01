import datetime

overall=[]

#procedure to add a goal
def addgoal():
    goal=str(input("What is your goal?\n"))
    deadline=str(input("What is your deadline? In format DD.MM.YYYY\n"))
    to_append=[goal, deadline]
    overall.append(to_append)

#function to convert the inputted string data type to a date data type
def convdate(n):
    thisdeadline=overall[n][1]
    print(datetime.datetime.strptime(thisdeadline, "%d.%m.%Y"))

#function to calculate time left to meet the goal
def calctime(n):
    new_deadline_date=datetime.datetime.strptime(overall[n][1], "%d.%m.%Y")
    current=datetime.datetime.today()
    time_till=new_deadline_date-current
    print(f"The time left to meet goal:{overall[n][0]} is {time_till.days} days")

#function to print the goal list
def print():
    for i in range(len(overall)):
        print(overall[i])
