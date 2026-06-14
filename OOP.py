#Import time library to use sleep()
import time

print("Welcome to T&S Bank")

# ==========================================
# 1. ENCAPSULATION & 2. ABSTRACTION
# ==========================================
# ENCAPSULATION: The Bank class bundles data (name, balance) and methods 
# (deposit, withdraw) into a single unit. 
class Bank:
    def __init__(self, name, initial_amount=0):
        self.name = name
        
        # STRICT ENCAPSULATION: Using a double underscore '__' makes this 
        # attribute private. It cannot be accessed directly from outside the class.
        self.__balance = initial_amount

    # Getter method to safely access the private balance
    def get_balance(self):
        return self.__balance

    # Setter method to safely modify the private balance
    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
        return self.__balance

    # Internal helper method
    def withdrawal_charge(self, withdraw_amount):
        return (18 * withdraw_amount) / 100

    # ABSTRACTION: The user calls withdraw(), completely unaware of the internal 
    # sleep timer, charge calculations, and condition checks happening behind the scenes.
    def withdraw(self, withdraw_amount):
        time.sleep(3)  # Pause the execution for 3 seconds
        charge = self.withdrawal_charge(withdraw_amount)
        total_deduction = withdraw_amount + charge
        
        # Checking withdrawal Conditions
        if self.__balance > 100:
            if self.__balance >= total_deduction:
                self.__balance -= total_deduction
                return self.__balance
            else:
                print("Your requested amount plus charges exceeds your current balance.")
        else:
            print("For withdrawal, the minimum limit is more than (BDT) 100.")

    # ==========================================
    # 3. POLYMORPHISM
    # ==========================================
    # METHOD OVERRIDING: We are redefining Python's built-in __str__ method 
    # to change how the object behaves when printed.
    def __str__(self):
        return f"Hello {self.name}, Your balance : BDT {self.__balance}"


# ==========================================
# 4. INHERITANCE
# ==========================================
# INHERITANCE: SavingsAccount is a "child" class that inherits all attributes 
# and methods from the "parent" Bank class.
class SavingsAccount(Bank):
    def __init__(self, name, initial_amount=0, interest_rate=0.05):
        # super() calls the parent class's __init__ method to set up name and balance
        super().__init__(name, initial_amount)
        self.interest_rate = interest_rate

    def apply_interest(self):
        # Using the getter and setter methods to interact with the private __balance
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest applied: BDT {interest}")

    # MORE POLYMORPHISM: Overriding the parent's withdrawal_charge method.
    # Savings accounts now get a lower withdrawal charge (5% instead of 18%).
    def withdrawal_charge(self, withdraw_amount):
        return (5 * withdraw_amount) / 100


# --- Main Program Execution ---

name = input("Enter Your name : ")
balance = int(input("Enter initial Balance : "))

# We now create an instance of SavingsAccount to utilize Inheritance
object_bank = SavingsAccount(name, balance)
print(object_bank)

deposit_amount = 0

# Condition for deposit
while deposit_amount < 500:
    deposit_amount = int(input("Enter Deposit Amount (must be >= 500) : (BDT) "))
    if deposit_amount >= 500:
        break
    print("Please Deposit at least 500. ")

object_bank.deposit(deposit_amount)
print(object_bank)

# Demonstrating the new method from the inherited class
object_bank.apply_interest()
print(object_bank)

withdraw_amount = int(input("Enter your withdraw amount (BDT) : "))
object_bank.withdraw(withdraw_amount)

print(object_bank)
