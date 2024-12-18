class Dokon:
    def __init__(self,nomi,location):
        self.nomi=nomi
        self.location=location
        self.balanc=0
        self.maxsulot_baza=[]

    def info_dokon(self):
        return f"nomi : {self.nomi}\nJoylashuv"
    def info_mahsulotlar(self):
        for mahsulot in self.maxsulot_baza:
            print(f"{mahsulot}")


while True:
    status=input("1:mahsulotlar")
    # if status=="1":

