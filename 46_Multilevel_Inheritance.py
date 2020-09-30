class Dad:
    cricket = 10
    _hockey = 20 #protected variable mtlb ya class use kr skti ya jo is sa drive ho class wo
    __football = 0 #private variable class ka jo bs isi class ma use hoo skay
# public - ak cheez jo ap apnay ghr ka gate ka bhr likh ka laga do mtlb koi bi prh la
# protected - jo cheez ap apny ghr ka gate ka andr ki trf likh ka laga do mtlb bs ghr walay arh sakain
# private - jo ap apny room ma looker ma rkh do likh kajo sirf ap prh sakain
class Son(Dad):
    cricket = 20
    hockey = 10
    football = 30

    def Doing(self):
        return f"I am doing my own work"
class Grandson(Son):
    cricket = 0

    def Doing(self): #Concept of polymorphism mtlb overwrite kr gya uscheez ko update kr diya
        return f"I am doing an excellent work work"


d = Dad()
s = Son()
g = Grandson()

a = g.hockey
print(a)
print(d._Dad__football) #tareeqa access krna ka private variable ko python ma is tareeqay ko name angling khty hain