#!/usr/bin/env python3
# main.py - Programa principal del Sistema de Gestión de Alumnos

import os
from typing import List
from colorama import init, Fore, Style
from alumno import Alumno
from persistencia import cargar_alumnos, guardar_alumnos
from funciones import (
    mostrar_menu_principal,
    agregar_alumno,
    buscar_por_rut,
    agregar_nota,
    mostrar_todos,
    mostrar_aprobados,
    mostrar_reprobados,
    mostrar_ordenados_promedio,
    buscar_por_nombre,
    editar_alumno,
    eliminar_alumno,
    mostrar_error,
    mostrar_exito
)
from reportes import generar_estadisticas, generar_reporte_detallado

# Inicializar colorama
init(autoreset=True)

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    """Muestra el banner inicial del programa"""
    limpiar_pantalla()
    print(Fore.BLUE + Style.BRIGHT + "="*60)
    print(Fore.CYAN + " SISTEMA DE GESTIÓN DE ALUMNOS ".center(60, "="))
    print(Fore.BLUE + "="*60)
    print(Fore.YELLOW + "\nVersión 2.0 - Gestión Académica".center(60))
    print(Fore.GREEN + "\nDesarrollado por: [Tu Nombre]".center(60))
    print(Fore.BLUE + "\n" + "="*60 + "\n")

def inicializar_sistema() -> List[Alumno]:
    """Carga los datos iniciales del sistema"""
    try:
        alumnos = cargar_alumnos()
        mostrar_exito(f"Datos cargados correctamente ({len(alumnos)} alumnos registrados)")
        return alumnos
    except Exception as e:
        mostrar_error(f"Error al cargar datos: {str(e)}")
        return []

def manejar_opcion(opcion: str, alumnos: List[Alumno]) -> bool:
    """Procesa la opción seleccionada por el usuario"""
    try:
        if opcion == "1":
            agregar_alumno(alumnos)
        elif opcion == "2":
            buscar_por_rut(alumnos)
        elif opcion == "3":
            agregar_nota(alumnos)
        elif opcion == "4":
            mostrar_todos(alumnos)
        elif opcion == "5":
            mostrar_aprobados(alumnos)
        elif opcion == "6":
            mostrar_reprobados(alumnos)
        elif opcion == "7":
            mostrar_ordenados_promedio(alumnos)
        elif opcion == "8":
            buscar_por_nombre(alumnos)
        elif opcion == "9":
            editar_alumno(alumnos)
        elif opcion == "10":
            eliminar_alumno(alumnos)
        elif opcion == "11":
            generar_estadisticas(alumnos)
        elif opcion == "12":
            generar_reporte_detallado(alumnos)
        elif opcion == "0":
            guardar_alumnos(alumnos)
            mostrar_exito("Datos guardados correctamente. ¡Hasta pronto!")
            return False
        else:
            mostrar_error("Opción no válida. Por favor ingrese un número del 0 al 13")
    except Exception as e:
        mostrar_error(f"Error inesperado: {str(e)}")
    
    input(Fore.YELLOW + "\nPresione Enter para continuar...")
    return True

def main():
    """Función principal del programa"""
    mostrar_banner()
    alumnos = inicializar_sistema()
    
    ejecutando = True
    while ejecutando:
        try:
            limpiar_pantalla()
            mostrar_menu_principal()
            opcion = input(Fore.CYAN + "\nSeleccione una opción (0-13): " + Fore.WHITE).strip()
            ejecutando = manejar_opcion(opcion, alumnos)
        except KeyboardInterrupt:
            print(Fore.RED + "\n\nInterrupción detectada. ¿Desea salir? (s/n): ", end="")
            if input().lower() == 's':
                guardar_alumnos(alumnos)
                ejecutando = False
            else:
                continue
        except Exception as e:
            mostrar_error(f"Error crítico: {str(e)}")
            ejecutando = False

if __name__ == "__main__":
    main()