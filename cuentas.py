
usuario = ""
contraseña = ""
e = True
while e:

    print("\n1:crear cuenta\n2:iniciar sesion\n3:recuperar cuenta\n4:cerrar\n")#opciones
    opcion = input("que desea realizar: ")

    match opcion:
        case "1":#creamos la cuenta
            usuario = input("ingrese el usuario: ")
            contraseña = input("ingrese la contraseña: ")
            correo = input("(opcional)ingrese un correo : ")

        case "2":#iniciamos sesion
            numusu = input("ingrese el nombre de usuario: ")
            numcon = input("ingrese la contraseña: ")
            if numusu == usuario and numcon == contraseña: #si los datos son correctos
                print("\nha iniciado sesion\n")
            else:
                print("\nerror, nombre de usuario o contraseña incorrectas\n")#si los datos son incorrectos

        case "3":#recuperar la cuenta
            print("1:recuperar nombre de usuario\n2:recuperar contraseña\n")
            qhacer = input("eliga su opcion: ")#recuperar el nombre o la contraseña

            if qhacer == "1":#recuperar nombre de usuario
                incorreo = input("ingrese su correo: ")
                if incorreo == correo and usuario != "":
                    print("el usuario es:",usuario)
                else:
                    print("correo invalido")

            if qhacer == "2" and contraseña != "":#recuperar contraseña
                recorreo = input("ingrese el correo: ")
                if recorreo == correo:
                    print("la contraseña es:",contraseña)
                else:
                    print("correo invalido")

        case "4":#salir
            print("\nprograma finalizado\n")
            break