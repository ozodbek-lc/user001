class Dokon:
    def __init__(self,nomi,balansi):
        self.nomi=nomi
        self.balansi=balansi
        self.mahsulot_bazasi=[]
        self.istorya=[]
    def add_mahsulot(self,malumot):
        self.mahsulot_bazasi.append(malumot)
        print("qoshildi")
    def del_mahsulot(self,malumot):
        if malumot in self.mahsulot_bazasi:
            self.mahsulot_bazasi.remove(malumot)
            print("o'chirildi")
        else: print("bunday malumot movjud emas")
    def add_istorya(self,malimot):
        self.istorya.append(malimot)
    def mohsulotlar_bazasi(self):
        for i in self.mahsulot_bazasi:
            print(i)
dokon=Dokon("karzinka",100000000)