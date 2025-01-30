# Turingův stroj pro sčítání binárních čísel

Tento projekt implementuje Turingův stroj v jazyce Python, který provádí sčítání dvou binárních čísel oddělených mezerou. Simulátor zahrnuje dynamickou správu pásky, definované přechody mezi stavy, binární kódování symbolů a protokolování průběhu výpočtu.

## Vlastnosti

*   **Dynamická správa pásky:** Páska se automaticky rozšiřuje podle potřeby a je inicializována prázdnými symboly `#`.
*   **Definované přechody mezi stavy:** Implementováno 16 unikátních stavů (0000 až 1111) s explicitními pravidly přechodu pro každý stav a symbol.
*   **Binární kódování:** Symboly (0, 1, a, b, +, mezera, d, e, f) jsou mapovány na 4bitovou binární reprezentaci pro interní zpracování.
*   **Protokolování provádění:** V každém kroku výpočtu se vypisuje aktuální stav pásky, pozice hlavy a aktuální stav Turingova stroje.
*   **Zpracování vstupů:** Program přijímá vstupní řetězec od uživatele a umisťuje ho doprostřed předem alokované pásky pro simulaci.

## Požadavky a instalace

*   Python 3.12 (doporučeno)
*   PyCharm 2024.2.3 (nebo jiné IDE s podporou Python 3.12)

## Spuštění

1.  **Klonování repozitáře (doporučeno):** `git clone https://github.com/Koscziej90/TM`
2.  **Vložení kódu:** Vložte kód do souboru s příponou `.py` (např. `turing_machine.py`).

Spusťte skript z příkazové řádky pomocí `python turing_machine.py`. Program vyzve k zadání vstupního řetězce. Po zadání vstupu se spustí simulace a v konzoli se zobrazí kroky výpočtu, včetně konečné podoby pásky a její binární reprezentace.

## Vstupní formát

*   Délka pásky je předem alokována na 1000 symbolů. Prázdná místa jsou vyplněna symbolem `#`.
*   Platné vstupní symboly: 0, 1, +, a, b, d, e, f a mezera.

## Struktura kódu

**Třída `TM`**

*   `__init__(self, paska, prazdny_symbol='#')`: Inicializuje Turingův stroj s danou páskou, prázdným symbolem, pozicí hlavy a počátečním stavem.
    *   `paska`: Vstupní páska (seznam symbolů).
    *   `prazdny_symbol`: Prázdný symbol (defaultně `#`).
    *   `pozice_hlavy`: Pozice hlavy na pásce.
    *   `stav`: Aktuální stav Turingova stroje.
    *   `symbol_na_binarni`: Slovník pro mapování symbolů na jejich 4-bitové binární kódy.

*   **Metody:**
    *   `najdi_prvni_neprazdny()`: Najde index prvního neprázdného symbolu (0 nebo 1) na pásce.
    *   `zmena_stavu()`: Řídí přechody mezi stavy na základě aktuálního symbolu pod hlavou a aktuálního stavu.
    *   `spust()`: Spouští výpočet Turingova stroje, dokud se nedosáhne koncového stavu (0111).
    *   `zakoduj_pasku()`: Převádí obsah pásky na řetězec s binární reprezentací symbolů.
    *   `stav_XXXX(self, aktualni_symbol)` (např. `stav_0000`, `stav_0001`...): Implementují logiku pro jednotlivé stavy, včetně přechodů, zápisu symbolů a posunu hlavy.

## Příklad výpočtu

**Počáteční stav pásky:**

`...#110#101#...`

Hlava se nachází na prvním symbolu '1' a stroj je v počátečním stavu '0000'.

**Kroky výpočtu:**

1.  Hlava se posouvá doleva, dokud nenarazí na první symbol '#'.
2.  Symbol '#' je nahrazen symbolem 'a' a stroj přechází do stavu '0001'.
3.  Hlava se posouvá doprava přes symboly '1', '1', '0', dokud nenarazí na další symbol '#'.
4.  Druhý symbol '#' je nahrazen symbolem 'b' a stroj přechází do stavu '0011'.
5.  Hlava se posouvá doleva, dokud nenarazí na symbol 'a'.
6.  Stroj přechází do stavu '0100'.
7.  Hlava se posouvá doprava a za prvním symbolem '#' vkládá symbol '+'.
8.  Hlava se posouvá doprava, dokud nenarazí na druhý symbol '#'.
9.  Stroj přechází do fáze binárního výpočtu.
10. Během této fáze jsou symboly '0' a '1' nahrazovány symboly 'd', 'e' a 'f' v souladu s pravidly pro sčítání binárních čísel.
11. Výsledná páska je transformována zpět do čitelné podoby.
12. Stroj dosáhne koncového stavu '0111' a výpočet je dokončen.

## Licence

Open-source (bez specifikace konkrétní licence).
