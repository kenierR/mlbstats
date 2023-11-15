import json, hmac, hashlib, time, base64 , secrets


timestamp = str(int(time.time()))
#request.method = 'GET'
#request.path_url.split('?')[0] = /api/v3/brokerage/orders/historical/batch
message = timestamp + 'GET' + '/api/v3/brokerage/products/BTC-USD/ticker' + ''
signature = hmac.new(secrets.secretKey.encode('utf-8'), message.encode('utf-8'), digestmod=hashlib.sha256).digest()
print(signature)




