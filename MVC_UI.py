from Model import Model
from View import View
from Controller import Controller

data = [
    {"Nimetus": "Leib", "Hind": 0.80, "kogus": 20},
    {"Nimetus": "Piim", "Hind": 0.50, "kogus": 15},
    {"Nimetus": "Vein", "Hind": 5.60, "kogus": 5}
]

Maxima = Controller(Model(data), View())

#Maxima.kuva_elemendid()
Maxima.kuva_element("Vein")