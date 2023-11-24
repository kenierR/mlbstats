from Crypto.source.my_btc_bot import my_btc_bot

class Bot:
    def __init__(self):
        self.Mbb = my_btc_bot()
        # self.last_fill_order = self.Mbb.get_fills_orders()['fills'][0] #ultima orden completada
        self.buy_expected_next_price = float(self.Mbb.get_product()['price']) - 250  # valor de la proxima buy
        self.sell_expected_next_price = float(self.Mbb.get_product()['price']) + 250  # valor del proximo sell
        self.last_buy_order_id = self.Mbb.get_list_orders('BUY', 'OPEN')  # ultima orden de compra
        self.last_sell_order_id = self.Mbb.get_list_orders('SELL', 'OPEN')  # ultima orden de venta

    def update_order(self):
        try:
            self.last_buy_order_id  = self.Mbb.get_list_orders('BUY' ,'OPEN')[0]['order_id'] # id de la ultima orden de compra
            self.last_sell_order_id = self.Mbb.get_list_orders('SELL','OPEN')[0]['order_id']# id de la ultima orden de venta
        except:
            pass
        if self.last_buy_order_id ==[]: # si no hay orden de compra
            #crea una orden de compra y update last_buy_order_id
            self.buy_expected_next_price = float(self.Mbb.get_product()['price']) - 250
            self.last_buy_order_id = self.Mbb.set_order_limit('BUY',0.02735,self.buy_expected_next_price)['order_id']
            self.sell_expected_next_price = float(self.Mbb.get_product()['price']) - 250
            try:
                if (self.Mbb.get_list_orders('SELL', 'OPEN')[0]['status']) == 'OPEN':
                    self.Mbb.set_edit_limit_order(self.last_sell_order_id,self.sell_expected_next_price,0.02735)
            except:
                pass


        if self.last_sell_order_id == [] :  # si no hay orden de venta
            # crea una orden de venta y update last_sell_order_id
            self.sell_expected_next_price = float(self.Mbb.get_product()['price']) + 250
            self.last_sell_order_id = self.Mbb.set_order_limit('SELL',0.02735,self.sell_expected_next_price)['order_id']
            self.buy_expected_next_price = float(self.Mbb.get_product()['price']) + 250
            try:
                if (self.Mbb.get_list_orders('BUY','OPEN')[0]['status']) == 'OPEN':
                    self.Mbb.set_edit_limit_order(self.last_buy_order_id,self.buy_expected_next_price,0.02735)
            except:
                pass