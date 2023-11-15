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
def index(request):
    precio_compra = 35451
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
    btc_balance = sp.btc_balance(precio_compra,50)
    btc_bal.append(btc_balance)
    print('balance:',btc_balance)


    content['precios'] = precios[-1200:]
    content['tiempo']  = tiempo[-1200:]
    content['top'] = top[-1200:]
    content['btc_balance'] = btc_bal[-1200:]
    #print(content['precios'])
    return render(request,'Crypto/index.html',content)