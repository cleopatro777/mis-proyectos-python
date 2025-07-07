lista = []

def añadir():
    while True:
        print("\n1:Añadir una tarea\n2:Salir")
        iopcion = input("Ingrese que desea realizar: ")
        

        match iopcion:

            case "1":
                tarea = input("Ingrese la tarea que desea realizar: ")

                if tarea not in lista:
                    lista.append(tarea)
                else:
                    print("Error, archivo repetido")
                print("")
                
            case "2":
                print("")
                break
def ver():
    print("")
    print(lista)
    print("")
def quitar():
        quitara = input("\nIngrese la tarea que desea eliminar: ")
        if quitara in lista:
             lista.remove(quitara)
             print("")
        else:
            print("Elemento no encontrado")
            print("")

while True:
    print("Opciones")
    print("1:Añadir una tarea\n2:Ver mi lista\n3:Eliminar una tarea\n4:Salir")
    opcion = input("Ingrese que desea realizar: ")

    match opcion:
        case "1":
            añadir()
        
        case "2":
            ver()

        case "3":
            quitar()

        case "4":
            break

    