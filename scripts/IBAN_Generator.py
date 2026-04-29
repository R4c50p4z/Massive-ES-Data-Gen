"""
    This is the most \"complex\" script of the project, it generates n randoms Spanish IBAN codes using the 
    same algorithm as real IBAN codes, but the data is generated randomly at least the entity is real,
    but the bann office and account number are generated randomly, the DC is calculated with the 
    algorithm previously explained
"""

import random
n = 1000
BANK_ENTITY = ("2080", "0061", "0182", "0234", "0240", "0081", "0186", "0049", "0128", "2100", "2045", "3035", "3058", "2000", "1474", "0019", "0239", "2085", "1465", "2095", "2103", "0011", "0241", "0220", "0235", "1490", "1491", "1508", "8832", "8833", "8843")
PESO = (6, 3, 7, 9, 10, 5, 8, 4, 2, 1)

def calc_dc(bankEntity, bankOffice, accountNumber):
    # DC 1: Entidad y Oficina (Se anaden dos ceros al principio por norma)
    eo_con_ceros = "00" + bankEntity + bankOffice
    sumEO = sum(int(eo_con_ceros[i]) * PESO[i] for i in range(10))
    resEO = 11 - (sumEO % 11)
    resEO = 0 if resEO == 11 else (1 if resEO == 10 else resEO)

    # DC 2: Cuenta
    sumAN = sum(int(accountNumber[i]) * PESO[i] for i in range(10))
    resAN = 11 - (sumAN % 11)
    resAN = 0 if resAN == 11 else (1 if resAN == 10 else resAN)
    
    return f"{resEO}{resAN}"

def calc_iban_control(completo_sin_es):
    # Módulo 97 para los dos dígitos tras el "ES"
    # ES = 1428 en código ISO
    paso1 = completo_sin_es + "142800"
    control = 98 - (int(paso1) % 97)
    return f"{control:02d}"

ibans = set() # Usar set es más rápido que una lista para evitar duplicados

while len(ibans) < n:
    entidad = random.choice(BANK_ENTITY)
    oficina = f"{random.randint(0, 9999):04d}"
    cuenta = f"{random.randint(0, 9999999999):010d}"
    
    dc_cuenta = calc_dc(entidad, oficina, cuenta)
    
    # El CCC (Código Cuenta Cliente) es: Entidad + Oficina + DC + Cuenta
    ccc = f"{entidad}{oficina}{dc_cuenta}{cuenta}"
    
    # Calculamos el control del IBAN (el que va después de ES)
    dc_iban = calc_iban_control(ccc)
    
    iban_final = f"ES{dc_iban}{ccc}\n"
    ibans.add(iban_final)

with open("./data/ibans_espana.txt", "w") as file:
    file.writelines(sorted(list(ibans)))