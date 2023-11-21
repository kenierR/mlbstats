import datetime
import time
import hmac
import hashlib
import http.client
import os,json
import uuid

class my_cb_apis():
  def __init__(self):
      self.conn = http.client.HTTPSConnection("api.coinbase.com")
      self.api_key = os.environ.get('coinbase_API_key')
      self.secret_key = os.environ.get('coinbase_API_secret')

  def Update(self,method,request_path,payload):
    timestamp = str(int(time.time()))
    message = str(timestamp) + method + request_path + payload
    signature = hmac.new(self.secret_key.encode('utf-8'), message.encode('utf-8'), hashlib.sha256).hexdigest()
    conn = http.client.HTTPSConnection("api.coinbase.com")
    headers = {
      'accept': 'application/json',
      'CB-ACCESS-KEY': self.api_key,
      'CB-ACCESS-TIMESTAMP': timestamp,
      'CB-ACCESS-SIGN': signature
    }

    conn.request(method, request_path, payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

payload = json.dumps({
  "client_order_id": str(uuid.uuid4()),
  "product_id": "BTC-USD",
  "side": "SELL",
  "order_configuration": {
    "limit_limit_gtc": {
      "base_size": "0.00002",
      "limit_price": "50000"
    }
  }
})

aux = my_cb_apis()
aux.Update('POST',request_path = "/api/v3/brokerage/orders",payload=payload)






#conn.request("POST", "/api/v3/brokerage/orders", payload, headers)
# You were probably troubleshooting, but the above line is redundant and can be simplified to:





