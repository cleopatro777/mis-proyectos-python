#Inicio
print("Bienvenido al programa que apenas se me ocurrio despues de meses como hacer!!")
print("")
print("¿eres un poquito lento? ¡no te preocupes, este programa te ayudara a contar las palabras de una frase!")
print("")

#Codigo
frase = input("Ingrese la frase que deseas contar en palabras: ")
frasesp = frase.split()
fraselen = len(frasesp)

#Final
print(f"La frase tiene {fraselen} palabras")