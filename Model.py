class EiLeitudElementi(Exception):
    pass

class Model:
    def __init__(self, p_elemendid):
        self.elemendid = p_elemendid

    def lisa_element(self, p_nimetus, p_hind, p_kogus):
        self.elemendid.append({"Nimetus": p_nimetus, "Hind": p_hind, "Kogus": p_kogus})

    def loe_elemendid(self):
        return self.elemendid

    def loe_element(self, p_nimetus):
        try:
            for element in self.elemendid:
                if p_nimetus in element.values():
                    return element, ""
            raise EiLeitudElementi("Nimekirjast ei leitud elementi '{}'".format(p_nimetus))
        except EiLeitudElementi as viga:
            return {}, viga

    def kustuta_element(self, p_nimetus):
        self.elemendid.remove(self.loe_element(p_nimetus)[0])

    def kustuta_kõik(self):
        self.elemendid = []

    def uuenda_elementi(self, p_nimetus, p_hind, p_kogus):
        vana_hind = self.loe_element(p_nimetus)[0]["Hind"]
        vana_kogus = self.loe_element(p_nimetus)[0]["Kogus"]
        self.loe_element(p_nimetus)[0]["Hind"] = p_hind
        self.loe_element(p_nimetus)[0]["Kogus"] = p_kogus
        return vana_hind, vana_kogus