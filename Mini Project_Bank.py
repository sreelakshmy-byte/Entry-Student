class BankAccount:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.amount = 0
        self.logged_in = False
    def login(self):
        correct_pin = "1775"
        attempts = 3
        while attempts > 0:
            pin = input("Enter your four-digit PIN to login: ")
            if pin == correct_pin:
                print("Login successful.")
                self.logged_in = True
                return True
            else:
                attempts -= 1
                print(f"\nInvalid pin. {attempts} attempts remaining.")
        print("Too many incorrect attempts. Exiting")
        return False

    def show_details(self):
        if self.logged_in:
            print("Personal details:")
            print("Name:", self.name)
            print("Age:", self.age)
        else:
            print("Please login to see details.")

    def deposit(self, amount):
        if self.logged_in:
            self.amount += amount
            print("Amount successfully added.")
        else:
            print("Please login to deposit money.")

    def withdraw(self, amount):
        if self.logged_in:
            if self.amount - amount >= 500:
                self.amount -= amount
                print("Amount successfully withdrawn.")
            else:
                print("Insufficient balance. Minimum balance of 500 must be maintained.")
        else:
            print("Please login to withdraw money.")

    def account_bal(self):
        if self.logged_in:
            print("Your bank balance is:", self.amount)
        else:
            print("Please login to check balance.")sree
name = input("Enter your name: ")
age = int(input("Enter your age: "))
a = BankAccount(name, age)
if a.login():
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Show Details\n5. Quit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            amount = float(input("Enter amount to be deposited: "))
            a.deposit(amount)
        elif choice == 2:
            amount = float(input("Enter amount to be withdrawn: "))
            a.withdraw(amount)
        elif choice == 3:
            a.account_bal()
        elif choice == 4:
            a.show_details()
        elif choice == 5:
            print("Exiting the program.")
            break
        else:
            print("You have entered a wrong value. Please enter a number between 1 and 5.")
else:
    print("Login Failed. Exiting the program.")