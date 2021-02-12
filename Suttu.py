def bmi(paino, pituus):
    """[summary]

    Args:
        paino ([type]): [description]
        pituus ([type]): [description]

    Returns:
        [type]: [description]
    """




    painoindeksi = paino / pituus ** 2
    return painoindeksi 



    
#Testataan
oma_bmi = bmi(88, 1.77)

def rasvaprosentti(bmi, ika, sukupuoli):
    rprosentti = 1.2 * bmi + 0.23 * ika - 10.8 * sukupuoli - 5.4
    return rprosentti

#testataan
oma_rasvaprosentti = rasvaprosentti(oma_bmi, 53, 1)
print("rprosentti", rasvaprosentti(bmi, ika, sukupuoli))
# testasin toimiiko print(oma_rasvaprosentti)

try:
  print(x)
except: 
  print('Something went wrong')
finally:
  print('The try except is finished')