def mayor(lista):
    may = lista[0]
    for x in range(1, len(lista)):
        if lista[x] > may:
            may = lista[x]
    return may


def menor(lista):
    men = lista[0]
    for x in range(1, len(lista)):
        if lista[x] < men:
            men = lista[x]
    return men

#bloque principal del programa
lista = []
for x in range(5):
    valor = int(input("Ingrese un valor: "))
    lista.append(valor)

print("El valor mayor de la lista es: ", mayor(lista))
print("El valor menor de la lista es: ", menor(lista))