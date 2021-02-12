# Kirjasto, jossa on tietojen järkevyystarkiktukseen soveltuvia funktioita

# 1. Poistetaan tekstistä ylimäääräiset merkit, kuten välilyönnit alusta ja lopusta
# 2. Vaihdetaan vahingossa syötetyt desimaali pilkku (,) desimaalipisteeksi (.)
# 3. Määritellään järkevän arvon alaraja (pienin hyväksytty arvo)
# 4. Määritellään järkevän arvon yläraja (suurin hyväksytty arvo)

def on_jarkeva(syote, alaraja, ylaraja):
    """
    Puhdistaa merkkijonosta ylimääräiset tulostamattomat merkit ja välilyönnit sekä selvittää onko syötetty arvo annettujen raja-arvojen sisällä funktio muuttaa desimaalipilkun desimaalipisteeksi.


    Args:
        syote (string): Näppäimistöltä syötetty arvo
        alaraja (float): Pienin sallittu arvo
        ylaraja (float): Suurin sallittu arvo
    """

    # Poistetaan whitespace merkit merkkijonon alusta
    puhdistettu_syote = syote.lstrip()

    # Poistetaan whitespace merkit merkkijonon lopusta
    puhdistettu_syote = puhdistettu_syote.rstrip()

    # Selvitetään onko merkkijonassa pilkku(,)
    pilkunpaikka = puhdistettu_syote.find(',')

    # Jos pilkku löytyy , korvataan se pisteellä
    if pilkunpaikka != -1:
        korjattu_syote = puhdistettu_syote.replace(',', '.')
    else:
        korjattu_syote = puhdistettu_syote

    # Muutetaan korjattu syöte merkkijonosta liukuluvuksi

    try:
        luku = float(korjattu_syote)
    except:
        print('Syötetyssä tiedossa on ylimääräisiä merkkejä, vain numerot sallittuja')
        luku = 0
    # Tarkistetaan alaraja, ettei syöte ole alarajan alapuolella

    try:
        if luku < alaraja:
            raise Exception('Syöttämäsi arvo on alle sallitun')
    except Exception as virheilmoitus:
            print(virheilmoitus)

    # Tarkistetaan, ettei syöte ole ylärajan yläpuolella
    try:
        if luku > ylaraja:
            raise Exception('Syöttämäsi arvo on yli sallitun')
    except Exception as virheilmoitus:
            print(virheilmoitus)

    # palautetaan luku
    return luku


# testataan toiminta
#tulos = on_jarkeva('sata', 1, 500)
#print(tulos)
