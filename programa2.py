def mascaracteres(palabras):
    pos = 0
    for x in range(len(palabras)):
        if len(palabras[x]) > len(palabras[pos]):
            pos = x
    return palabras[pos]


#bloque principal del programa
palabras = ["primavera", "verano", "otoño", "invierno"]
print("Palabra con mas caracteres:", mascaracteres(palabras))