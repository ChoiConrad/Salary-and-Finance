import incometax

salary=input("Welcome to Salary and Finance please enter your salary or hourly wage : ")
salary= float(salary)
if(salary<9999): 
    hours= input("How many Hours worked per week? :")
    hours= float(hours)
    print(hours)
    salary=salary*hours*52.0
    print(salary)
    takehome= incometax.calculateall(salary)
else:
    takehome = incometax.calculateall(salary)

takehome= round(takehome,2)
print(f"Your take home pay is {takehome}")

