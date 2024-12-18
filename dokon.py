from mahsulot import Mahsulotlar

class Dokon:
    def __init__(self, nomi, location):
        self.nomi = nomi
        self.location = location
        self.balanc = 0
        self.maxsulot_baza = []
        self.korzinka=[]

    def info_dokon(self):
        return f"nomi : {self.nomi}\nJoylashuv : {self.location}\nBalans : {self.balanc}"

    def info_maxsulot(self, mahsulot):
        return f"nomi : {mahsulot.nomi}\nnarxi : {mahsulot.narxi}\nmuddati : {mahsulot.muddati}"

dokon = Dokon("Korzinka", "Beruniy metro")
print(dokon.info_dokon())
