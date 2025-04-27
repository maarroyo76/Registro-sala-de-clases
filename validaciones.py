def validar_rut(rut):
    rut = rut.replace('-', '').replace('.', '').upper()
    if not rut[:-1].isdigit():
        return False
    
    cuerpo, dv = rut[:-1], rut[-1]
    if dv not in '0123456789K':
        return False
    
    # Cálculo del dígito verificador esperado
    suma = 0
    multiplo = 2
    for c in reversed(cuerpo):
        suma += int(c) * multiplo
        multiplo = multiplo + 1 if multiplo < 7 else 2
    
    calculado = 11 - (suma % 11)
    if calculado == 11:
        calculado = '0'
    elif calculado == 10:
        calculado = 'K'
    else:
        calculado = str(calculado)
    
    return calculado == dv

def validar_nota(nota: float) -> bool:
    return 1.0 <= nota <= 7.0