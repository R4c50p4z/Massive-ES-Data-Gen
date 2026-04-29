"""
    Spanish DNi generator script, it generates n lines of random DNi numbers, they could be real, beacouse
    it takes the same algorithm as real DNI numbers and letters, in order (from 1 to n) but are generated 
"""
n = 80000000
LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

def generar_censo_completo(limite_superior):
    print(f"Iniciando generación de {limite_superior} DNIs...")
    
    with open("./data/dnis_espana_completo.txt", "w") as file:
        buffer = []
        for i in range(1, limite_superior + 1):
            # El formato :08d es clave para los números bajos (ej. 05443221Z)
            num = f"{i:08d}"
            dni = f"{num}{LETTERS[int(num) % 23]}\n"
            buffer.append(dni)
            
            # Escribimos cada millón para ir rápido pero seguro
            if i % 1000000 == 0:
                file.writelines(buffer)
                buffer = []
                print(f"Progreso: {i // 1000000}M / {limite_superior // 1000000}M")
        
        if buffer:
            file.writelines(buffer)

generar_censo_completo(n)  # Generar hasta el DNI número 80 millones (aprox. población espanola)