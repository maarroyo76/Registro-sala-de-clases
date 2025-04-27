from validaciones import validar_nota, validar_rut

class Alumno:
    def __init__(self, nombre, rut):
        self.nombre = nombre
        if validar_rut is False:
            raise ValueError("Rut invalido")
        self.rut = rut
        self.notas = []

    def agregar_nota(self, nota):
        if validar_nota(nota) is False:
            raise ValueError("La nota debe estar entre 1.0 y 7.0")
        self.notas.append(nota)

    def promedio(self):
        if not self.notas:
            return 0.0
        return round(sum(self.notas) / len(self.notas), 1)

    def estado(self):
        return "Aprobado" if self.promedio() >= 4.0 else "Reprobado"
    
    def __str__(self):
        return(f"Alumno: {self.nombre}\n"
               f"RUT: {self.rut}\n"
               f"Notas: {', '.join(map(str, self.notas))}\n"
               f"Promedio: {self.promedio()}\n"
               f"Estado: {self.estado}")
               