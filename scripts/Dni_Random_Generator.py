"""
    Spanish DNi generator script, it generates n lines of random DNi numbers, they could be real, beacouse
    it takes the same algorithm as real DNI numbers and letters, but are generated completly randomly and 
    it writes them in a text file in stacks of 25% of the total number of 
"""

import random
n = 10000
LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"
buffer = []
 
with open("./data/dnis_espana_completo.txt", "w") as file:
    for i in range(1, n + 1):
        # El formato :08d es clave para los números bajos (ej. 05443221Z)
        num = random.randint (1, 80000000)  # Generar un número aleatorio entre 1 y 80 millones
        dni = f"{num:08d}{LETTERS[num % 23]}\n"
        buffer.append(dni)
        
        # Escribimos en el archivo en 4 tandas para optimizar un poco la velocidad de escritura
        if i % (n // 4) == 0:
            file.writelines(buffer)
            buffer = []
            