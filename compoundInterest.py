def collect_user_input():
    # User input
    principal = float(input("Principle (amount): "))
    time =      float(input("Time:               "))
    rate =      float(input("Rate:               "))

    return principal, time, rate

def calculate_and_print_compound_interest(principal, time, rate):
# Formula for amount
    amount = principal * ( 1 + rate / 100) ** time

    # Formula for compound interest
    compound_interest = round(amount - principal, 2) # round to nearest hundredth

    # Print result
    print(f"Compound Interest: {compound_interest}")

def calculateCompoundInterest():
    number_of_clients = 3 # Declares number of clients for how many times the loop will ask

    # Will loop through below depending on how many clients there are
    for i in range(number_of_clients):
        # Prints divider
        if i != 0:
            print("---")

        # User input
        principal, time, rate = collect_user_input()
        
        # Calculate and print Compound Interest
        calculate_and_print_compound_interest(principal, time, rate)
        
    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
