class View:
    def kuva_elemendid(self, p_elemendid):
        print("Kõik elemendid:")
        for element in p_elemendid:
            print("\t", element)

    def kuva_element(self, p_element):
        print("Ühe elemendi andmed:")
        print("\t", p_element)