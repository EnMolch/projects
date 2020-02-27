"""
Snack_V3 Opjektorientierter Automat mit Nutzerkonten
"""
import math
PRODUKT_NAMEN = ["Mars","Molch", "Schrödingers Katze", "Sicke plays", "Pornobalken zum Aufkleben",
                "Goethes Faust", "Goethes flache Hand", "Waldesel", "P90", "B-rush"]
PRODUKT_PREIS = [1.2, 1.3, 1, 0.5, 3.5, 0.7, 0.6, 4.20, 0.99, 3]
PRODUKT_ANZAHL = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
Nutzer_Daten = []
PRODUKT_ARRAY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ADDRESS_OFFSET = 0
PRODUKT_LAGER_HILFE = []
class Produkte:

    def __init__(self, Name, Preis, Anzahl):
        self.Name = Name
        self.Preis = Preis
        self.Anzahl = Anzahl
    def GetLager(self):
        return self.Anzahl
    def GetKosten(self):
        return self.Preis
    def SetLager(self, Anzahl):
        self.Anzahl = Anzahl
    def GetName(self):
        return self.Name

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
        File_Handle = open("save.txt", "w")
        for i in range(len(Nutzer_Daten)):
            if i != 0:
                File_Handle.write(",")
            File_Handle.write(str(Nutzer_Daten[i]))
        File_Handle.write(",")
        File_Handle.write("\n")
        for i in range(len(PRODUKT_LAGER_HILFE)):
            if i!= 0:
                File_Handle.write(",")
            File_Handle.write(str(PRODUKT_LAGER_HILFE[i]))
        
        File_Handle.close()


        
                    

class Snacc:

    def __init__(self):
        pass

    def Einzahlung(self, ID):
        """
        Einzahlen auf persönliches Konto
        :param User_Identity: Nutzerkennung zur Kontoaddressierung
        :return: Kontostand
        """

        Kontostand = float(ID.Get_Konto())

        try:
            Konto_Cache = round(float(input("Wie viel wollen sie einzahlen?  ")), 2)
            print(Kontostand)
            if Konto_Cache > 0:
                Kontostand = Kontostand + Konto_Cache
                print(Kontostand)
                ID.Set_Konto(Kontostand)
            else:
                print("Frech Kati.")

        except ValueError:
            print("Geben sie nur gültige Werte ein! \n")
    
    def Kaufen(self, Name, Preis, Stonks, ID):
        if Stonks >0:
            Kontostand = float(ID.Get_Konto())
            print(Kontostand) 
            if Preis < Kontostand:
                ID.Set_Konto(Kontostand - Preis)
                print(f"viel spass mit {Name}")
                PRODUKT_ANZAHL[PRODUKT_NAMEN.index(Name)] = int(PRODUKT_ANZAHL[PRODUKT_NAMEN.index(Name)]) -1
                PRODUKT_LAGER_HILFE[PRODUKT_NAMEN.index(Name)+ADDRESS_OFFSET] = int(PRODUKT_LAGER_HILFE[PRODUKT_NAMEN.index(Name)+ADDRESS_OFFSET]) -1
            else:
                print("Sieh den Monopolkapitalist, der dich mit Haut und Haaren frist!")
    def Produkt_Init(self, ID):
        for i in range(len(PRODUKT_NAMEN)):
            PRODUKT_ARRAY[i] = Produkte(PRODUKT_NAMEN[i], PRODUKT_PREIS[i], PRODUKT_ANZAHL[i])



if __name__ == "__main__":
    while(1):
        Bname_In = str(input("Username: "))
        Pw_In = str(input("Passwort: "))
        File_Handle = open("save.txt", "r")
        Nutzer_Daten = []
        Nutzer_Daten.extend(File_Handle.readline().split(","))
        Nutzer_Daten.pop()
        print(Nutzer_Daten)

        PRODUKT_LAGER_HILFE = []
        PRODUKT_ANZAHL = []
        PRODUKT_LAGER_HILFE.extend(File_Handle.readline().split(","))
        ADDRESS_OFFSET = (math.floor(float(Nutzer_Daten.index(Bname_In))/3))*10
        for i in range(10):
            PRODUKT_ANZAHL.extend(PRODUKT_LAGER_HILFE[i+ADDRESS_OFFSET])
        print(PRODUKT_ANZAHL)

        File_Handle.close()

        
        try:
            Reg_Einlog = int(input("Einloggen [0]   Registrieren[1]  "))
            print(Reg_Einlog)
            User_Identity = Nutzer(Bname_In, Pw_In)            #Fallunterscheidung in Neu oder Alt

            if Reg_Einlog >0:
                User_Identity.Registrieren()
                Automat_Instanz = Snacc()

            else: 
                User_Identity.Einloggen()
                Automat_Instanz = Snacc()

            while (User_Identity.Logged_In):
                Automat_Instanz.Produkt_Init(Bname_In)
                Input_Cache = input("""Willkommen beim Snacc!
                Was wollen sie tun?
                    Einzahlen   [1]
                    Kaufen      [2]
                    Beenden     [3]  """)

                if Input_Cache == "1":
                    Automat_Instanz.Einzahlung(User_Identity)
                    

                elif Input_Cache == "2":
                    for i in range(len(PRODUKT_ARRAY)):
                        print(ADDRESS_OFFSET)
                        print(PRODUKT_ARRAY[i].GetName(), "    ", PRODUKT_ARRAY[i].GetKosten(),"    " ,PRODUKT_ARRAY[i].GetLager())
                    Name_Buy = str(input("Bitte den Namen des gewünschten Produktes eingeben: "))
                    
                    if Name_Buy in PRODUKT_NAMEN:
                        Temp_Index = PRODUKT_NAMEN.index(Name_Buy)
                        Temp_Preise = PRODUKT_PREIS[Temp_Index]
                        Temp_Anzahl = int(PRODUKT_ANZAHL[Temp_Index])
                        Automat_Instanz.Kaufen(Name_Buy, Temp_Preise , Temp_Anzahl, User_Identity)

                    else:
                        print("Bitte korrekten Produktnamen eingeben")

                elif Input_Cache == "3":
                    User_Identity.Ausloggen()
        except ValueError:
            print("Keine valide Option")
