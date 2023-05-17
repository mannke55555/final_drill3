lista = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

def separar_magos_cientificos(lista):
    magos = []
    cientificos = []
    otros = []

    for lista in lista:
        if lista in ["Harry Houdini", "David Blaine", "Teller"]:
            magos.append(lista)
        elif lista in ["Newton", "Hawking", "Einstein"]:
            cientificos.append(lista)
        else:
            otros.append(lista)

    return magos, cientificos, otros

def hacer_grandioso(magos):
    for i in range(len(magos)):
        magos[i] = "El gran " + magos[i]

    return magos

def imprimir_nombres(lista):
    print("Lista completa:")
    print(lista)
    print()

# Lista completa
print("Lista completa:")
print(lista)
print()

# Separar magos, científicos y resto
magos, cientificos, otros = separar_magos_cientificos(lista)

# Lista de magos grandiosos
magos_grandiosos = hacer_grandioso(magos)
print("Magos grandiosos:")
print(magos_grandiosos)
print()

# Lista de científicos
print("Científicos:")
print(cientificos)
print()

# Lista de restantes
print("Otros:")
print(otros)
