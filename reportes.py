# reportes.py
from typing import List
from alumno import Alumno
from colorama import Fore

def generar_estadisticas(alumnos: List[Alumno]):
    """Genera un reporte estadístico completo"""
    if not alumnos:
        print(Fore.YELLOW + "\nNo hay alumnos registrados")
        return
    
    promedios = [a.promedio() for a in alumnos]
    aprobados = sum(1 for a in alumnos if a.estado() == "Aprobado")
    
    print(Fore.CYAN + "\n" + " ESTADÍSTICAS DEL CURSO ".center(50, "="))
    print(Fore.YELLOW + f"\nTotal alumnos: {len(alumnos)}")
    print(f"Aprobados: {aprobados} ({aprobados/len(alumnos)*100:.1f}%)")
    print(f"Reprobados: {len(alumnos)-aprobados}")
    print(Fore.GREEN + f"\nMejor promedio: {max(promedios):.1f}")
    print(Fore.RED + f"Peor promedio: {min(promedios):.1f}")
    print(Fore.BLUE + f"Promedio general: {sum(promedios)/len(promedios):.1f}")

def generar_reporte_detallado(alumnos: List[Alumno]):
    """Genera un reporte detallado en formato tabla"""
    from colorama import Fore, Back
    print(Fore.BLUE + "\n" + " REPORTE DETALLADO ".center(80, "="))
    print(Fore.YELLOW + "\n{:<5} {:<30} {:<15} {:<15} {:<10} {:<10}".format(
        "ID", "Nombre", "RUT", "Promedio", "Estado", "Notas"))
    print("-"*80)
    
    for idx, alumno in enumerate(alumnos, 1):
        estado_color = Fore.GREEN if alumno.estado() == "Aprobado" else Fore.RED
        print(Fore.WHITE + "{:<5} {:<30} {:<15} {:<15.1f} {}{:<10}{} {:<10}".format(
            idx,
            alumno.nombre[:28] + "..." if len(alumno.nombre) > 28 else alumno.nombre,
            alumno.rut,
            alumno.promedio(),
            estado_color,
            alumno.estado(),
            Fore.WHITE,
            ", ".join(map(str, alumno.notas))[:20] + "..."))