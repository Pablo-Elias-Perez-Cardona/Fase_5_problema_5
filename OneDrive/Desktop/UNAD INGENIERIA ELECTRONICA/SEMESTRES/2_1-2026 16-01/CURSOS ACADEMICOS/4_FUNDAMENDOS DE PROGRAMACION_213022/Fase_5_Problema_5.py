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

# R4: Validar que los valores de horas sean numéricos
for recurso in equipo:                                            # Recorre cada fila de la matriz (cada recurso)
    nombre = recurso[0]                                           # El primer elemento de la fila es el nombre del recurso
    for hora in recurso[1:]:                                      # Recorre las horas de lunes a viernes (del segundo al sexto elemento)
        if not isinstance(hora, int):                             # Verifica si el valor NO es un número entero
            print(f"Error: el valor '{hora}' en el recurso {nombre} no es numérico")  
            # Si encuentra un error, muestra un mensaje indicando el recurso y el valor incorrecto

# R5: Función para calcular la suma de horas semanales por recurso
def calcular_jornada(recurso):                                    # Define una función que recibe como parámetro una fila de la matriz (un recurso)
    nombre = recurso[0]                                           # El primer elemento de la fila es el nombre del recurso
    horas = sum(recurso[1:])                                      # Suma todas las horas de lunes a viernes (del segundo al sexto elemento)
    return nombre, horas                                          # Devuelve el nombre del recurso y el total de horas trabajadas en la semana

# R6: Comparar el total de horas con el umbral de 40 horas
def clasificar_jornada(horas):                                    # Define una función que recibe el total de horas semanales
    if horas > 40:                                                # Si el total de horas es mayor a 40
        return "Sobretiempo"                                      # Devuelve la clasificación "Sobretiempo"
    else:                                                         # En cualquier otro caso (40 o menos)
        return "Horario estándar"                                 # Devuelve la clasificación "Horario estándar"

# R7: Integrar cálculo y clasificación en una sola función
def procesar_recurso(recurso):                                    # Define una función que recibe como parámetro una fila de la matriz (un recurso)
    nombre, horas = calcular_jornada(recurso)                     # Llama a la función calcular_jornada (R3) para obtener nombre y total de horas
    clasificacion = clasificar_jornada(horas)                     # Llama a la función clasificar_jornada (R4) para determinar la clasificación
    return nombre, horas, clasificacion                           # Devuelve el nombre, el total de horas y la clasificación final
