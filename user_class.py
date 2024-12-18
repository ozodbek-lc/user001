
class USER:
    def __init__(self,tel_nomer,kartasi,passwort,balans,client):
        self.tel_nomer=tel_nomer
        self.kartasi=kartasi
        self.passwort=passwort
        self.balans=balans
        self.karzinka=[]
        # self.admin=True
        self.client=client
    def add_karzinka(self,mahsulot):
        self.karzinka.append(mahsulot)
    def balans_harajat(self,minus):
        self.balans-=minus


user=USER(998909997788,1,1122,1000000,True)
user1=USER(998909997781,1,1122,1000000,True)
user2=USER(998909997782,1,1122,1000000,True)
user3=USER(998909997783,1,1122,1000000,True)
user4=USER(776655,778899,1111,5000000,False)