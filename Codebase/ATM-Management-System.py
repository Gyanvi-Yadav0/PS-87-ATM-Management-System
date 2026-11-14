# ATM Management System 

FILE_NAME = "atm.txt"
DEFAULT_PIN = "1234"
DEFAULT_BALANCE = 10000

def load_data():
    try:
        with open(FILE_NAME, "r") as f:
            lines = f.read().strip().split("\n")
            pin = lines[0].strip()
            balance = int(lines[1].strip())
            transactions = lines[2:] if len(lines) > 2 else []
            return pin, balance, transactions
    except (FileNotFoundError, IndexError, ValueError):
        with open(FILE_NAME, "w") as f:
            f.write(f"{DEFAULT_PIN}\n{DEFAULT_BALANCE}\n")
        return DEFAULT_PIN, DEFAULT_BALANCE, []

def save_data(pin, balance, transactions):
    try:
        with open(FILE_NAME, "w") as f:
            f.write(f"{pin}\n{balance}\n")
            for t in transactions:
                f.write(t + "\n")
    except Exception as e:
        print(f"File error: {e}")

def check_balance(balance):
    print(f"Current Balance: {balance}")

def deposit(balance, transactions):
    try:
        amount = int(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid Amount. Please enter numbers only.")
            return balance
        balance += amount
        transactions.append(f"Deposit {amount} | Balance: {balance}")
        print(f"Deposit Successful. New Balance: {balance}")
    except ValueError:
        print("Invalid Amount. Please enter numbers only.")
    return balance

def withdraw(balance, transactions):
    try:
        amount = input("Enter amount to withdraw: ")
        amount = int(amount)
        if amount <= 0:
            print("Invalid Amount. Please enter numbers only.")
            return balance
        if amount > balance:
            print("Insufficient Balance.")
            return balance
        balance -= amount
        transactions.append(f"Withdraw {amount} | Balance: {balance}")
        print(f"Withdrawal Successful. New Balance: {balance}")
    except ValueError:
        print("Invalid amount. Please enter numbers only.")
    return balance

def mini_statement(transactions):
    if not transactions:
        print("No Transactions Yet.")
    else:
        print("--- MINI STATEMENT ---")
        for i, t in enumerate(transactions, 1):
            print(f"{i}. {t}")

def main():
    pin, balance, transactions = load_data()


    attempts = 3
    logged_in = False
    while attempts > 0:
        entered_pin = input("Enter PIN: ")
        if entered_pin == pin:
            print("Login Successful")
            logged_in = True
            break
        else:
            attempts -= 1
            if attempts == 0:
                print("Account Locked. Exiting...")
                return
            else:
                print(f"Invalid PIN. Attempts left: {attempts}")


    while True:
        print("\n--- ATM Menu ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Mini Statement")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid Amount. Please enter numbers only.")
            continue

        if choice == 1:
            check_balance(balance)
        elif choice == 2:
            balance = deposit(balance, transactions)
            save_data(pin, balance, transactions)
        elif choice == 3:
            balance = withdraw(balance, transactions)
            save_data(pin, balance, transactions)
        elif choice == 4:
            mini_statement(transactions)
        elif choice == 5:
            print("Thank You. Exiting...")
            break
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    main()
