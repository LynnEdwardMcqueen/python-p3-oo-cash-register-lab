#!/usr/bin/env python3
import ipdb



class PurchaseItem:
    def __init__(self, item, price, quantity):
   # def __init__(self, item, price,):
        self.set_item(item)
        self.set_price(price)
        self.set_quantity(quantity)

    def get_item(self):
        return self._item
    
    def set_item(self, item):
        self._item = item
        return

    def get_price(self):
        return self._price
    
    def set_price(self, price):
        self._price = price
        return
    
    def get_quantity(self):
       return self._quantity
    
    def set_quantity(self, quantity):
       self._quantity = quantity
       return
    item = property(get_item, set_item)
    price = property(get_price, set_price)
    quantity = property(get_quantity, set_quantity)

class CashRegister:
     
    def __init__(self, discount = 0):
        self.set_discount(discount)
        self.set_total(0)
        return

    def get_discount(self):
        return self._discount
    
    def set_discount(self, discount):
        self._discount = discount
        return

    def get_total(self):
        return self._total 
    
    def set_total(self, total):
        self._total = total
        if (total == 0):
            self.merchandise_basket = []
        return
    
    def add_item(self, item, price, quantity = 1):
        new_item = PurchaseItem(item, price, quantity)
        self.set_total(self.get_total() + quantity * price)
        self.merchandise_basket.append(new_item)
        return

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            self._total = self._total * (1 - (self.discount/100.0))
            print(f"After the discount, the total comes to $%0.f." % self._total)
        return

    def get_items(self):
       
        print("Here in get_items length = ", self.merchandise_basket)
        self.set_items( self.merchandise_basket )
        print(self._items)
        return self._items
        
    def set_items(self, foo):
        self._items = []
        
      
        for item_candidate in self.merchandise_basket:
          print("item_candidate.item = ", item_candidate.item)
          for i in range(item_candidate.quantity):
              self._items.append(item_candidate.item)
        return
 
    def reset_register_totals(self):
        self.set_total(0)
        self.merchandise_basket = []
        return
    
    def void_last_transaction(self):
        last_transaction = self.merchandise_basket[-1]
        print("Last Item = ",last_transaction.item )
        print("Last Price = ", last_transaction.price)
        print("Last Quantity = ", last_transaction.quantity)
        self.set_total(self.get_total() - last_transaction.price * last_transaction.quantity)
        # If total goes to 0, self.merchandise_basket gets set to [].  
        if (len(self.merchandise_basket) != 0):
          self.merchandise_basket.pop()
        return

        
        
    merchandise_basket = []
    discount = property(get_discount, set_discount,)
    total = property(get_total, set_total)
    items = property(get_items, set_items)
    
cash_register = CashRegister()
cash_register.add_item("eggs", 0.98)
cash_register.reset_register_totals()
cash_register.add_item("Lucky Charms", 4.5)
cash_register.reset_register_totals()


cash_register.add_item("eggs", 1.99, 3)
cash_register.void_last_transaction()
print(cash_register.total)
