print("===== BANK ACCOUNT SYSTEM =====")
class BankAccount:
    def __init__(self,account_number,name,balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

b1 = BankAccount(256,"vaishnavi",1000000)

class Methods:
    def __init__(self):
        self.BankAccount()

amount = 2000
balance = 2000
n = int(input("enter amount to deposit:"))
print("deposited successfully!")
balance = balance+amount
print("currentbalance=",balance)

withdrawal_amount = int(input("enter amount to withdraw:"))
print("withdrawn successfully!")
balance = balance-amount
print("currentbalance=",balance)

if withdrawal_amount<=balance:
    print("insufficient balance!")

else:
    print("sufficient balance!")

print("currentbalance=",balance)

print(b1)




        
        
