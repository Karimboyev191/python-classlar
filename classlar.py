
"""
Created on Tue Jan  2 19:18:35 2024

@author: Karimboyev Xudoybergan
"""

# class Shaxs:
#     def __init__(self,ism,familiya,tyil):
#         self.ism=ism
#         self.familiya=familiya
#         self.tyil=tyil
        
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}. "
#         return info
        
#     def get_age(self,yil):
#         return yil-self.yil
    
# class Professor(Shaxs):
#     def __init__(self,ism,familiya,tyil,tel):
#         super().__init__(ism,familiya,tyil)
#         self.tel=tel
        
#     def get_info(self):
#         info=super().get_info()
#         info+= self.tel
#         return info
    
# class Foydalanuvchi(Shaxs):
#     def __init__(self,ism,familiya,tyil,tel):
#         super().__init__(ism,familiya,tyil)
#         self.tel=tel
        
#     def get_info(self):
#         info=super().get_info()
#         info+=self.tel
#         return info
    
# class Sotuvchi(Shaxs):
#     def __init__(self,ism,familiya,tyil,tel):
#         super().__init__(ism,familiya,tyil)
#         self.tel=tel
        
#     def get_info(self):
#         info=super().get_info()
#         info+=self.tel
#         return info
    
# class Mijoz(Shaxs):
#     def __init__(self,ism,familiya,tyil,tel):
#         super().__init__(ism,familiya,tyil)
#         self.tel=tel
        
#     def get_info(self):
#         info=super().get_info()
#         info+=self.tel
#         return info
# class Admin(Foydalanuvchi):
#     def __init__(self,ism,familiya,tyil,tel,login):
#         super().__init__(ism,familiya,tyil,tel)
#         self.login=login
        
#     def get_info(self):
#         info=super().get_info()
#         info+=self.login
#         return info
    
#     def ban_user(self,login):
#         print("Foydalanuvchi bloklandi")
    
# inson1=Shaxs("Izzat","Abdusharipov",2004)
# inson1=Foydalanuvchi("Izzat","Abdusharipov",2004,"+998904340477")
# inson1=Admin("Izzat","Abdusharipov",2004,"+998904340477","Izzat9011")




# class Talaba:
#     talabalar_soni=0
#     def __init__(self,ism,familiya,guruh,shartnoma):
#         self.ism = ism
#         self.familiya = familiya
#         self.guruh = guruh
#         self.shartnoma=shartnoma
#         self.bosqich = 0
#         Talaba.talabalar_soni+=1
#         self.__id=Talaba.talabalar_soni

#     @classmethod
#     def obyektlar_soni(cls):
#         return cls.talabalar_soni

#     def get_fullname(self):
#         return f"{self.ism} {self.familiya}"

#     def get_id(self):
#         return self.__id
    
#     def change_id(self,ID):
#         self.__id=ID
    
#     def get_info(self):
#         return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
#     def get_age(self,yil):
#         return yil - self.t_yil
    
#     def set_bosqich(self,y_bosqich):
#         self.bosqich = y_bosqich
        
#     def update_bosqich(self):
#         self.bosqich += 1
        

# class Shaxs:
#     odamlar_soni=0
#     def __init__(self,ism,familiya,ish_joyi,tyil,jshshir):
#         self.ism=ism
#         self.familiya=familiya
#         self.ish_joyi=ish_joyi
#         self.tyil=tyil
#         self.passport="AA1234567"
#         self.__jshshir=jshshir
#         Shaxs.odamlar_soni+=1
        
#     @classmethod
#     def obyektlar_soni(cls):
#         return cls.odamlar_soni
        
#     def get_stir(self):
#         return self.__jshshir
    
#     def change_stir(self,stir):
#         self.__jshshir=stir
    
#     def get_info(self):
#         info = f"{self.ism} {self.familiya}. "
#         info += f"Passport:{self.passport}, {self.tyil}-da tug'ilgan" 
#         return info
    
#     def get_age(self,yil):
#         return yil-self.tyil
    
    
# a1=Talaba("Izzat","Abdusharipov","931-22","Kontrakt")
# a2=Shaxs("Xudoybergan","Karimboyev","Baraka MCHJ",2004,21324354566556)

# print(a1.get_id())
# a1.change_id(3)
# print(a1.get_id())

# print(a2.get_stir())
# a2.change_stir(2535343242)
# print(a2.get_stir())













