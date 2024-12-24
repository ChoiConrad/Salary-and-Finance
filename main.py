import incometax
import billsAndSubscriptions

while True:
    choice = input(
        "If you would like to calculate your Take home pay, press 1 \n"
        "If you would like to calculate your monthly bills, press 2: "
    )
    if choice == "1":
        incometax.takehomepay()
        break
    elif choice == "2":
        billsAndSubscriptions.billCalc()
        break
    else:
        print("Invalid input. Please input 1 or 2.")