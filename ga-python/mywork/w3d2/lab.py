class Customer():

    def __init__(self):
        self.balance = 0.0
        self.allow_overdrafts = False
        self.transaction_history = []

    def deposit(self, money):
        self.balance += money
        self.transaction_history.append(tuple(("Deposit", money)))

    def withdraw(self, money):
        self.balance -= money
        self.transaction_history.append(tuple(("Withdrawl", money)))
        if self.balance < 0:
            if self.allow_overdrafts == False:
                self.balance += money
                print("Insuficient funds. The account balance is", self.balance)
                self.transaction_history.pop()
            elif self.allow_overdrafts == True:
                self.balance -= 35
                self.transaction_history.append(tuple(("Overdraft", 35)))
                print("Wow they are allowing overdrafts, thats something I woudln't do! Their balance is", self.balance)

    def current_balance(self):
        print('Your current balance is', self.balance)

    def Change_Allow_Overdraft_False(self):
        self.allow_overdrafts = False

    def Change_Allow_Overdraft_True(self):
        self.allow_overdrafts = True

    def Show_Transaction_history(self):
        for each in self.transaction_history:
            print(each)


Jimmy_Franco = Customer()
Jimmy_Franco.current_balance()
Jimmy_Franco.deposit(11.11)
Jimmy_Franco.withdraw(.11)
Jimmy_Franco.withdraw(11.12)
Jimmy_Franco.Change_Allow_Overdraft_True()
Jimmy_Franco.withdraw(11.11)
Jimmy_Franco.Show_Transaction_history()

