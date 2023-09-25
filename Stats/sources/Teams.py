import  statsapi as sap
import json

class Teams():
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])


# teams = sap.lookup_team('NYY')[0]
# print(type(teams))
# aux = json.dumps(Teams(teams).__dict__)
# auxload = json.loads(aux)
# print(type(auxload))
# for key in auxload:
#     print(key,auxload[key])


class SoyUnico(object):

    __instance = None
    nombre = None

    def __str__(self):
        return 'self' + ' ' + self.nombre

    def __new__(cls):
        if SoyUnico.__instance is None:
            SoyUnico.__instance = object.__new__(cls)
        return SoyUnico.__instance

aux = SoyUnico()
aux.nombre = 'kenier'
pp = SoyUnico()
pp.nombre = 'pp'

print(aux,pp)