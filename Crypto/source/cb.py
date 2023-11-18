from coinbase.wallet.client import Client
import os

class CB:
    def __init__(self):
        self.coinbase_API_key = os.environ.get('coinbase_API_key')
        self.coinbase_API_secret = os.environ.get('coinbase_API_secret')
        self.client = Client(self.coinbase_API_key, self.coinbase_API_secret)

    def spot(self):
        return self.client.get_spot_price()['amount']
    def account(self):
        return self.client.get_accounts()

    def btc_balance_inc(self,precio_comp,inc):
        balance = float(self.client.get_primary_account()['balance']['amount'])*float(precio_comp)
        esperado_valor = balance+float(inc)
        #print('balance:',balance,'valor esperado:',esperado_valor,'satohis:',self.client.get_primary_account()['balance']['amount'])
        return esperado_valor//float(self.client.get_primary_account()['balance']['amount'])
    def btc_balance(self):
        balance = float(self.client.get_primary_account()['balance']['amount'])*float(self.spot())
        return "{:.2f}".format(balance)
    def usd_balance(self):
        return "{:.2f}".format(float(self.client.get_account('USD')['balance']['amount']))
