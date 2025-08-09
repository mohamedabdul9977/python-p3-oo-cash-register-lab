#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discount = discount 
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        cost = price * quantity
        self.total += cost
        self.last_transaction = cost
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0.0
        if self.items:
           self.items.pop()