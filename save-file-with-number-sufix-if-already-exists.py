import os

def guarda_fitxer(directori, nom_fitxer, contingut):
    """
    Guarda un fitxer al directori especificat. Si ja existeix un fitxer amb el mateix nom,
    afegeix un sufix (_1, _2, ...) al nom del fitxer.

    :param directori: Ruta del directori on guardar el fitxer
    :param nom_fitxer: Nom del fitxer
    :param contingut: Contingut del fitxer
    """
    if not os.path.exists(directori):
        os.makedirs(directori)
    
    ruta_fitxer = os.path.join(directori, nom_fitxer)
    base, extensio = os.path.splitext(ruta_fitxer)
    
    comptador = 1
    while os.path.exists(ruta_fitxer):
        ruta_fitxer = f"{base}_{comptador}{extensio}"
        comptador += 1

    with open(ruta_fitxer, 'w') as fitxer:
        fitxer.write(contingut)
    
    print(f"Fitxer guardat com: {ruta_fitxer}")

# Exemple d'ús
directori = 'la_meva_carpeta'
nom_fitxer = 'el_meu_fitxer.txt'
contingut = 'Aquest és el contingut del fitxer.'

guarda_fitxer(directori, nom_fitxer, contingut)