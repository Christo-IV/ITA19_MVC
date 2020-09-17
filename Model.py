class Model:
    def __init__(self, p_elemendid):
        self.elemendid = p_elemendid

    def lisa_element(self, p_nimetus, p_hind, p_kogus):
        self.elemendid.append({"Nimetus":p_nimetus, })

    def lisa_elemendid(self, p_elemendid):
        for element in p_elemendid:
            self.lisa_element(element)

    def loe_elemendid(self):
        return self.elemendid

    def loe_element(self, p_nimetus):
        for element in self.elemendid:
            if p_nimetus in element.values():
                return element
        #raise EiLeitudElementi

    def kustuta_element(self, p_nimetus):
        self.elemendid.remove(p_nimetus)

    def kustuta_elemendid(self):
        self.elemendid = []

    def muuda_element(self, p_mida, p_milleks):
        for element in self.elemendid:
            if p_mida in element.values():
                pass