# Otetaan käyttöön muduulin sanitetti.py toiminnot
import saniteetti

# Funktio painoindeksin (body mass index) laskemiseksi
def bmi(paino, pituus):
    painoindeksi = paino / pituus**2
    return painoindeksi

# Funktio kehon rasvaprosentin laskemiseksi


def rasvaprosentti(bmi, ika, sukupuoli):
    rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    return rprosentti


# Kysytään käyttäjältä tarvittavat tiedot
paino_str = input("Anna painosi kilogrammoina: ")
paino = saniteetti.on_jarkeva(paino_str, 20 200)
pituus_str = input("Anna pituutesi metreinä: ")
pituus_str = saniteetti.on_jarkeva(1, 3)
ika_str = input("Kuinka vanha olet?: ")
ika_str = saniteetti.on_jarkeva(20, 100)
sukupuoli_str = input("Paina 1, jos olet mies, 0 jos olet nainen: ")

# Merkkijonot luvuiksi
tapahtui_virhe = False

try:
    if paino_str.isalpha()():
        raise TypeError('Vain numerot 0-9 ja desimaali piste ovat sallittuja')

    # jos ei virhettä, muutetaan liukuluvuksi
    paino = float(paino_str)

    # jos tapahtui virhe tulostetaan virheilmoitus teksti ja asetetaan virhemuuttujan arvoksi True

except Exception as virhe:
    print(virhe)
    tapahtui_virhe = True

# TODO: tee tyyppitarkistusrutiinit kaikille muuttujille

try:
    pituus = float(pituus_str)

    # jos tapahtui virhe tulostetaan virheilmoitus teksti ja asetetaan virhemuuttujan arvoksi True
    pituus = float(pituus_str)
except:
    print('Pituus virheellinen')
    tapahtui_virhe = True

try:
    ika = float(ika_str)

except:
    print('Ikä virheellinen')
    tapahtui_virhe = True

try:
    sukupuoli = float(sukupuoli_str)

except:
    print('Sukupuoli virheellinen, syötä vain 0 tai 1')
    tapahtui_virhe = True

if tapahtui_virhe == False:
    painoindeksi = bmi(paino, pituus)
    print('Painoindeksisi on:', painoindeksi)
    rprosentti = rasvaprosentti(painoindeksi, ika, sukupuoli)
    print('Kehosi rasvaprosentti on:', rprosentti)

else:
    print('Ei voitu laske, koska syöttötiedoissa oli virhe')
