from django.shortcuts import render
from django.shortcuts import render
from Crypto.source.cb import CB
from datetime import date
from datetime import datetime
from Crypto.source.Bot import Bot
# Create your views here.
bot = Bot()
precios = []
tiempo = []
list_prec_comp = []
list_prec_venta = []
btc_bal = []
btc_to_buy = []

def index(request):
    rango = 100
    time_len = 200
    content = {}
    bot.update_order()
    try:
        precio_compra = bot.Mbb.get_list_orders('BUY' ,'OPEN')[0]['order_configuration']['limit_limit_gtc']['limit_price']
    except:
        precio_compra = bot.Mbb.get_order(bot.last_buy_order_id)['order']['order_configuration']['limit_limit_gtc']['limit_price']
    try:
        precio_venta = bot.Mbb.get_list_orders('SELL', 'OPEN')[0]['order_configuration']['limit_limit_gtc']['limit_price']
    except:
        precio_venta = bot.Mbb.get_order(bot.last_sell_order_id)['order']['order_configuration']['limit_limit_gtc']['limit_price']

    spot = bot.Mbb.get_product()['price']
    precios.append(float(spot))
    now = datetime.now()
    t = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
    tiempo.append(t)
    list_prec_comp.append(float(precio_compra))
    list_prec_venta.append(float(precio_venta))
    content['precios'] = precios[-time_len:]
    content['tiempo']  = tiempo[-time_len:]
    content['list_prec_comp'] = list_prec_comp[-time_len:]
    content['list_prec_venta'] = list_prec_venta[-time_len:]



    return render(request,'Crypto/index.html',content)