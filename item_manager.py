# このモジュールをインクルードすると、自身の所有するItemインスタンスを操れるようになります。

from item import Item
from tabulate import tabulate
from itertools import groupby

def items_list(self):   # 自身の所有する（自身がオーナーとなっている）全てのItemインスタンスを返します。
    items = [item for item in Item.item_all() if item.owner == self]
    return items

def pick_items(self, number, quantity):   # numberと対応した自身の所有するItemインスタンスを指定されたquantitiy分返します。
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]

def show_items(self):   # 自身の所有するItemインスタンスの在庫状況を、["番号", "商品名", "金額", "数量"]という列でテーブル形式にして出力します。
    table_data = []
    for stock in _stock(self):
        table_data.append([stock['number'], stock['label']['name'], stock['label']['price'], len(stock['items'])])
    print(tabulate(table_data, headers=["番号", "商品名", "金額", "数量"], tablefmt="grid"))    # tabulateモジュールを使ってテーブル形式で結果を出力

def _stock(self):   # 自身の所有するItemインスタンスの在庫状況を返します。
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(item_ls, key=lambda m: m.name):   # Item#nameで同じ値を返すItemインスタンスで分類します。
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append({"number": index, "label": {"name": item[0].name, "price": item[0].price}, "items": item})   # itemsの中には、分類されたItemインスタンスが格納されます。
    return stock
