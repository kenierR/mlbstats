from coinbase.wallet.client import Client


class CB:
    def __init__(self):
        self.coinbase_API_key = "6xLCMtGOQPiitK5O"
        self.coinbase_API_secret = "OdgFYrpVfgZ3XnRpZ7mchTN8AqFKu9Kp"
        self.client = Client(self.coinbase_API_key, self.coinbase_API_secret)

    def spot(self):
        return self.client.get_spot_price()['amount']
    def account(self):
        return self.client.get_accounts()

    def btc_balance(self,precio_comp,inc):
        balance = float(self.client.get_primary_account()['balance']['amount'])*float(precio_comp)
        esperado_valor = balance+float(inc)
        print('balance:',balance,'valor esperado:',esperado_valor,'satohis:',self.client.get_primary_account()['balance']['amount'])
        return esperado_valor//float(self.client.get_primary_account()['balance']['amount'])
