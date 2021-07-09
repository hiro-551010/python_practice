import pandas as pd
import os

class Item:
    def __init__(self, item_code, item_name, price):
        self.item_code = item_code
        self.item_name = item_name
        self.price = price
        
    
    def get_price(self):
        TAX_AMOUNT = 1.10
        return self.price * TAX_AMOUNT

class Order:
    def __init__(self, item_master):
        self.item_order_list = []
        self.item_name_list = []
        self.item_price_list = []
        self.item_master = item_master
    
    def add_item_order(self,item_code, item_name, item_price):
        self.item_order_list.append(item_code)
        self.item_name_list.append(item_name)
        self.item_price_list.append(item_price)
        
    def view_item_list(self):
        for item_order, item_name, item_price in zip(self.item_order_list, self.item_name_list, self.item_price_list):
            print("商品コード:{}".format(item_order))
            print("商品名:{}".format(item_name))
            print("価格:{}".format(item_price))

    def save_csv(self):
        path = os.path.join(os.path.dirname(__file__) + '/item.csv')

        # for item_order, item_name, item_price in zip(self.item_order_list, self.item_name_list, self.item_price_list):
        #     df = pd.DataFrame([[item_order, item_name, item_price]])
        #     csv = pd.read_csv(path)
        #     if self.item_order_list in csv:
        #         print('その商品コードはすでに使われています')
        #     else:
        #         if '商品コード' in csv:
        #             df.columns = ['商品コード', '商品名', '価格']
        #             df.to_csv(path, mode='a', index=False, encoding='utf-8')
        #         else:
        #             df.to_csv(path, mode='a', index=False, encoding='utf-8')


        # df = pd.DataFrame({
        #     '商品コード': self.item_order_list,
        #     '商品名': self.item_name_list,
        #     '価格': self.item_price_list,
        # }

        df = pd.DataFrame([[self.item_order_list, self.item_name_list, self.item_price_list]])
        csv = pd.read_csv(path)

    
        
    
### メイン処理
def main():
    # マスタ登録
    item_master = []
    # item_master.append(Item("001","りんご",100))
    # item_master.append(Item("002","なし",120))
    # item_master.append(Item("003","みかん",150))
    # 確認
    # print(item_master[0].item_code)
    

    #コンソールで商品登録
    itemcode = input('任意の商品コードを入力してください: ')
    itemname = input('商品名を入力してください: ')
    itemprice = input('価格を入力してください: ')
    item_master.append(Item(itemcode, itemname, itemprice))


    # オーダー登録
    order=Order(item_master)
    # order.add_item_order("001", "りんご", 100)
    # order.add_item_order("002", "なし", 120)
    # order.add_item_order("003", "みかん", 150)
    order.add_item_order(itemcode, itemname, itemprice)
    
    # オーダー表示
    order.view_item_list()

    order.save_csv()
    



if __name__ == "__main__":
    main()

