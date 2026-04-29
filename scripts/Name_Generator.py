"""
    This script generates n ranom Spanish names with first and last names taking a .txt file 
    generated with copilot with 1000 names and 1000 last names
"""

import csv
import random
buffer = []
nombres = []
apellidos = []
n = 1000
with open('./data/names.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f) # Usa la primera fila como llaves
    for row in reader:
        nombres.append(row['nombre'])
        apellidos.append(row['apellido'])

def generar_persona_aleatoria():
    # 'random.choice' elige un elemento al azar de la lista
    nombre_random = random.choice(nombres)
    
    # 'random.sample' elige 2 elementos distintos de la lista de apellidos
    # Esto evita que alguien se llame "García García" a menos que lo permitas
    apellidos_random = random.sample(apellidos, k=2)
    
    return {
        "nombre": nombre_random,
        "apellido1": apellidos_random[0],
        "apellido2": apellidos_random[1]
    }

# Ejemplo de uso:
open ("./data/nombres_completos.txt", "w").close()  # Limpiar el archivo antes de escribir
with open("./data/nombres_completos.txt", "w") as file:
    for _ in range(n):  
        persona = generar_persona_aleatoria()
        buffer.append(f"{persona['nombre']} {persona['apellido1']} {persona['apellido2']}\n")
    

    file.write(''.join(buffer))