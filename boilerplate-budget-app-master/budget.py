class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = list()

    #Deposit method accepts amount and description (optional) then appends object to the ledger list
    def deposit(self, amount, description=""):
        
        self.ledger.append({"amount": amount, "description": description})

    #With
    def withdraw(self, amount, description=""):
        
        self.ledger.append({"amount": amount, "description": description})



def create_spend_chart(categories):
    return None