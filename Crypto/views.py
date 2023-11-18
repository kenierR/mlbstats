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
    content = {}
    sp = CB()
    spot = sp.spot()
    #precios.insert(len(spot),spot)
    print(spot)
    precios.append(float(spot))
    now = datetime.now()
    t = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    tiempo.append(t)
    top.append(float(precio_compra))
    print(top)

    #obtener valance
    btc_balance_inc = sp.btc_balance_inc(precio_compra,100)
    btc_balance_dec = sp.btc_balance_inc(precio_compra,-100)
    btc_bal.append(btc_balance_inc)
    btc_to_buy.append(btc_balance_dec)
    print('balance:',btc_balance_inc)
    btc_balance = sp.btc_balance()


    content['precios'] = precios[-200:]
    content['tiempo']  = tiempo[-200:]
    content['top'] = top[-200:]
    content['btc_balance_inc'] = btc_bal[-200:]
    content['btc_balance'] = float(btc_balance)
    content['btc_to_buy'] = btc_to_buy[-200:]

    #print(content['precios'])
    return render(request,'Crypto/index.html',content)