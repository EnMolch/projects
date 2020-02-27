"""
Snack_V3 Opjektorientierter Automat mit Nutzerkonten
"""
import math
PRODUKT_NAMEN = ["Mars", "Molch", "Schrödingers Katze", "Sicke plays", "Pornobalken zum Aufkleben",
                 "Goethes Faust", "Goethes flache Hand", "Waldesel", "P90", "B-rush"]
PRODUKT_PREIS = [1.2, 1.3, 1, 0.5, 3.5, 0.7, 0.6, 4.20, 0.99, 3]
PRODUKT_ANZAHL = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
NUTZER_DATEN = []
PRODUKT_ARRAY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
ADDRESS_OFFSET = 0
PRODUKT_LAGER_HILFE = []
class Produkte:
    """ Klasse Produkte: genutzt zum Generieren der Objekte Produkt,
    sowie setter und getter für Attribute
    """
    def __init__(self, name_prod, preis_prod, anzahl_prod):
        self.name_prod = name_prod
        self.preis_prod = preis_prod
        self.anzahl_prod = anzahl_prod
    def get_lager(self):
        """Getter für Anzahl der Objekte
        Returns:
            [Int] -- [Anzahl eines Produktes]
        """
        return self.anzahl_prod
    def get_kosten(self):
        """[Getter für Preis]
        Returns:
            [float] -- [Preis eines Produktes]
        """
        return self.preis_prod
    def set_lager(self, anzahl_prod):
        """[Setter für Amzahl des Produktes]
        Arguments:
            anzahl_prod {[Int]} -- [Soll - Anzahl des Produktes]
        """
        self.anzahl_prod = anzahl_prod
    def getName(self):
        """[Getter für Namen eines Produktes]
        Returns:
            [string] -- [Name eines Produktes]
        """
        return self.name_prod

class Nutzer:
    """[Klasse zum Generieren von Nutzern]
    """
    def __init__(self, Bname_Nutz, Pw, Konto=0):
        self.Bname_Nutz = Bname_Nutz
        self.Pw = Pw
        self.Konto = Konto
        self.Logged_In = False

    def Set_Konto(self, Konto):
        self.Konto = Konto

    def Get_Konto(self):
        return self.Konto

    def Einloggen(self):
        for i in NUTZER_DATEN:
            if str(i) == self.Bname_Nutz:
                if NUTZER_DATEN[NUTZER_DATEN.index(i)+1] == self.Pw:
                    self.Logged_In = 1
                    self.Konto = NUTZER_DATEN[NUTZER_DATEN.index(self.Bname_Nutz)+2]
                    return
                else:
                    print("inkorrektes Passwort, absolute Frechheit.")
                    return
        print("error, der Nutzer konnte nicht gefunden werden")
        return
    def Registrieren(self):
        for i in NUTZER_DATEN:
            if i == self.Bname_Nutz:
                print("Fehler, der Nutzer existiert bereits")
                return
            else:
                pass
        try:
            NUTZER_DATEN.append(self.Bname_Nutz)
            NUTZER_DATEN.append(self.Pw)
            NUTZER_DATEN.append(self.Konto)
            print(NUTZER_DATEN)
            self.Logged_In = 1
        except ValueError:
            print("das Passwort ist invalide")

    def Ausloggen(self):

        self.Logged_In = 0
        NUTZER_DATEN[NUTZER_DATEN.index(self.Bname_Nutz)+2] = self.Konto
        File_Handle = open("save.txt", "w")
        for i in range(len(NUTZER_DATEN)):
            if i != 0:
                File_Handle.write(",")
            File_Handle.write(str(NUTZER_DATEN[i]))
        File_Handle.write(",")
        File_Handle.write("\n")
        for i in range(len(PRODUKT_LAGER_HILFE)):
            if i != 0:
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
    def Kaufen(self, name_prod, preis_prod, Stonks, ID):
        if Stonks > 0:
            Kontostand = float(ID.Get_Konto())
            print(Kontostand)
            if preis_prod < Kontostand:
                ID.Set_Konto(Kontostand - preis_prod)
                print(f"viel spass mit {name_prod}")
                PRODUKT_ANZAHL[PRODUKT_NAMEN.index(name_prod)] = int(PRODUKT_ANZAHL[PRODUKT_NAMEN.index(name_prod)]) -1
                PRODUKT_LAGER_HILFE[PRODUKT_NAMEN.index(name_prod)+ADDRESS_OFFSET] = int(PRODUKT_LAGER_HILFE[PRODUKT_NAMEN.index(name_prod)+ADDRESS_OFFSET]) -1
            else:
                print("Sieh den Monopolkapitalist, der dich mit Haut und Haaren frist!")
    def Produkt_Init(self):
        for i in range(len(PRODUKT_NAMEN)):
            PRODUKT_ARRAY[i] = Produkte(PRODUKT_NAMEN[i], PRODUKT_PREIS[i], PRODUKT_ANZAHL[i])



if __name__ == "__main__":
    while 1:
        Bname_In = str(input("Username: "))
        Pw_In = str(input("Passwort: "))
        File_Handle = open("save.txt", "r")
        NUTZER_DATEN = []
        NUTZER_DATEN.extend(File_Handle.readline().split(","))
        NUTZER_DATEN.pop()
        print(NUTZER_DATEN)

        PRODUKT_LAGER_HILFE = []
        PRODUKT_ANZAHL = []
        PRODUKT_LAGER_HILFE.extend(File_Handle.readline().split(","))
        ADDRESS_OFFSET = (math.floor(float(NUTZER_DATEN.index(Bname_In))/3))*10
        for i in range(10):
            PRODUKT_ANZAHL.extend(PRODUKT_LAGER_HILFE[i+ADDRESS_OFFSET])
        print(PRODUKT_ANZAHL)

        File_Handle.close()

        try:
            Reg_Einlog = int(input("Einloggen [0]   Registrieren[1]  "))
            print(Reg_Einlog)
            User_Identity = Nutzer(Bname_In, Pw_In)            #Fallunterscheidung in Neu oder Alt

            if Reg_Einlog > 0:
                User_Identity.Registrieren()
                Automat_Instanz = Snacc()

            else:
                User_Identity.Einloggen()
                Automat_Instanz = Snacc()

            while User_Identity.Logged_In:
                Automat_Instanz.Produkt_Init()
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
                        print(PRODUKT_ARRAY[i].getName(), "  ", PRODUKT_ARRAY[i].get_kosten(), "  ",PRODUKT_ARRAY[i].getLager())
                    Name_Buy = str(input("Bitte den Namen des gewünschten Produktes eingeben: "))

                    if Name_Buy in PRODUKT_NAMEN:
                        Temp_Index = PRODUKT_NAMEN.index(Name_Buy)
                        Temp_Preise = PRODUKT_PREIS[Temp_Index]
                        Temp_Anzahl = int(PRODUKT_ANZAHL[Temp_Index])
                        Automat_Instanz.Kaufen(Name_Buy, Temp_Preise, Temp_Anzahl, User_Identity)

                    else:
                        print("Bitte korrekten Produktnamen eingeben")

                elif Input_Cache == "3":
                    User_Identity.Ausloggen()
        except ValueError:
            print("Keine valide Option")
