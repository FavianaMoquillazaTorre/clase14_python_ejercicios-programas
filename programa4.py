def cargar_sueldos():
    sueldos = []
    for x in range(10):
        su = int(input("Ingresar el sueldo: "))
        sueldos.append(su)
    return sueldos


def imprimir_sueldos(sueldos):
    print("Listado de sueldos de los empleados: ")
    for x in range(len(sueldos)):
        print(sueldos[x])


def sueldos_mayor4000(sueldos):
    cant = 0
    for x in range(len(sueldos)):
        if sueldos[x] > 4000:
            cant = cant+1
    print("Empleados con un sueldo superior a 4000: ", cant)


def promedio(sueldos):
    suma = 0
    for x in range(len(sueldos)):
        suma = suma+sueldos[x]
    promedio = suma//10
    return promedio

def sueldos_bajos(sueldos):
    pro = promedio(sueldos)
    print("Sueldo promedio de la empresa: ", pro)
    print("Sueldos que estan por debajo del promedio: ")
    for x in range(len(sueldos)):
        if sueldos[x]<pro:
            print(sueldos[x])


# bloque principal del programa

sueldos=cargar_sueldos()
imprimir_sueldos(sueldos)
sueldos_mayor4000(sueldos)
sueldos_bajos(sueldos)