"""
Snack_V3 Opjektorientierter Automat mit Nutzerkonten
"""
Produkt_Namen = ["Mars","Molch", "Schrödigners Katze", "Sicke plays", "Pornobalken zum Aufkleben",
                "Goethes Faust", "Goethes flache Hand", "Waldesel", "P90", "B-rush"]
Produkt_Preise = [1.2, 1.3, 1, 0.5, 3.5, 0.7, 0.6, 4.20, 0.99, 3]
Produkt_Anzahl = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Nutzer_Daten = []
Produkt_Array = []
class Produkte:

    def __init__(self, Name, Preis, Anzahl):
        self.Name = Name
        self.Preis = Preis
        self.Anzahl = Anzahl
    def Lager(self):
        return self.Anzahl
    def Kosten(self):
        return self.Preis

class Nutzer:

    def __init__(self, Bname, Pw, Konto = 0):
        self.Bname = Bname
        self.Pw = Pw
        self.Konto = Konto
        self.Logged_In = False
        

    def Set_Konto(self, Konto):
        self.Konto = Konto

    def Get_Konto(self):
        return self.Konto

    def Einloggen(self):
        for i in Nutzer_Daten:
            if str(i) == self.Bname:
                if Nutzer_Daten[Nutzer_Daten.index(i)+1] == self.Pw:
                    self.Logged_In = 1
                    self.Konto = Nutzer_Daten[Nutzer_Daten.index(self.Bname)+2]
                    return
                else:
                    print("inkorrektes Passwort, absolute Frechheit.")
                    return
        print("error, der Nutzer konnte nicht gefunden werden")
        return
    
    def Registrieren (self):
        for i in Nutzer_Daten:
            if i == self.Bname:
                print("Fehler, der Nutzer existiert bereits")
                return
            else:
                pass
        try:
            Nutzer_Daten.append(self.Bname)
            Nutzer_Daten.append(self.Pw)
            Nutzer_Daten.append(self.Konto)
            print(Nutzer_Daten)
            self.Logged_In = 1
        except ValueError:
            print("das Passwort ist invalide")

    def Ausloggen(self):
        self.Logged_In = 0
        Nutzer_Daten[Nutzer_Daten.index(self.Bname)+2] = self.Konto
        #Daten ins file schreiben

        
                    



class Snacc:

    def __init__(self):
        pass

    def Einzahlung(self, ID):
        """
        Einzahlen auf persönliches Konto
        :param User_Identity: Nutzerkennung zur Kontoaddressierung
        :return: Kontostand
        """

        Kontostand = ID.Get_Konto()

        try:
            Konto_Cache = round(float(input("Wie viel wollen sie einzahlen?")), 2)

            if Konto_Cache > 0:
                Kontostand = Kontostand + Konto_Cache
                print(Kontostand)
                ID.Set_Konto(Kontostand)
            else:
                print("Frech Kati.")

        except ValueError:
            print("Geben sie nur gültige Werte ein! \n")
    
    def Kaufen(self, Name, Preis, Stonks, Bname):
        if Stonks >0:    
            if Preis < Bname.Get_Konto:
                Bname.set_Konto(Bname.Get_Konto - Preis)
                print(f"viel spass mit {Name}")
                Produkt_Anzahl[Produkt_Namen.index(Name)] = Produkt_Anzahl[Produkt_Namen.index(Name)] -1
    
    def Produkt_Init(self):
        for i in range(0,len(Produkt_Namen), 3):
            Produkt_Array[i] = Produkte(Produkt_Namen[i], Produkt_Preise[i], Produkt_Anzahl[i])



if __name__ == "__main__":
    while(1):
        Bname_In = str(input("Username: "))
        Pw_In = str(input("Passwort: "))
        try:
            Reg_Einlog = int(input("Einloggen [0]   Registrieren[1]"))
            print(Reg_Einlog)
        except ValueError:
            print("Keine valide Option")
        User_Identity = Nutzer(Bname_In, Pw_In)            #Fallunterscheidung in Neu oder Alt

        if Reg_Einlog:
            User_Identity.Registrieren()
            Automat_Instanz = Snacc()
            Automat_Instanz.Produkt_Init()

        else: 
            User_Identity.Einloggen()
            Automat_Instanz = Snacc()
            Automat_Instanz.Produkt_Init()

        while (User_Identity.Logged_In):
            Automat_Instanz.Produkt_Init()
            Input_Cache = input("""Willkommen beim Snacc!
            Was wollen sie tun?
                Einzahlen   [1]
                Kaufen      [2]
                Beenden     [3] """)

            if Input_Cache == "1":
                Automat_Instanz.Einzahlung(User_Identity)
                

            elif Input_Cache == "2":
                for i in Produkt_Array:
                    print(i)
                #Automat_Instanz.Kaufen()

            elif Input_Cache == "3":
                User_Identity.Ausloggen()
