class Account:
    def __init__(self,owner, balance = 0):
        self.owner = owner
        self.balance = balance
        
    def __str__(self):
        return f'Account owner: {self.owner} \nAccount balance: ${self.balance}'
        
    def deposit(self,  dep_amount):
        self.balance += dep_amount
        print(f'Balance + Deposit: ${self.balance}', '\nDeposit Accepted')
        
    def withdraw(self,wd_amount):
        if self.balance >= wd_amount:
            self.balance -= wd_amount
            print('Withdrawal Accepted')
        else:
            print('Account Overdrawn')

account = Account('Name', 100)
print(account)
account.owner
account.balance
account.deposit(50)
account.withdraw(120)
account.withdraw(160)


