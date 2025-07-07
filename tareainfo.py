
def numnegativo():

    num1 = int(input("ingrese el numero 1: "))
    num2 = int(input("ingrese el numero 2: "))
    num3 = int(input("ingrese el numero 3: "))

    resultado1 = ""
    resultado2 = ""
    resultado3 = ""
    
    if num1 < 0:
        
        print("\nel numero 1 es negativo\n")
    else:
        print("el numero 1 es positivo")
    
    if num2 < 0:
        print("el numero 2 es negativo")
        
    else:
        print("el numero 2 es positivo")

    if num3 < 0:
        print("el numero 3 es negativo")
        
    else:
        print("\nel numero 3 es positivo\n")
def pares():
    num1 = int(input("ingrese el numero 1: "))
    num2 = int(input("ingrese el numero 2: "))
    num3 = int(input("ingrese el numero 3: "))

    if num1 % 2 == 0:
        print("\nel numero 1 es par\n")
    else:
        print("\nel numero 1 no es par\n")
    
    if num2 % 2 == 0:
        print("el numero 2 es par")
    else:
        print("el numero 2 no es par")
    
    if num3 % 2 == 0:
        print("\nel numero 3 es par\n")
    else:
        print("\nel numero 3 no es par\n")
def nummayor():
    num1 = int(input("ingrese el numero 1: "))
    num2 = int(input("ingrese el numero 2: "))
    num3 = int(input("ingrese el numero 3: "))
    
    mayor = max(num1, num2, num3)

    if num1 == num2 == num3:
        print("\nson iguales\n")
    else:
        print("el numero mas grande es:",mayor)
        print("")
def superior():
    num1 = int(input("ingrese el numero 1: "))
    num2 = int(input("ingrese el numero 2: "))
    num3 = int(input("ingrese el numero 3: "))

    if num1 + num2 + num3 >= 100:
        print("")
        print("el resultado de la suma es",num1 + num2 + num3)
    else:
        print("el resultado de la suma es",num1 + num2 + num3)
        print("\nes un numero superior o igual a 100\n")
        print("\nel numero es inferior a 100\n")  
while True:

    print("1:ver si un numero es negativo\n2:ver si un numero es par\n3:ver cual numero es mayor\n4:ver el tamaño de los numeros\n5:salir")
    respuesta = input()

    match respuesta:
        case "1":
            numnegativo()
        case "2":
            pares()
        case "3":
            nummayor()
        case "4":
            superior()
        case "5":
            break
    
    


    
    
    

    

    

