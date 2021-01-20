class bankAccount(object):
    def __init__(self, owner, age, gender, balance):
        self.owner = owner
        if age < 21:
            print("you can not open an account because of your age.")
        else:
            self.age = age
        self.gender = gender
        self.balance = balance

        if self.gender == "woman" and 21 <= age and 30 >= age:
            self.balance = self.balance + 5000    
        
    def deposit(self):
        amount = float(input("Enter amount to be deposited: ")) 
        self.balance += amount 
        print("\n Amount Deposited:", amount) 
    
    def withdraw(self): 
	    amount = float(input("Enter amount to be withdrawn: ")) 
	    if self.balance >= amount: 
		    self.balance -= amount 
		    print("\n You Withdrew:", amount) 
	    else: 
		    print("\n Insufficient balance ") 
 
    def check_balance(self):
        print(self.owner, "has" , self.balance ,"amount in the account")


bir = bankAccount("mahmut", 22, "man", 1222)
bir.deposit()
bir.check_balance()
bir.withdraw()
bir.check_balance()

iki = bankAccount("ayse", 23, "woman", 1000)
iki.deposit()
iki.check_balance()
iki.withdraw()
iki.check_balance()
