class Talaba:
    talabalar_soni=0
    def __init__(self,ism,familiya,guruh,shartnoma):
        self.ism = ism
        self.familiya = familiya
        self.guruh = guruh
        self.shartnoma=shartnoma
        self.bosqich = 0
        Talaba.talabalar_soni+=1
        self.__id=Talaba.talabalar_soni

    @classmethod
    def obyektlar_soni(cls):
        return cls.talabalar_soni

    def get_fullname(self):
        return f"{self.ism} {self.familiya}"

    def get_id(self):
        return self.__id
    
    def change_id(self,ID):
        self.__id=ID
    
    def get_info(self):
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def get_age(self,yil):
        return yil - self.t_yil
    
    def set_bosqich(self,y_bosqich):
        self.bosqich = y_bosqich
        
    def update_bosqich(self):
        self.bosqich += 1
        

class Shaxs:
    odamlar_soni=0
    def __init__(self,ism,familiya,ish_joyi,tyil,jshshir):
        self.ism=ism
        self.familiya=familiya
        self.ish_joyi=ish_joyi
        self.tyil=tyil
        self.passport="AA1234567"
        self.__jshshir=jshshir
        Shaxs.odamlar_soni+=1
        
    @classmethod
    def obyektlar_soni(cls):
        return cls.odamlar_soni
        
    def get_stir(self):
        return self.__jshshir
    
    def change_stir(self,stir):
        self.__jshshir=stir
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport:{self.passport}, {self.tyil}-da tug'ilgan" 
        return info
    
    def get_age(self,yil):
        return yil-self.tyil