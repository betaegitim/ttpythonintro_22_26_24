class kediler():
    def __init__(self,isim,asili:bool,cipli:bool):
        self.isim=isim
        self.asili=asili
        self.cipli=cipli

    def asilimi(self):
        return self.asili

    def ciplimi(self):
        return self.cipli

    def isim(self):
        return self.isim

mirnav=kediler("mirnav",True,True)
pamuk=kediler("pamuk",False,True)
selo=kediler("selo",False,False)

if mirnav.asilimi:
    print ("mırnav aşılı")

