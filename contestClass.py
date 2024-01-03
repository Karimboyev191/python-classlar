class Massiv():
    def __init__(self,*m):
        self.m=list(m)
        
    def get(self):
        print(*self.m)
        
    def swap(self,k,l):
        self.m[k-1], self.m[l-1]=self.m[l-1],self.m[k-1]
        print(*self.m)

    def matrix(self, n):
        rows = len(self.m)
        for i in range(rows):
            s = i * n
            e = (i + 1) * n
            r = self.m[s:e]
            print(*r)
        
    def qushish(self,k):
        q=[]
        for i in self.m:
            q.append(i+k)
            
        print(*q)
    
    def kupaytir(self,k,l,son):
        
        for i in range(k,l):
            self.m[i] *= son
            
        print(*self.m)
            
    def teskarisiga_qushish(self):
        t = self.m[::-1]  
        r=[]
        for x,y in zip(self.m,t):
            r.append(x+y)
        self.m=r
        print(*self.m)
        
            
a=Massiv(4,2,11,7,9,5,1)        
        
    
class Matn():
    def __init__(self,satr):
        self.satr=satr

    def get(self):
        print(self.satr)
        
    def uchirish(self,k):
        s=self.satr[:k-1]+self.satr[k:]
        print(s)
        
    def kiritish(self,n,matn):
        s=self.satr[:n] + matn + self.satr[n:]
        print(s)
        
    def katta_harf(self,k):
        s=self.satr[:k-1] + self.satr[k-1].upper() + self.satr[k:]
        print(s)
        
    def almashtirish(self,k,l):
        s = self.satr[:k-1] + self.satr[l-1] + self.satr[k:l-1] + self.satr[k-1] + self.satr[l:]
        print(s)
        
    def belgi_kupaytirish(self,n):
        s=""
        for i in self.satr:
            s+=i*n
        print(s)
        
        
b=Matn("Uzbekistan")