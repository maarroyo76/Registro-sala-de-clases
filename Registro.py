
lista_alumnos = ['Lucas', 'Juan', 'Pedro']
notas_alumnos = [[7, 6.9, 5.8], [6.3, 4.7, 5.5], [4, 3.7, 1.9]]
id_alumnos = [000000000, 111111111, 222222222]

def ingresar_notas(notas_alumnos, numero_alumno):
    alumno = numero_alumno -1
    while True:
        try:
            print('Ingrese las notas del Alumno de una en una')
            print('(Ejemplo: 5 , 6.7,  4.1)')
            nota1 = float(input('Ingrese la primera nota: '))
            nota2 = float(input('Ingrese la segunda nota: '))
            nota3 = float(input('Ingrese la tercera nota: '))
        except ValueError:
            print('Valores inválidos. Intente otra vez.')
            continue
        if 1 <= nota1 <= 7 and 1 <= nota2 <= 7 and 1 <= nota3 <= 7:
            break
        else:
            print('Valores inválidos. Intente otra vez.')
    notas_alumnos[alumno] = [nota1, nota2, nota3]   
    print('Notas actualizadas exitosamente')

def eliminar(lista_alumnos, notas_alumnos, id_alumnos, numero_alumno):
    alumno = numero_alumno - 1  
    lista_alumnos.pop(alumno)  
    notas_alumnos.pop(alumno)  
    id_alumnos.pop(alumno)  
    print('¡Alumno eliminado con éxito!')

def calcular_promedio(notas_alumnos, numero_alumno):
    alumno = numero_alumno -1
    promedio = sum(notas_alumnos[alumno])
    promedio = sum(notas_alumnos[alumno]) / len(notas_alumnos[alumno])
    promedio = round(promedio,1)
    print(f"El promedio de {lista_alumnos[alumno]} es: {promedio}")
    print(f"Las notas del alumno son {notas_alumnos[alumno]}")

def imprimir_nombres(lista_alumnos):
    for p, nombre in enumerate(lista_alumnos):
        print(f"{p+1} - {nombre}")

def buscar_alumno(lista_alumnos, alumno):
    for nombre in lista_alumnos:
        if nombre == alumno:
            return True
    return False

def nuevo_alumno():
    while True:
        print('Ingrese el nombre del nuevo alumno')
        alumno = input('>>')
        if buscar_alumno(lista_alumnos, alumno):
            print('Alumno ya ingresado, Intente otra vez')
        else:
            break
    while True:
        try:
            print('Ingrese el RUT del alumno (sin puntos ni guión)')
            run_alumno = int(input('>>'))
            if len(str(run_alumno)) > 7 and len(str(run_alumno)) < 10:
                break
            else :
                print('Run Invalido intente otra vez')
        except ValueError:
            print('Run invalido')
    while True:
        try:
            print('Ingrese las notas del Alumno de una en una')
            print('(Ejemplo: 5 , 6.7,  4.1)')
            nota1 = float(input('Ingrese la primera nota: '))
            nota2 = float(input('Ingrese la segunda nota: '))
            nota3 = float(input('Ingrese la tercera nota: '))
        except ValueError:
            print('Valores inválidos. Intente otra vez.')
            continue
        if 1 <= nota1 <= 7 and 1 <= nota2 <= 7 and 1 <= nota3 <= 7:
            break
        else:
            print('Valores inválidos. Intente otra vez.')

    lista_alumnos.append(alumno)
    notas_alumnos.append([nota1, nota2, nota3])
    id_alumnos.append(run_alumno)
    print('Alumno agregado exitosamente!')

def promedio_alumno():
    imprimir_nombres(lista_alumnos)
    while True:
        try:
            numero_alumno = int(input('Seleccione un alumno: '))
            if numero_alumno <= 0 or numero_alumno > len(lista_alumnos):
                print('Opcion Invalida, Intente otra vez')
            else:
                calcular_promedio(notas_alumnos, numero_alumno)
                break
        except ValueError:
            print('Opcion Invalida, Intente otra vez')

def borrar_alumno():
    imprimir_nombres(lista_alumnos)
    while True:
        try:
            numero_alumno = int(input('Seleccione un alumno: '))
            if numero_alumno <= 0 or numero_alumno > len(lista_alumnos):
                print('Opcion Invalida, Intente otra vez')
            else:
                eliminar(lista_alumnos, notas_alumnos, id_alumnos, numero_alumno)
                break
        except ValueError:
            print('Opcion Invalida, Intente otra vez')

def actualizar_notas():
    imprimir_nombres(lista_alumnos)
    while True:
        try:
            numero_alumno = int(input('Seleccione un alumno: '))
            if numero_alumno <= 0 or numero_alumno > len(lista_alumnos):
                print('Opcion Invalida, Intente otra vez')
            else:
                ingresar_notas(notas_alumnos, numero_alumno)
                print('Notas actualizadas exitosamente')
                break
        except ValueError:
            print('Opcion Invalida, Intente otra vez')

def listar_alumnos():
    for p, nombre in enumerate(lista_alumnos):
        promedio = sum(notas_alumnos[p]) / len(notas_alumnos[p])
        promedio = round(promedio, 1)
        print(f"{p+1} - {nombre} - Notas: {notas_alumnos[p]} - Promedio: {promedio}")

def mostrar_repitentes():
    repitentes = []
    for p, nombre in enumerate(lista_alumnos):
        promedio = sum(notas_alumnos[p]) / len(notas_alumnos[p])
        promedio = round(promedio, 1)
        if promedio < 4:
            repitentes.append(f"{p+1} - {nombre} - Notas: {notas_alumnos[p]} - Promedio: {promedio}")
    if repitentes:
        for repitente in repitentes:
            print(repitente)
    else:
        print('No hay alumnos repitentes')

def mostrar_aprobados():
    aprobados = []
    for p, nombre in enumerate(lista_alumnos):
        promedio = sum(notas_alumnos[p]) / len(notas_alumnos[p])
        promedio = round(promedio, 1)
        if promedio >= 4:
            aprobados.append(f"{p+1} - {nombre} - Notas: {notas_alumnos[p]} - Promedio: {promedio}")
    if aprobados:
        for aprobado in aprobados:
            print(aprobado)
    else:
        print('No hay alumnos aprobados')

def exportar_txt():
    with open('Registro Alumnos.txt', "w") as archivo:
        for p, nombre in enumerate(lista_alumnos):
            promedio = sum(notas_alumnos[p]) / len(notas_alumnos[p])
            promedio = round(promedio, 1)
            archivo.write(f"{p+1} - {nombre} - Notas: {notas_alumnos[p]} - Promedio: {promedio}\n")
        print("Registro exportado exitosamente como 'Registro Alumnos.txt'")

def menu():
    print('***** Menu *****')
    print('[1] Nuevo alumno')
    print('[2] Calcular promedio alumno')
    print('[3] Eliminar Alumno')
    print('[4] Actualizar Notas')
    print('[5] Listar alumnos')
    print('[6] Ver alumnos reprobados')
    print('[7] Ver alumnos aprobados')
    print('[8] Exportar registro a txt')
    print('[9] Salir')
    print('****************')

def ejecutar_programa():
    while True:
        try:
            menu()
            opc = int(input('>>'))
            if opc == 1:
                nuevo_alumno()
            elif opc == 2:
                promedio_alumno()
            elif opc == 3:
                borrar_alumno()
            elif opc == 4:
                actualizar_notas()
            elif opc == 5:
                listar_alumnos()
            elif opc == 6:
                mostrar_repitentes()
            elif opc == 7:
                mostrar_aprobados()
            elif opc == 8:
                exportar_txt()
            elif opc == 9:
                print('Hasta luego!')
                break
        except ValueError:
            print('Opcion Invalida, Intente otra vez')

ejecutar_programa()
