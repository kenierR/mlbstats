import http.client
import json
import json, hmac, hashlib, time, base64,os

conn = http.client.HTTPSConnection("api.coinbase.com")
timestamp = str(int(time.time()))
method = 'GET'
request_path = '/api/v3/brokerage/products/BTC-USD/ticker'
body = ''
payload = timestamp+method+request_path+body
signature = hmac.new(os.environ.get('coinbase_API_secret').encode('utf-8'), payload.encode('utf-8'), digestmod=hashlib.sha256).digest()

headers = {
  'Content-Type': 'application/json',
  'cb-access-key': os.environ.get('coinbase_API_key'),
  'cb-access-passphrase': os.environ.get('coinbase_API_secret'),
  'cb-access-sign': signature,
  'cb-access-timestamp': timestamp
}
conn.request("GET", "/api/v3/brokerage/accounts?limit=2", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))