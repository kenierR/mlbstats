import datetime
import time
import hmac
import hashlib
import http.client
import os,json
import uuid

class my_btc_bot():
    def __init__(self):
      self._updated = False
      self.conn = http.client.HTTPSConnection("api.coinbase.com")
      self.api_key = os.environ.get('coinbase_API_key')
      self.secret_key = os.environ.get('coinbase_API_secret')
      self.timestamp = str(int(time.time()))
      self.method = ''
      self.request_path = ''
      self.payload = ''
      self.signature = ''
      self.conn = ''
      self.headers = ''


    def Update(self,method,request_path,payload):
        self.timestamp = str(int(time.time()))
        self.payload = payload
        self.request_path = request_path
        self.method = method
        message = str(self.timestamp) + self.method + self.request_path + self.payload
        self.signature = hmac.new(self.secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
        self.headers = {
            'accept': 'application/json',
            'CB-ACCESS-KEY': self.api_key,
            'CB-ACCESS-TIMESTAMP': self.timestamp,
            'CB-ACCESS-SIGN': self.signature
        }
        self.conn = http.client.HTTPSConnection("api.coinbase.com")
        self._updated = True
    def set_order_limit(self,side,base_size,limit_price):
        payload = json.dumps({
            "client_order_id": str(uuid.uuid4()),
            "product_id": "BTC-USD",
            "side": str(side),
            "order_configuration": {
                "limit_limit_gtc": {
                    "base_size": str(base_size),
                    "limit_price": str(limit_price)
                }
            }
        })

        self.Update(method='POST',request_path = "/api/v3/brokerage/orders",payload=payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        self._updated = False
        return json.loads(data.decode("utf-8"))

    def get_order(self,id):
        request_path = '/api/v3/brokerage/orders/historical/{order_id}'.format(order_id = id)
        payload = ''
        self.Update('GET', request_path, payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        return json.loads(data.decode("utf-8"))

    def get_fills_orders(self):
        request_path = '/api/v3/brokerage/orders/historical/fills'
        payload = ''
        self.Update('GET',request_path,payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        return json.loads(data.decode("utf-8"))

    def get_list_all_order(self):
        request_path = '/api/v3/brokerage/orders/historical/batch'
        payload = ''
        self.Update('GET', request_path, payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        return json.loads(data.decode("utf-8"))

    def get_list_orders(self,side,status):
        list_orders = []
        orders = self.get_list_all_order()['orders']
        for order in orders:
            if order['side'] == side and order['status'] == status:
                list_orders.append(order)

        return list_orders
    def set_cancel_order(self,id):
        request_path = '/api/v3/brokerage/orders/batch_cancel'
        payload = json.dumps({
            "order_ids": [
                str(id)
            ]
        })
        self.Update('POST', request_path, payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        return json.loads(data.decode("utf-8"))
    def cancel_all_orders(self):
        list_orders_buy = self.get_list_orders('BUY','OPEN')
        list_orders_sell = self.get_list_orders('SELL', 'OPEN')
        for buy in list_orders_buy:
            self.set_cancel_order(buy['order_id'])
        for sell in list_orders_sell:
            self.set_cancel_order(sell['order_id'])

    def set_edit_limit_order(self,id,price,size):
        request_path = '/api/v3/brokerage/orders/edit'
        payload = json.dumps({
            "order_id": str(id),
            "price": str(price),
            "size": str(size)
        })
        print(payload)
        self.Update('POST', request_path, payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        return json.loads(data.decode("utf-8"))
    def set_order_edit_preview(self,id,price,size):
        request_path = '/api/v3/brokerage/orders/edit_preview'
        payload = json.dumps({
            "order_id": str(id),
            "price": str(price),
            "size": str(size)
        })
        print(payload)
        self.Update('POST', request_path, payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        return json.loads(data.decode("utf-8"))
    def get_product(self):
        request_path = "/api/v3/brokerage/products/BTC-USD"
        payload = ''
        self.Update('GET', request_path, payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        return json.loads(data.decode("utf-8"))
    def get_account(self,id):
        request_path = "/api/v3/brokerage/accounts/{product_id}".format(product_id = id)
        payload = ''
        self.Update('GET', request_path, payload)
        if self._updated:
            self.conn.request(self.method, self.request_path, self.payload, self.headers)
            res = self.conn.getresponse()
            data = res.read()
        else:
            return 'Error:you need update data'
        return json.loads(data.decode("utf-8"))
    def btc_balance(self):
        available = float(self.get_account(os.environ.get('btc_account_id'))['account']['available_balance']['value'])
        hold = float(self.get_account(os.environ.get('btc_account_id'))['account']['hold']['value'])
        price = float(self.get_product()['price'])
        return round(price*(available+hold),2)
    def btc_amount(self):
        available = float(self.get_account(os.environ.get('btc_account_id'))['account']['available_balance']['value'])
        hold = float(self.get_account(os.environ.get('btc_account_id'))['account']['hold']['value'])
        return (available+hold)
    def usd_balance(self):
        available = float(self.get_account(os.environ.get('usd_account_id'))['account']['available_balance']['value'])
        hold = float(self.get_account(os.environ.get('usd_account_id'))['account']['hold']['value'])
        return round((available + hold), 2)
