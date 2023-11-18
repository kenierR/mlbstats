from coinbase.wallet.client import Client


class CB:
    def __init__(self):
        self.coinbase_API_key = "Cqalyyr0Eu32dpwL"
        self.coinbase_API_secret = "NZgXD5mVnWa1e2e9Eum8quDocb4L8nuF"
        self.client = Client(self.coinbase_API_key, self.coinbase_API_secret)

    def spot(self):
        return self.client.get_spot_price()['amount']
    def account(self):
        return self.client.get_accounts()

    def btc_balance_inc(self,precio_comp,inc):
        balance = float(self.client.get_primary_account()['balance']['amount'])*float(precio_comp)
        esperado_valor = balance+float(inc)
        print('balance:',balance,'valor esperado:',esperado_valor,'satohis:',self.client.get_primary_account()['balance']['amount'])
        return esperado_valor//float(self.client.get_primary_account()['balance']['amount'])
    def btc_balance(self):
        balance = float(self.client.get_primary_account()['balance']['amount'])*float(self.spot())
        return balance
