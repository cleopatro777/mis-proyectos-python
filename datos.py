grupo = []

# Cargar tareas existentes
with open("datos.txt", "r") as archivo:
    grupo = archivo.read().splitlines()


def añadir():
    print("")
    aña = input("Ingrese una tarea que añadir: ")
    grupo.append(aña)
    print("")


def ver():
    print("")
    print("Tareas actuales:")
    for tarea in grupo:
        print("-", tarea)
    print("")


def elim():
    print("")
    el = input("Ingrese la tarea que desee eliminar: ")
    if el in grupo:
        grupo.remove(el)
    else:
        print("Error, elemento no encontrado")
    print("")


while True:
    print("1: Agregar una tarea")
    print("2: Ver mi lista")
    print("3: Eliminar un elemento")
    print("4: Salir")

    opcion = input("\nIngrese su opción: ")

    match opcion:
        case "1":
            añadir()

        case "2":
            ver()

        case "3":
            elim()

        case "4":
            # Guardar al salir
            with open("datos.txt", "w") as archivo:
                for item in grupo:
                    archivo.write(item + "\n")
            print("Programa finalizado")
            break


