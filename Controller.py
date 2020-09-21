class Controller:
    def __init__(self, p_model, p_view):
        self.model = p_model
        self.view = p_view

    # Elemendi kuvamine
    def kuva_elemendid(self):
        elemendid = self.model.loe_elemendid()
        self.view.kuva_elemendid(elemendid)

    def kuva_element(self, p_nimetus):
        element, veateade = self.model.loe_element(p_nimetus)
        if veateade == "":
            self.view.kuva_element(element)
        else:
            self.view.veateade(veateade)

    def lisa_element(self, p_nimetus, p_hind, p_kogus):
        if p_hind <= 0:
            self.view.veateade("Hind peab olema suurem kui 0")
        elif p_kogus <= 0:
            self.view.veateade("Kogus peab olema suurem kui 0")
        else:
            self.model.lisa_element(p_nimetus, p_hind, p_kogus)
            self.view.lisa_element(p_nimetus, p_hind, p_kogus)

    def uuenda_elementi(self, p_nimetus, p_hind, p_kogus):
        if p_hind <= 0:
            self.view.veateade("Hind peab olema suurem kui 0")
        elif p_kogus <= 0:
            self.view.veateade("Kogus peab olema suurem kui 0")
        else:
            vana_hind, vana_kogus = self.model.uuenda_elementi(p_nimetus, p_hind, p_kogus)
            self.view.uuenda_elementi(p_nimetus, vana_hind, p_hind, vana_kogus, p_kogus)

    def kustuta_element(self, p_nimetus):
        self.model.kustuta_element(p_nimetus)
        self.view.kustuta_element(p_nimetus)

    def kustuta_kõik(self):
        self.model.kustuta_kõik()
        self.view.kustuta_kõik()