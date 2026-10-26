# priogram to find ATM Transaction Simulation

balance = float(input("Enter starting balance: "))
number_of_transactions = int(input("How many transactions? "))

for i in range(number_of_transactions):
    transaction = input("Enter deposit or withdraw: ")
    amount = float(input("Enter amount: "))

    if transaction == "deposit":
        balance = balance + amount
        print("Money deposited")
    elif transaction == "withdraw":
        if amount <= balance:
            balance = balance - amount
            print("Money withdrawn")
        else:
            print("Not enough money")
    else:
        print("Invalid transaction")

print("Final balance:", balance)