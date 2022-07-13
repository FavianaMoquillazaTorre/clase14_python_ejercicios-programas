def carga_lista():
    li = []
    for x in range(5):
        valor = int(input("Ingrese un valor: "))
        li.append(valor)
    return li

def retornar_mayormenor(li):
    may = li[0]
    men = li[0]
    for x in range(1, len(li)):
        if li[x] > may:
            may = li[x]
        else:
            if li[x] < men:
                men = li[x]
    return [may, men]


#bloque principal del programa

lista = carga_lista()
rango = retornar_mayormenor(lista)
print("Mayor elemento de la lista: ", rango[0])
print("Menor elemento de la lista: ", rango[1])