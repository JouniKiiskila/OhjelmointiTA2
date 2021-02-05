def ympyran_ala(halkaisija):
    """Funktio laskee ympyränpinta-alan halkaisijan perusteella
       args:
       halkaisija (float): ympyrän halkaisija
    Returns:
        float: ympyrän pinta-ala
        
    """

    sade = halkaisija / 2
    pinta_ala = sade ** 2 * 3.14159
    return pinta_ala

kayttaja = 'Markku'
kaupungit =['Raisio'], ['Turku'], ['Lieto'], ['Kaarina']
print('Metrisen ympyran halkaisija on =', ympyran_ala(1))
