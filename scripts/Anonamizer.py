"""
    This script generates a CSV file with n randomly combined names with first and last names, a Spanish DNI,
    and a Spanish IBAN code the data is taken from other generated files in the same scripts folder,
    if the data generated is casually real, it is only for testing purposes and should not be used for
    any other reason, the data is generated randomly and may not correspond to real people or real data, 
    it is only for testing purposes and should not be used for any other reason, the only real data is DNI
    beacouse it is generated with the same algorithm as real DNIs, and the entity of IBAN is also real, 
    but the rest of the data is completely random and should not be used for any other reason than testing
    THE DATA GENERATED IN THIS SCRIPT IS COMPLETLY RANDOM
"""

import random 
buffer = []
n = 100
open ("./data/final_data/anonamizados.csv", "w").close()  # Limpiar el archivo antes de escribir
with open("./data/final_data/anonamizados.csv", "w") as file:

    with open("nombres.txt") as f:
        nombres = f.read().splitlines() # Leer una sola vez
    with open("./data/dnis_espana_completo.txt") as f:
        dnis = f.read().splitlines() # Leer una sola vez
    with open("./data/ibans_espana.txt") as f:
        ibans = f.read().splitlines() # Leer una sola vez
    for _ in range(n):
        nElegido = random.choice(nombres)
        dniElegido = random.choice(dnis)
        ibanElegido = random.choice(ibans)

        buffer.append(f"{nElegido},{dniElegido},{ibanElegido}\n")

    file.writelines(buffer)
