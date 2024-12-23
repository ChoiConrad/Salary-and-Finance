def federaltax(salary):
    if salary < 0:
        print("Your salary came in as negative. Please recheck what you input.")
        return None  
    elif 0 <= salary <= 11000:  # Includes salary = 0
        return salary - salary * 0.1
    elif 11001 < salary <= 44725:
        return salary -  salary * 0.12
    elif 44726 < salary <= 95375:
        return salary -  salary * 0.22
    elif 95376 < salary <= 182100:
        return salary -  salary * 0.24
    elif 182101 < salary <= 231250:
        return salary -  salary * 0.32
    elif 231251 < salary <= 578125:
        return salary -  salary * 0.35
    else:
        return salary -  salary * 0.37
    
def ficatax(federal):
    return federal - federal*0.0765
    

def stateincometax(salary):
    if salary < 0:
        print("Your salary came in as negative. Please recheck what you input.")
        return None 
    elif 0 <= salary <= 10756:  # Includes salary = 0
        return salary -  salary * 0.01
    elif 10756 < salary <= 25499:
        return salary -  salary * 0.02
    elif 25499 < salary <= 40245:
        return salary -  salary * 0.04
    elif 40245 < salary <= 55866:
        return salary -  salary * 0.06
    elif 55866 < salary <= 70606:
        return salary -  salary * 0.08
    elif 70606 < salary <= 360659:
        return salary -  salary * 0.093
    elif 360659 < salary <= 432787:
        return salary -  salary * 0.103
    elif 432787 < salary <= 721314:
        return salary -  salary * 0.113
    else:  # Captures all cases above 721314
        return salary -  salary * 0.123
    
def calculateall(salary):
    return stateincometax(ficatax(federaltax(salary)))
    
