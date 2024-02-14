# 
# Darbības ar masīviem - https://www.w3schools.com/python/python_arrays.asp
# 

transactions = []

while True:
    print("\nBanking Options:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. List last 10 transactions")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':

        deposit = int(input("How much u want to deposit, type amount: "))
        transactions.append(deposit)
        
        pass
    elif choice == '2':

        withdraw = int(input("How much u want to withdraw :"))
        transactions.append(withdraw * -1)

        pass
    elif choice == '3':
        g = 0
        for x in transactions:
            g = g + x 
        print("You balance ", g)
        print("Your transactions", transactions)
        pass
    elif choice == '4':
        
        print("You last 10 transactions was:", transactions[-10:])

        pass
    elif choice == '5':
        print("Exiting the banking system. Thank you!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
