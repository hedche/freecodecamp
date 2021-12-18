class Category:
    #"Food", for example, will become self.name
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    #Deposit method accepts amount and description (optional) then appends object to the ledger list
    def deposit(self, amount, description=""):
        
        self.ledger.append({"amount": amount, "description": description})

    #Withdraw method is similar to deposit, however, it will be a negative number in the ledger
    def withdraw(self, amount, description=""):
        
        #If there is still funds, append.
        if(self.check_funds(amount)):
            
            self.ledger.append({"amount": -amount, "description": description})
            return True;
        
        return False

    def get_balance(self, amount):
        
        total = sum(self.ledger)

def create_spend_chart(categories):
    return None