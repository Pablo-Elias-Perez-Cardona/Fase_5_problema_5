print("Fase 5 ----------------------- Evaluacion Final POA")
print("Problema 5 ------------------- Horas trabajadas")
print("Nombre del estudiante:-------- Pablo Elías Pérez Cardona")
print("Grupo:------------------------ 213022_822")
print("Programa:--------------------- Fundamentos de programacion - Ingeniería Electrónica")
print("Código Fuente:---------------- autoría propia")

# R1: Solicitar al usuario el número de recursos
num_recursos = int(input("Ingrese el número de recursos: "))      # Pide cuántos recursos se van a ingresar y convierte la entrada a entero
equipo = []                                                       # Inicializa la matriz vacía donde se guardarán los recursos

# R2: Pedir nombre y horas de cada recurso (con validación)
for i in range(num_recursos):                                     # Recorre desde 0 hasta el número de recursos
    nombre = input(f"Ingrese el nombre del recurso {i+1}: ")      # Solicita el nombre del recurso actual
    horas = []                                                    # Lista vacía para almacenar las horas de lunes a viernes

