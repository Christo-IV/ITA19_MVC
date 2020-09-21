from Model import Model
from View import View
from Controller import Controller

data = [
    {"Nimetus": "Leib", "Hind": 0.80, "Kogus": 20},
    {"Nimetus": "Piim", "Hind": 0.50, "Kogus": 15},
    {"Nimetus": "Vein", "Hind": 5.60, "Kogus": 5}
]

Maxima = Controller(Model(data), View())

Maxima.kuva_elemendid()

#Maxima.lisa_element("Lada", 399, 9)

#Maxima.kuva_element("Lada")

#Maxima.uuenda_elementi("Piim", 0.87, 20)

Maxima.kustuta_kõik()

Maxima.kuva_elemendid()