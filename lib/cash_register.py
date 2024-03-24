class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction_amount = 0.0 

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.items.append((title, price))  
            self.total += price
            self.last_transaction_amount = price  

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")

        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_title, last_item_price = self.items.pop()
            self.total -= last_item_price
            self.last_transaction_amount = 0.0 
        else:
            print("No items to void.")