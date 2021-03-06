class View:
    def kuva_elemendid(self, p_elemendid):
        print("Kõik elemendid:")
        print("{:<10} | {:>10} | {:>10}".format("Nimetus", "Hind", "Kogus"))
        print("---------------------------------------")
        for element in p_elemendid:
            print("{:<10} | {:>10}€ | {:>10}tk".format(element["Nimetus"], element["Hind"], element["Kogus"]))
        print("---------------------------------------\n")

    def kuva_element(self, p_element):
        print("Elemendi {} andmed:".format(p_element["Nimetus"]))
        print("{:<10} | {:>10} | {:>10}".format("Nimetus", "Hind", "Kogus"))
        print("---------------------------------------")
        print("{:<10} | {:>10}€ | {:>10}tk".format(p_element["Nimetus"], p_element["Hind"], p_element["Kogus"]))
        print("---------------------------------------\n")

    def lisa_element(self, p_nimetus, p_hind, p_kogus):
        print("Lisatud '{}' element:".format(p_nimetus))
        print("{:<10} | {:>10} | {:>10}").format("Nimetus", "Hind", "Kogus")
        print("---------------------------------------")
        print("{:<10} | {:>10} | {:>10}".format(p_nimetus, p_hind, p_kogus))
        print("---------------------------------------\n")

    def veateade(self, p_viga):
        print("---[ Viga: {} ]---\n".format(p_viga))

    def uuenda_elementi(self, p_nimetus, vana_hind, uus_hind, vana_kogus, uus_kogus):
        if vana_hind != uus_hind:
            print("Muudetud elemendi '{}' hind: {}€ --> {}€".format(p_nimetus, vana_hind, uus_hind))
        if vana_kogus != uus_kogus:
            print("Muudetud elemendi '{}' kogus: {}tk --> {}tk".format(p_nimetus, vana_kogus, uus_kogus))
        print()

    def kustuta_element(self, p_nimetus):
        print("Element '{}' on nimekirjast kustutatud\n".format(p_nimetus))

    def kustuta_kõik(self):
        print("Kõik elemendid on nimekirjast kustutatud\n")