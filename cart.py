from ownable import Ownable
from item_manager import show_items

class Cart(Ownable):
    set_owner = Ownable.set_owner
    show_items = show_items
    
    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("💸 購入できる残高がありません。")
        else:
            print("💸 購入が確定しました！")
            self.owner.wallet.withdraw(self.total_amount())
            for item in self.items:
                item.set_owner(self.owner)
            self.items = []