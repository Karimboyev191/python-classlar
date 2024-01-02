
"""
Created on Tue Jan  2 19:18:35 2024

@author: Karimboyev Xudoybergan
"""

class Shaxs:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        return info
        
    def get_age(self,yil):
        return yil-self.yil
    
class Professor(Shaxs):
    def __init__(self,ism,familiya,tyil,tel):
        super().__init__(ism,familiya,tyil)
        self.tel=tel
        
    def get_info(self):
        info=super().get_info()
        info+= self.tel
        return info
    
class Foydalanuvchi(Shaxs):
    def __init__(self,ism,familiya,tyil,tel):
        super().__init__(ism,familiya,tyil)
        self.tel=tel
        
    def get_info(self):
        info=super().get_info()
        info+=self.tel
        return info
    
class Sotuvchi(Shaxs):
    def __init__(self,ism,familiya,tyil,tel):
        super().__init__(ism,familiya,tyil)
        self.tel=tel
        
    def get_info(self):
        info=super().get_info()
        info+=self.tel
        return info
    
class Mijoz(Shaxs):
    def __init__(self,ism,familiya,tyil,tel):
        super().__init__(ism,familiya,tyil)
        self.tel=tel
        
    def get_info(self):
        info=super().get_info()
        info+=self.tel
        return info
class Admin(Foydalanuvchi):
    def __init__(self,ism,familiya,tyil,tel,login):
        super().__init__(ism,familiya,tyil,tel)
        self.login=login
        
    def get_info(self):
        info=super().get_info()
        info+=self.login
        return info
    
    def ban_user(self,login):
        print("Foydalanuvchi bloklandi")
    
inson1=Shaxs("Izzat","Abdusharipov",2004)
inson1=Foydalanuvchi("Izzat","Abdusharipov",2004,"+998904340477")
inson1=Admin("Izzat","Abdusharipov",2004,"+998904340477","Izzat9011")