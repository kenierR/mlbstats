from coinbase.wallet.client import Client
from Crypto.source.cb import CB
import pandas as pd
# coinbase_API_key = "6xLCMtGOQPiitK5O"
# coinbase_API_secret = "OdgFYrpVfgZ3XnRpZ7mchTN8AqFKu9Kp"
#
# client = Client(coinbase_API_key, coinbase_API_secret)
#
# precioCompra = client.get_buy_price()
# precioVenta = client.get_sell_price()
# precioSpot  = client.get_spot_price()
# print('compra:',precioCompra['amount'])
# print('venta :',precioVenta['amount'])
# print('spot  :',precioSpot['amount'])



aux = CB()
print(aux.spot()['amount'])
