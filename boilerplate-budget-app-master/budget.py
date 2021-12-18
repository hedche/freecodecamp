class Category:
    #"Food", for example, will become self.name
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    def __str__(self) -> str:
        title_length = 30
        

    #Deposit method accepts amount and description (optional) then appends object to the ledger list
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    #Withdraw method is similar to deposit, however, it will be a negative number in the ledger
    def withdraw(self, amount, description=""):
        
        #If there is still funds, append and return True, if not return False
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -amount, "description": description})
            return True;
        return False

    #This will add all the appended amounts of the ledger list
    def get_balance(self):
        total = 0
        for item in self.ledger:
            total += item["amount"]
        return total
        
    #Transfer method which will transfer amounts using deposit and withdraw methods  
    def transfer(self, amount, category):
        
        #If there is still funds, append.
        if(self.check_funds(amount)):
            category.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount,"Transfer to " + category.name)
            return True
        
        return False

    def check_funds(self, amount):
        if(self.get_balance() >= amount):
            return True
        return False

def create_spend_chart(categories):
    astrk = "*"
    
    return None