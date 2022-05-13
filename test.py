# Tee ratkaisusi tähän:
 
class Suoritus:
 
    def __init__(self, kurssi: str):
        self.__kurssi = kurssi
        self.__arvosanat = ""
        self.__opintopisteet = ""
 
 
    def kurssi(self):
        return self.__kurssi
 
    def arvosanat(self):
        return self.__arvosanat
 
    def lisaa_arvosana(self, arvosana: int):
        if(self.__arvosanat < arvosana):
            self.__arvosanat = arvosana
 
    def opintopisteet(self):
        return self.__opintopisteet
 
    def lisaa_opintopisteet(self, opintopisteet: int):
        self.__opintopisteet = opintopisteet 
   
 
 
class Suoritukset:
    def __init__(self):
        self.kurssit = {}
 
    def lisaa_suoritus(self,kurssi:str, arvosana: int, opintopisteet: int ):
        if not kurssi in self.kurssit:
            self.kurssit[kurssi] = Suoritus(kurssi)     
        self.kurssit[kurssi].lisaa_arvosana(arvosana)
        self.kurssit[kurssi].lisaa_opintopisteet(opintopisteet)
        #tätä pitäisi jotenkin muokata
        print(self.kurssit.items())

    def haeArvosanat(self):
        for arvosana in self.kurssit.get("arvosanat"):
            print(arvosana)
 
    def hae_tiedot(self, kurssi: str):
        if not kurssi in self.kurssit:
            return None
        return self.kurssit[kurssi]

    def selaa_tiedot(self):
        for kurssi in self.kurssit:
             #miten saa arvosanat ja opintopisteet loopaamalla näkyviin?, nyt antaa vain kurssin ( nimen, avain?)
                for kurssi in self.kurssit:
                   
                    print(kurssi)
            
    
                   
    
 
class SuorituksetSovellus:
    def __init__(self):
        self.suoritukset = Suoritukset()

 
    def ohje(self):
        print("komennot: ")        
        print("1 lisää suoritus")
        print("2 hae suoritus")
        print("3 tilastot")
        print("0 lopetus")
 
    def suorituksen_lisays(self):
        kurssi = input("kurssi: ")
        arvosana = input("arvosana: ")
        opintopisteet = input("opintopisteet: ")
        self.suoritukset.lisaa_suoritus(kurssi, arvosana, opintopisteet) 
 
    def haku(self):
        kurssi = input("kurssi: ")
        Suoritus = self.suoritukset.hae_tiedot(kurssi)
        if Suoritus == None:
            print("ei suoritusta")
            return
        print(f"{kurssi} ({Suoritus.opintopisteet()} op) arvosana {Suoritus.arvosanat()}")
    
    
    def tilastot(self):
        self.suoritukset.selaa_tiedot()
       
    
    def suorita(self):
        self.ohje()
        while True:
            print("")
            komento = input("komento: ")
            if komento == "0":
                break
            elif komento == "1":
                self.suorituksen_lisays()
            elif komento == "2":
                self.haku()
            elif komento == "3":
                self.tilastot()
            else:
                self.ohje()
 
 
# kun testaat, mitään muuta koodia ei saa olla luokkien ulkopuolella kuin seuraavat rivit
sovellus = SuorituksetSovellus()
sovellus.suorita()