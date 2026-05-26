

def ingresar_calificaciones():
    """
    ingresar_calificaciones() que permita al usuario introducir el nombre de una materia y su calificación correspondiente. Esta función debe:
    Solicitar al usuario que ingrese el nombre de la materia
    Solicitar la calificación (validando que sea un número entre 0 y 10)
    Almacenar ambos datos en dos listas separadas (una para nombres y otra para calificaciones)
    Preguntar si desea continuar ingresando más materias
    Retornar ambas listas cuando el usuario decida terminar

    parametres: no tiene parametros de entrada

    return materias, calificaciones
    """
    materias = []
    calificaciones = []

    while True:
        materia = input("Digite el nombre de la materia: ")
        materias.append(materia)

        while True:
            try:
                calificacion = float(input("Digite la calificación de la materia, solo se aceptan valores entre 0 y 10: "))
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    break
                else:
                    print("El número solo puede ser entre 0 y 10")
            except ValueError:
                print("El valor digitado no es válido")

        validar_continuar = input('¿Quiere digitar otra materia? s para si, o n para no: ').lower()
        if validar_continuar != 's':
            break

    return materias, calificaciones

def calcular_promedio(calificaciones):
    """
    calcular_promedio(calificaciones) que reciba la lista de calificaciones y calcule el promedio. Esta función debe:
    Sumar todas las calificaciones
    Dividir la suma entre el número total de calificaciones
    Retornar el promedio calculado

    parametres: calificaciones, una lista de números

    return el promedio de las materias la suma y se divide en el total de materia si es 0 se retorna el mismo valor para no dividir en 0
    """
    if len(calificaciones) == 0:
        return 0  # Evitar división por cero

    suma_calificaciones = sum(calificaciones)
    promedio = suma_calificaciones / len(calificaciones)
    return promedio


#valor predeterminado del umbral 5.0


def determinar_estado(calificaciones, umbral=5.0):
    ''' 
    separamos los indices que serian la posicion de cada nota en la lista en las aprobadas que superan el umbral y desaprobadas que no aprueban el umbral 

    parametres: calificaciones, una lista de números y umbral un numero que por defecto es 5.0

    return dos listas una con los indices de las materias aprobadas y otra con los indices de las materias reprobadas
    
    '''
    aprobadas = []
    reprobadas = []

    for i in range(len(calificaciones)):

        if calificaciones[i] >= umbral:
            aprobadas.append(i)
        else:
            reprobadas.append(i)

    return aprobadas,reprobadas

def encontrar_extremos(calificaciones):

    indice_masalta = 0
    indice_masbaja = 0
    for i in range(len(calificaciones)):
        
        if calificaciones[i] > calificaciones[indice_masalta]:
            indice_masalta = i
        
        if calificaciones[i] < calificaciones[indice_masbaja]:
            indice_masbaja = i

    return indice_masalta, indice_masbaja    
   

def main():
    '''Función principal que coordina la ejecución del programa. Esta función debe:
    Llamar a ingresar_calificaciones() para obtener las listas de materias y calificaciones
    Llamar a calcular_promedio() y mostrar el resultado al usuario'''

    #entrada de datos y generar promedio y determinar estado de cada materia y encontrar la nota mas alta y mas baja
    materias, calificaciones = ingresar_calificaciones()
    promedio = calcular_promedio(calificaciones)
    aprobadas, reprobadas = determinar_estado(calificaciones)
    indice_masalta, indice_masbaja = encontrar_extremos(calificaciones)
    
    print("-" * 40 + "\n") 
    print("las materias digitadas son: \n")
    for i in range(len(materias)):

        print(f'{materias[i]}: {calificaciones[i]}')
        
    print('\n' + "-" * 40  + '\n')
    
    print('el promedio general es: ', promedio )

    print('\n' + "-" * 40  + '\n')
    
    print('las materias aprobadas son: \n')

    for i in range(len(aprobadas)):
        print(materias[aprobadas[i]])
    
    print("\nlas materias reprobadas son: \n")

    for i in range(len(reprobadas)):
        print(materias[reprobadas[i]])

    print('\n' + "-" * 40  + '\n')

    print(f'la nota con mayor calificacion es:  {materias[indice_masalta]} con:  {calificaciones[indice_masalta]}')
    print(f'la nota con menor calificacion es:  {materias[indice_masbaja]} con:  {calificaciones[indice_masbaja]}')

    print('\n' + "-" * 40  + '\n')


if __name__ == "__main__":
    main()
 
  
  

