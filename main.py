class TM:
    def __init__(self, paska, prazdny_symbol='#'):
        self.paska = paska  # Vstupní páska
        self.prazdny_symbol = prazdny_symbol  # Prázdný symbol
        self.pozice_hlavy = self.najdi_prvni_neprazdny()  # Nastavíme hlavu na první nepraždný symbol
        self.stav = '0000'  # Počáteční stav je 'start'
        self.symbol_na_binarni = {
            '0': '0010',
            '1': '0001',
            '#': '0000',
            'a': '0011',
            'b': '0100',
            ' ': '0101',
            '+': '0110',
            'd': '0111',
            'e': '1000',
            'f': '1001'
        }

    def najdi_prvni_neprazdny(self):
        # Najde první neprazdný symbol na pásce
        for index, symbol in enumerate(self.paska):
            if symbol in '01':
                return index
        return 0

    def zmena_stavu(self):
        aktualni_symbol = self.paska[self.pozice_hlavy] if self.pozice_hlavy < len(self.paska) else self.prazdny_symbol

        # Vytiskne aktuální krok pásky
        print(f"Stav: {self.stav}), Pozice hlavy: {self.pozice_hlavy}, Symbol: {aktualni_symbol} (Binárně: {self.symbol_na_binarni.get(aktualni_symbol, 'N/A')})")

        # Mapování stavů na funkce pro přechody
        stavy_prechody = {
            '0000': self.stav_0000,
            '0001': self.stav_0001,
            '0010': self.stav_0010,
            '0011': self.stav_0011,
            '0100': self.stav_0100,
            '0101': self.stav_0101,
            '0110': self.stav_0110,
            '1000': self.stav_1000,
            '1001': self.stav_1001,
            '1011': self.stav_1011,
            '1100': self.stav_1100,
            '1101': self.stav_1101,
            '1111': self.stav_1111,
            '1110': self.stav_1110,
            '1010': self.stav_1010,
            '0111': self.stav_0111
        }

        # Zavolání metody pro aktuální stav
        if self.stav in stavy_prechody:
            return stavy_prechody[self.stav](aktualni_symbol)

        return False  # Pokračuj ve vykonávání

    def stav_0000(self, aktualni_symbol):
        if aktualni_symbol in '01':
            self.posun_hlavu('L')
        elif aktualni_symbol == '#':
            self.zapis_symbol('a')
            self.prechod('0001', 'R')

    def stav_0001(self, aktualni_symbol):
        if aktualni_symbol in '01':
            self.posun_hlavu('R')
        elif aktualni_symbol == '#':
            self.prechod('0010', 'R')

    def stav_0010(self, aktualni_symbol):
        if aktualni_symbol in '01':
            self.prechod('0001', 'R')
        elif aktualni_symbol == '#':
            self.zapis_symbol('b')
            self.prechod('0011', 'L')

    def stav_0011(self, aktualni_symbol):
        if aktualni_symbol in '01#':
            self.posun_hlavu('L')
        elif aktualni_symbol == 'a':
            self.prechod('0100', 'R')

    def stav_0100(self, aktualni_symbol):
        if aktualni_symbol in '01':
            self.posun_hlavu('R')
        elif aktualni_symbol == '#':
            self.zapis_symbol('+')
            self.prechod('0101', 'R')
        elif aktualni_symbol == ' ':
            self.posun_hlavu('R')

    def stav_0101(self, aktualni_symbol):
        if aktualni_symbol == '#':
            self.prechod('0110', 'L')
        elif aktualni_symbol in '01':
            self.posun_hlavu('R')
        elif aktualni_symbol == 'b':
            self.prechod('0111', 'R')

    def stav_0110(self, aktualni_symbol):
        if aktualni_symbol == '1':
            self.zapis_symbol('d')
            self.prechod('1000', 'L')
        elif aktualni_symbol == '0':
            self.zapis_symbol('d')
            self.prechod('1001', 'L')
        elif aktualni_symbol == '+':
            self.zapis_symbol(' ')
            self.prechod('1010', 'L')

    def stav_1000(self, aktualni_symbol):
        if aktualni_symbol in '01':
            self.posun_hlavu('L')
        elif aktualni_symbol == '+':
            self.prechod('1011', 'L')

    def stav_1001(self, aktualni_symbol):
        if aktualni_symbol in '01':
            self.posun_hlavu('L')
        elif aktualni_symbol == '+':
            self.prechod('1100', 'L')

    def stav_1011(self, aktualni_symbol):
        if aktualni_symbol == '0' or aktualni_symbol == '#':
            self.zapis_symbol('e')
            self.prechod('1101', 'R')
        elif aktualni_symbol == '1':
            self.zapis_symbol('f')
            self.prechod('1110', 'L')
        elif aktualni_symbol in 'ef':
            self.posun_hlavu('L')
        elif aktualni_symbol == ' ':
            self.posun_hlavu('L')

    def stav_1100(self, aktualni_symbol):
        if aktualni_symbol == '0':
            self.zapis_symbol('f')
            self.prechod('1111', 'R')
        elif aktualni_symbol == '1':
            self.zapis_symbol('e')
            self.prechod('1111', 'R')
        elif aktualni_symbol in 'ef':
            self.posun_hlavu('L')
        elif aktualni_symbol == ' ':
            self.posun_hlavu('L')

    def stav_1101(self, aktualni_symbol):
        if aktualni_symbol in '01ef+ ':
            self.posun_hlavu('R')
        elif aktualni_symbol == 'd':
            self.zapis_symbol(' ')
            self.prechod('0110', 'L')

    def stav_1111(self, aktualni_symbol):
        if aktualni_symbol in '01ef+ ':
            self.posun_hlavu('R')
        elif aktualni_symbol == 'd':
            self.zapis_symbol(' ')
            self.prechod('0110', 'L')

    def stav_1110(self, aktualni_symbol):
        if aktualni_symbol == '0' or aktualni_symbol == 'a':
            self.zapis_symbol('1')
            self.prechod('1101', 'R')
        elif aktualni_symbol == '1':
            self.zapis_symbol('0')
            self.posun_hlavu('L')

    def stav_1010(self, aktualni_symbol):
        if aktualni_symbol == 'e':
            self.zapis_symbol('1')
            self.posun_hlavu('L')
        elif aktualni_symbol == 'f':
            self.zapis_symbol('0')
            self.posun_hlavu('L')
        elif aktualni_symbol == 'a':
            self.prechod('0100', 'R')
        elif aktualni_symbol in '01':
            self.posun_hlavu('L')
        elif aktualni_symbol == ' ':
            self.posun_hlavu('L')
        elif aktualni_symbol == '#':
            self.zapis_symbol('a')
            self.prechod('0100', 'R')

    def stav_0111(self, aktualni_symbol):
        print("Turinguv stroj dokončil výpočet.")
        return True

    def zapis_symbol(self, symbol):
        if self.pozice_hlavy >= len(self.paska):
            self.paska.append(self.prazdny_symbol)
        self.paska[self.pozice_hlavy] = symbol

    def posun_hlavu(self, smer):
        if smer == 'R':
            self.pozice_hlavy += 1
            if self.pozice_hlavy >= len(self.paska):
                self.paska.append(self.prazdny_symbol)
        elif smer == 'L':
            self.pozice_hlavy = max(0, self.pozice_hlavy - 1)

    def prechod(self, novy_stav, smer):
        self.stav = novy_stav
        self.posun_hlavu(smer)

    def zakoduj_pasku(self, paska):
        # Trim leading and trailing '#' symbols and whitespace
        paska = paska.strip('#').strip()

        # If the tape is empty after trimming, return empty string
        if not paska:
            return ''

        kodovana_paska = ''
        for symbol in paska:
            if symbol in self.symbol_na_binarni:
                kodovana_paska += self.symbol_na_binarni[symbol] + ' '
            else:
                kodovana_paska += 'N/A '
        return kodovana_paska.strip()

    def spust(self):
        krok = 0
        while True:
            # Remove consecutive '#' symbols for cleaner output
            aktualni_paska = ''.join(self.paska).strip('#')
            if aktualni_paska:
                print(f"Krok {krok}: {aktualni_paska} (Hlava na {self.pozice_hlavy}, Stav {self.stav})")
            else:
                print(f"Krok {krok}: # (Hlava na {self.pozice_hlavy}, Stav {self.stav})")

            zastaveno = self.zmena_stavu()
            krok += 1
            if zastaveno:
                break
        return ''.join(self.paska)


# Hlavní smyčka
while True:
    vstup_paska = list(input("Zadejte vstup: "))
    paska = ['#'] * 1000
    start_pos = (1000 - len(vstup_paska)) // 2
    paska[start_pos:start_pos + len(vstup_paska)] = vstup_paska
    TM = TM(paska)
    konecna_paska = TM.spust()
    print("\nVýsledky:")
    print("Konečná páska (symboly):", konecna_paska)
    print("Konečná páska (binárně):", TM.zakoduj_pasku(konecna_paska))