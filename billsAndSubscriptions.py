def billCalc():
    bills = []
    while True:
        try:
            x = input("Please input your bill or input -1 to exit: ")
            x = float(x)  # Convert input to a number
            if x == -1:   # Check for the exit condition
                break
            bills.append(x)
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"Your monthly bill is: {sum(bills):.2f} \nYour yearly bill is: {12*sum(bills):.2f}")
