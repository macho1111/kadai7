from ownable import Ownable

class Item(Ownable):
    instances = []

    def __init__(self, name, price, owner=None):
        self.name = name
        self.price = price
        self.set_owner(owner)
        # Itemインスタンスの生成時、そのItemインスタンス(self)は、insntancesというクラス変数に格納されます。
        Item.instances.append(self)

    def label(self):
        return {"name": self.name, "price": self.price}

    @staticmethod
    def item_all():
        # instancesを返します ==> Item.item_all()でこれまでに生成されたItemインスタンスを全て返すということです。
        return Item.instances
