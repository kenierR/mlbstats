from Stats.models import *
import statsapi as sap

def UpdatePosition():
    pos = sap.meta('positions')
    dbPos = Position()
    for key,value in pos.items:
        dbPos[key]=value

    dbPos.save()
