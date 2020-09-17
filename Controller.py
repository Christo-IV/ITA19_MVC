class EiLeitudElementi(Exception):
    pass


class Controller:
    def __init__(self, p_model, p_view):
        self.model = p_model
        self.view = p_view


    # Elemendi kuvamine
    def kuva_elemendid(self):
        elemendid = self.model.loe_elemendid()
        self.view.kuva_elemendid(elemendid)

    def kuva_element(self, p_nimetus):
        try:
            element = self.model.loe_element(p_nimetus)
        except EiLeitudElementi:
            element = {}
        self.view.kuva_element(element)