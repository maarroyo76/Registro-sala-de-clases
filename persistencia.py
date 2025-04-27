import json
from  pathlib import Path
from typing import List
from alumno import Alumno


def guardar_alumnos(alumnos: List[Alumno], archivo: str = 'alumnos.json') -> None:
    datos = []
    for alumno in alumnos:
        datos.append({
            'nombre': alumno.nombre,
            'rut': alumno.rut,
            'notas': alumno.notas
        })
    
    with open(archivo, 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=2, ensure_ascii=False)


def cargar_alumnos(archivo: str = 'alumnos.json') -> List[Alumno]:
    if not Path(archivo).exists():
        return []
    
    with open(archivo, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    
    alumnos = []
    for dato in datos:
        try:
            alumno = Alumno(dato['nombre'], dato['rut'])
            alumno.notas = dato['notas']
            alumnos.append(alumno)
        except (KeyError, ValueError) as e:
            print(f"Error cargando alumno: {e}")
            continue
    
    return alumnos
