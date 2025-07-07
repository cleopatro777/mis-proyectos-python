#Elegir la frase
frase = input("Ingrese la frase: ")
frasere = frase
#Aqui se imprime el resultado
resultado = ""

#Por cada letra en la frase
for letra in range(len(frase)):
    
    i = frase[-1] # Detecta la ultima letra
    z = frase[:-1] #Le resta la ultima letra
    frase = z #Cambiamos el valor de la frase a la misma sin la ultima letra
    resultado += i #Imprimimos la ultima letra en i

    if len(resultado) == len(frasere): #Si el resultado tiene el mismo numero de letras que la frase
        print(resultado) #imprimir resultado paso a paso
