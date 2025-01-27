# Classes Bank Account - Py_learn_projectn
class Bank_Account():
    def __init__(self, bankName, accountType, accountNumber, initialBalance=0):
        self.bankName = bankName
        self.accountType = accountType
        self.accountNumber = accountNumber
        self.balance= initialBalance
        self.avialableBalance = 0
        
    def deposit(self, amount):
        if amount > 0:
           self.balance += amount
           bankFee = self.balance * 0.05 ## Assume the bank charges 2% for deposits
           self.avialableBalance = self.balance - bankFee
           print(f'You have successfully deposited {amount} into your account.\nYour New balance is: {self.balance} the available balance is: {self.avialableBalance}')
        else:
            print(f'It is impossible to deposit: {amount}') 
        
        
    def withdraw(self, amount):
       if self.avialableBalance > amount and amount > 0:
           self.avialableBalance -= amount
           bankFee = amount * 0.05 ## Assume the bank charges 2% for withdrawals
           print(f'You have successfully withdrawn {amount} from your account.\nYour New balance is: {self.avialableBalance} the available balance is: {self.avialableBalance - bankFee }') 
           self.avialableBalance -= bankFee              
       else:
           print(f'Insufficient funds, your available balance is {self.avialableBalance} you can not withdraw {amount}')
           
    def check_balance(self):
        print(f'This is your current balance: {self.balance} and your available balance is {self.avialableBalance}')       
## Instantiation 
myFnb = Bank_Account('First National Bank', 'Savings', '2145 5673 9802 1242',70 ) 
myCapitec = Bank_Account('Capitec', 'Credit', '4416 3678 2884 1699')   
## Call function to deposit money into account   
myFnb.deposit(600)
myCapitec.deposit(56.90)    
myCapitec.deposit(-45)
## Call function to withdraw money from account  
myFnb.withdraw(550)
myCapitec.withdraw(100)
## Call function to view account balance 
myFnb.check_balance()
myCapitec.check_balance()