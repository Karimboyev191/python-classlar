class Avto:
    __num_avto = 0
    def __init__(self, model, rang, korobka, narh, pozitsiya,yili):
        self.nomi = model
        self.rangi = rang
        self.korobkasi = korobka
        self.narxi = narh
        self.pozitsiyasi = pozitsiya
        self.yili = yili
        self.kilometr = 0
        Avto.__num_avto+=1
        
    def get_info(self):
        full = f"nomi: {self.nomi} ,"
        full += f"rangi: {self.rangi} ,"
        full += f"korobkasi: {self.korobkasi} ,"
        full += f"narhi: {self.narxi} ,"
        full += f"pozitsiyasi: {self.pozitsiyasi} ,"
        full += f"yili: {self.yili} ,"
        full += f"kilometri: {self.kilometr}"
        return full
    
    def __repr__(self):
        return self.nomi
    
    def update_km(self, qiymat):
        self.kilometr = self.kilometr + qiymat


class Avtosalon:
    def __init__(self, nomi, manzili, telefoni):
        self.nomi = nomi
        self.manzili = manzili
        self.telefoni = telefoni
        self.avtomobillar = []
        
    def __repr__(self):
        return f"{self.nomi} avtosaloni"
    
    def add_avto(self, *avtolar):
        for avto in avtolar:
            if isinstance(avto, Avto):
                self.avtomobillar.append(avto)
            else:
                print("Avto kiriting")
    
    def __getitem__(self,index):
        return self.avtomobillar[index]
    
    def __setitem__(self,index,qiymat):
        self.avtomobillar[index]=qiymat
        
    def __call__(self,*qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtomobillar]
            
         
avto1 = Avto("BMW M5", "qora", "avtomat", 250000, "competition sport", 2023)
avto2 = Avto("Lexus ISF350","oq", "avtomat", 150000, "ISF", 2022)

dukon1 = Avtosalon("DID", "Toshkent", "+998904340477")