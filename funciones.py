# menu_operaciones.py
from typing import List, Optional
from dataclasses import asdict
from colorama import init, Fore, Back, Style
from alumno import Alumno
from persistencia import guardar_alumnos
from validaciones import validar_rut, validar_nota
import os

init(autoreset=True)

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_menu_principal():
    """Muestra el menú principal con todas las opciones disponibles"""
    limpiar_pantalla()
    print(Fore.YELLOW + "\n" + "="*50)
    print(Fore.CYAN + Back.BLUE + " SISTEMA DE GESTIÓN DE ALUMNOS ".center(50))
    print(Fore.YELLOW + "="*50)
    print(Fore.GREEN + "\n1. Agregar nuevo alumno")
    print(Fore.GREEN + "2. Buscar alumno por RUT")
    print(Fore.GREEN + "3. Agregar nota a alumno")
    print(Fore.GREEN + "4. Mostrar todos los alumnos")
    print(Fore.GREEN + "5. Mostrar alumnos aprobados")
    print(Fore.GREEN + "6. Mostrar alumnos reprobados")
    print(Fore.GREEN + "7. Mostrar alumnos ordenados por promedio")
    print(Fore.GREEN + "8. Buscar alumnos por nombre")
    print(Fore.GREEN + "9. Editar información de alumno")
    print(Fore.GREEN + "10. Eliminar alumno")
    print(Fore.GREEN + "11. Generar estadísticas del curso")
    print(Fore.GREEN + "12. Generar reporte detallado")
    print(Fore.RED + "0. Salir del programa")
    print(Fore.YELLOW + "\n" + "="*50)

def mostrar_error(mensaje: str):
    """Muestra un mensaje de error con formato"""
    print(Fore.RED + f"\n[!] ERROR: {mensaje}")

def mostrar_exito(mensaje: str):
    """Muestra un mensaje de éxito con formato"""
    print(Fore.GREEN + f"\n[✓] {mensaje}")

def mostrar_alerta(mensaje: str):
    """Muestra un mensaje de alerta con formato"""
    print(Fore.YELLOW + f"\n[!] {mensaje}")

def buscar_alumno_por_rut(alumnos: List[Alumno], rut: str) -> Optional[Alumno]:
    """Busca un alumno por su RUT"""
    return next((a for a in alumnos if a.rut == rut), None)

def input_validado(prompt: str, tipo=str, validador=None, mensaje_error="Entrada inválida"):
    """
    Solicita input al usuario con validación
    Args:
        prompt: Mensaje a mostrar
        tipo: Tipo de dato esperado
        validador: Función de validación adicional
        mensaje_error: Mensaje a mostrar cuando falla la validación
    """
    while True:
        try:
            entrada = input(prompt).strip()
            if not entrada:
                raise ValueError("La entrada no puede estar vacía")
            
            valor = tipo(entrada)
            
            if validador and not validador(valor):
                raise ValueError(mensaje_error)
                
            return valor
        except ValueError as e:
            mostrar_error(f"{mensaje_error}: {e}")

def agregar_alumno(alumnos: List[Alumno]) -> None:
    """Registra un nuevo alumno en el sistema"""
    print(Fore.CYAN + "\n" + " REGISTRAR NUEVO ALUMNO ".center(50, "-"))
    
    nombre = input_validado(
        "Nombre completo: ",
        str,
        lambda x: len(x) >= 3,
        "El nombre debe tener al menos 3 caracteres"
    )
    
    rut = input_validado(
        "RUT (formato 12345678-9): ",
        str,
        validar_rut,
        "RUT inválido"
    )
    
    if buscar_alumno_por_rut(alumnos, rut):
        mostrar_error(f"Ya existe un alumno con RUT {rut}")
        return
    
    try:
        nuevo_alumno = Alumno(nombre, rut)
        alumnos.append(nuevo_alumno)
        guardar_alumnos(alumnos)
        mostrar_exito(f"Alumno {nombre} registrado exitosamente!")
    except Exception as e:
        mostrar_error(f"Error al registrar alumno: {e}")

def buscar_por_rut(alumnos: List[Alumno]) -> None:
    """Busca y muestra un alumno por su RUT"""
    print(Fore.CYAN + "\n" + " BUSCAR ALUMNO POR RUT ".center(50, "-"))
    
    rut = input_validado(
        "Ingrese RUT a buscar: ",
        str,
        validar_rut,
        "RUT inválido"
    )
    
    alumno = buscar_alumno_por_rut(alumnos, rut)
    
    if alumno:
        print(Fore.BLUE + "\n" + " RESULTADO DE BÚSQUEDA ".center(50, "="))
        print(alumno)
    else:
        mostrar_error("No se encontró ningún alumno con ese RUT")

def agregar_nota(alumnos: List[Alumno]) -> None:
    """Agrega una nota a un alumno existente"""
    print(Fore.CYAN + "\n" + " AGREGAR NOTA A ALUMNO ".center(50, "-"))
    
    rut = input_validado(
        "Ingrese RUT del alumno: ",
        str,
        validar_rut,
        "RUT inválido"
    )
    
    alumno = buscar_alumno_por_rut(alumnos, rut)
    
    if not alumno:
        mostrar_error("Alumno no encontrado")
        return
    
    print(Fore.YELLOW + f"\nAlumno encontrado: {alumno.nombre}")
    
    nota = input_validado(
        "Ingrese la nota (1.0-7.0): ",
        float,
        lambda x: 1.0 <= x <= 7.0,
        "La nota debe estar entre 1.0 y 7.0"
    )
    
    try:
        alumno.agregar_nota(nota)
        guardar_alumnos(alumnos)
        mostrar_exito(f"Nota {nota} agregada exitosamente a {alumno.nombre}")
    except ValueError as e:
        mostrar_error(str(e))

def mostrar_listado(alumnos: List[Alumno], titulo: str, filtro=None):
    """Muestra un listado de alumnos con formato"""
    print(Fore.BLUE + "\n" + f" {titulo} ".center(50, "="))
    
    alumnos_a_mostrar = [a for a in alumnos if filtro(a)] if filtro else alumnos
    
    if not alumnos_a_mostrar:
        mostrar_alerta("No hay alumnos para mostrar")
        return
    
    for i, alumno in enumerate(alumnos_a_mostrar, 1):
        print(Fore.YELLOW + f"\nAlumno #{i}")
        print(alumno)
        print(Fore.WHITE + "-"*50)

def mostrar_todos(alumnos: List[Alumno]) -> None:
    """Muestra todos los alumnos registrados"""
    mostrar_listado(alumnos, "LISTADO COMPLETO DE ALUMNOS")

def mostrar_aprobados(alumnos: List[Alumno]) -> None:
    """Muestra solo los alumnos aprobados"""
    mostrar_listado(
        alumnos, 
        "ALUMNOS APROBADOS",
        lambda a: a.estado == "Aprobado"
    )

def mostrar_reprobados(alumnos: List[Alumno]) -> None:
    """Muestra solo los alumnos reprobados"""
    mostrar_listado(
        alumnos,
        "ALUMNOS REPROBADOS",
        lambda a: a.estado == "Reprobado"
    )

def mostrar_ordenados_promedio(alumnos: List[Alumno]) -> None:
    """Muestra alumnos ordenados por promedio"""
    if not alumnos:
        mostrar_alerta("No hay alumnos registrados")
        return
    
    alumnos_ordenados = sorted(
        alumnos,
        key=lambda a: a.promedio,
        reverse=True
    )
    
    print(Fore.BLUE + "\n" + " ALUMNOS ORDENADOS POR PROMEDIO ".center(50, "="))
    
    for i, alumno in enumerate(alumnos_ordenados, 1):
        estado_color = Fore.GREEN if alumno.estado == "Aprobado" else Fore.RED
        print(Fore.YELLOW + f"\nPosición #{i} | Promedio: {alumno.promedio:.1f}")
        print(alumno)
        print(Fore.WHITE + "-"*50)

def buscar_por_nombre(alumnos: List[Alumno]) -> None:
    """Busca alumnos por coincidencia de nombre"""
    print(Fore.CYAN + "\n" + " BUSCAR ALUMNOS POR NOMBRE ".center(50, "-"))
    
    busqueda = input_validado(
        "Ingrese nombre o parte del nombre a buscar: ",
        str,
        lambda x: len(x) >= 2,
        "Debe ingresar al menos 2 caracteres"
    ).lower()
    
    resultados = [
        a for a in alumnos 
        if busqueda in a.nombre.lower()
    ]
    
    mostrar_listado(
        resultados,
        f"RESULTADOS PARA '{busqueda}'"
    )

def editar_alumno(alumnos: List[Alumno]) -> None:
    """Edita la información de un alumno existente"""
    print(Fore.CYAN + "\n" + " EDITAR ALUMNO ".center(50, "-"))
    
    rut = input_validado(
        "Ingrese RUT del alumno a editar: ",
        str,
        validar_rut,
        "RUT inválido"
    )
    
    alumno = buscar_alumno_por_rut(alumnos, rut)
    
    if not alumno:
        mostrar_error("Alumno no encontrado")
        return
    
    print(Fore.YELLOW + f"\nEditando alumno: {alumno.nombre} ({alumno.rut})")
    
    # Editar nombre
    nuevo_nombre = input(f"Nuevo nombre [{alumno.nombre}]: ").strip()
    if nuevo_nombre:
        alumno.nombre = nuevo_nombre
    
    # Editar notas
    print(Fore.YELLOW + "\nNotas actuales:", ", ".join(map(str, alumno.notas)))
    if input("\n¿Desea editar notas? (s/n): ").lower() == 's':
        alumno.notas = []
        while True:
            try:
                nota = input("Ingrese nota (1-7) o dejar vacío para terminar: ").strip()
                if not nota:
                    break
                nota = float(nota)
                if not validar_nota(nota):
                    mostrar_error("Nota debe estar entre 1.0 y 7.0")
                    continue
                alumno.agregar_nota(nota)
            except ValueError:
                mostrar_error("Debe ingresar un número válido")
    
    guardar_alumnos(alumnos)
    mostrar_exito(f"Alumno {alumno.nombre} actualizado correctamente")

def eliminar_alumno(alumnos: List[Alumno]) -> None:
    """Elimina un alumno del sistema"""
    print(Fore.RED + "\n" + " ELIMINAR ALUMNO ".center(50, "-"))
    
    rut = input_validado(
        "Ingrese RUT del alumno a eliminar: ",
        str,
        validar_rut,
        "RUT inválido"
    )
    
    alumno = buscar_alumno_por_rut(alumnos, rut)
    
    if not alumno:
        mostrar_error("Alumno no encontrado")
        return
    
    print(Fore.YELLOW + f"\nAlumno a eliminar: {alumno.nombre} ({alumno.rut})")
    
    if input("\n¿Está seguro que desea eliminar este alumno? (s/n): ").lower() == 's':
        alumnos.remove(alumno)
        guardar_alumnos(alumnos)
        mostrar_exito("Alumno eliminado correctamente")
    else:
        mostrar_alerta("Operación cancelada")

def generar_estadisticas(alumnos: List[Alumno]) -> None:
    """Genera estadísticas del curso"""
    if not alumnos:
        mostrar_alerta("No hay alumnos registrados")
        return
    
    promedios = [a.promedio for a in alumnos]
    aprobados = sum(1 for a in alumnos if a.estado == "Aprobado")
    
    print(Fore.BLUE + "\n" + " ESTADÍSTICAS DEL CURSO ".center(50, "="))
    print(Fore.YELLOW + f"\nTotal alumnos: {len(alumnos)}")
    print(f"Aprobados: {aprobados} ({aprobados/len(alumnos)*100:.1f}%)")
    print(f"Reprobados: {len(alumnos)-aprobados}")
    print(Fore.GREEN + f"\nMejor promedio: {max(promedios):.1f}")
    print(Fore.RED + f"Peor promedio: {min(promedios):.1f}")
    print(Fore.CYAN + f"Promedio general: {sum(promedios)/len(promedios):.1f}")

def generar_reporte_detallado(alumnos: List[Alumno]) -> None:
    """Genera un reporte detallado en formato tabla"""
    if not alumnos:
        mostrar_alerta("No hay alumnos registrados")
        return
    
    print(Fore.BLUE + "\n" + " REPORTE DETALLADO ".center(80, "="))
    print(Fore.YELLOW + "\n{:<5} {:<30} {:<15} {:<15} {:<10} {:<15}".format(
        "ID", "Nombre", "RUT", "Promedio", "Estado", "Notas"))
    print(Fore.WHITE + "-"*80)
    
    for idx, alumno in enumerate(alumnos, 1):
        estado_color = Fore.GREEN if alumno.estado == "Aprobado" else Fore.RED
        print(Fore.WHITE + "{:<5} {:<30} {:<15} {:<15.1f} {}{:<10}{} {:<15}".format(
            idx,
            alumno.nombre[:28] + "..." if len(alumno.nombre) > 28 else alumno.nombre,
            alumno.rut,
            alumno.promedio,
            estado_color,
            alumno.estado,
            Fore.WHITE,
            ", ".join(map(str, alumno.notas))[:20] + "..."))