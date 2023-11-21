import json, hmac, hashlib, time, requests
from requests.auth import AuthBase
import os
# Before implementation, set environmental variables with the names API_KEY and API_SECRET
API_KEY = os.environ.get('coinbase_API_key')
API_SECRET = os.environ.get('coinbase_API_secret')


# Create custom authentication for Coinbase API
class CoinbaseWalletAuth(AuthBase):
    def __init__(self, api_key, secret_key):
        self.api_key = api_key
        self.secret_key = secret_key

    def __call__(self, request):
        timestamp = str(int(time.time()))

        # the following try statement will fix the bug
        try:
            body = request.body.decode()
            if body == "{}":
                request.body = b""
                body = ''
        except AttributeError:
             request.body = b""
             body = ''


        message = timestamp + request.method + request.path_url + body
        signature = hmac.new(self.secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()
        request.headers.update({
                'CB-ACCESS-SIGN': signature,
                'CB-ACCESS-TIMESTAMP': timestamp,
                'CB-ACCESS-KEY': self.api_key,
        })
        return request


api_url = 'https://api.coinbase.com/v3/brokerage/'
auth = CoinbaseWalletAuth(API_KEY, API_SECRET)

# Get current user
r = requests.get(api_url + 'orders/historical/c5a2f91f-ef43-4499-ab02-50af8d7e3934', auth=auth)
print(r.json())