from django.shortcuts import render
from django.shortcuts import render
from Crypto.source.cb import CB
from datetime import date
from datetime import datetime
# Create your views here.

precios = []
tiempo = []
top = []
btc_bal = []
btc_to_buy = []
def index(request):
    precio_compra = 36800
    rango = 100
    time_len = 200
    content = {}
    sp = CB()
    spot = sp.spot()
    #precios.insert(len(spot),spot)
    precios.append(float(spot))
    now = datetime.now()
    t = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    tiempo.append(t)
    top.append(float(precio_compra))

    #obtener valance
    btc_balance_inc = sp.btc_balance_inc(precio_compra,rango)
    btc_balance_dec = sp.btc_balance_inc(precio_compra,-rango)
    btc_bal.append(btc_balance_inc)
    btc_to_buy.append(btc_balance_dec)
    btc_balance = sp.btc_balance()
    total_balane = float(btc_balance) + float(sp.usd_balance())


    content['precios'] = precios[-time_len:]
    content['tiempo']  = tiempo[-time_len:]
    content['top'] = top[-time_len:]
    content['btc_balance_inc'] = btc_bal[-time_len:]
    content['btc_balance'] = btc_balance
    content['btc_to_buy'] = btc_to_buy[-time_len:]
    content['usd_balance'] = sp.usd_balance()
    content['total_balance'] = total_balane
    #print(content['precios'])
    return render(request,'Crypto/index.html',content)