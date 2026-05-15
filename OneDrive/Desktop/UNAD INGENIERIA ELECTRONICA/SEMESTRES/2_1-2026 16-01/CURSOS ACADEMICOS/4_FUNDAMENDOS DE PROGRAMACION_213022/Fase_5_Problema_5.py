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

    
    # R3: Pedir las horas trabajadas de lunes a viernes con validación
    for dia in ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]:
        while True:                                               # Repite hasta que el dato sea válido
            try:
                hora = int(input(f"Ingrese las horas trabajadas el {dia} por {nombre}: "))
                horas.append(hora)                                # Si es válido, agrega la hora a la lista
                break                                             # Sale del ciclo y pasa al siguiente día
            except ValueError:                                    # Si ocurre un error (dato no numérico)
                print("Error: valor no válido. Debe ingresar un número entero.")  
    equipo.append([nombre] + horas)                               # Construye la fila con nombre + horas y la agrega a la matriz 'equipo'
