import time

print("Welcome to T&S Bank")


class Bank:
    #Creating Instance
    def __init__(self, name, initial_ammount=0):
        self.name = name
        self.balance = initial_ammount

    def deposite(self, deposite_ammount):
        self.balance += deposite_ammount
        return self.balance

    #Return the value of wwithdrawal charge
    def withdrawal_charge(self,withdraw_ammount):
        return (18 * withdraw_ammount) / 100

    def withdraw(self, withdraw_ammount):
        time.sleep(3)  #Puase the execution for 3 second
        charge = self.withdrawal_charge(withdraw_ammount)
        withdraw_ammount += charge
        #Checking withdrawal Conditions
        if self.balance > 100:
            if self.balance >= withdraw_ammount:
                self.balance -= withdraw_ammount
                return self.balance
            else:
                print("Your request ammount exceed yourt current balance.")
        else:
            print("For withdraw minimum limit is more than (BDT) 100")

    def __str__(self):
        return f"Hello {self.name}, Your balance : BDT {self.balance}"


name = input("Enter Your name : ")
balance = int(input("Enter initial Balance : "))
object_bank = Bank(name, balance)
print(object_bank)

deposite_ammount = 0

#Condition for deposite
while deposite_ammount < 500:
    deposite_ammount = int(input("Enter Deposite Ammount (must be >= 500) : (BDT) "))
    if deposite_ammount < 500:
        break
    print("Please Deposite at least 500. ")

object_bank.deposite(deposite_ammount)
print(object_bank)

withdraw_ammount = int(input("Enter your withdraw ammount(BDT) : "))
object_bank.withdraw(withdraw_ammount)

print(object_bank)
